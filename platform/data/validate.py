#!/usr/bin/env python3
"""Validate the platform's machine-readable single source of truth.

Run from anywhere (isolated mode recommended):

    python3 -I platform/data/validate.py
    python3 -I .../validate.py --write-derived   # recompute derived values in place, then validate

Checks (errors make the exit code 1; warnings do not):
  1. JSON Schema of every dataset (schemas/*.schema.json; uses `jsonschema` if installed,
     otherwise a built-in subset validator).
  2. Unique ids; every referenced figure id, yardstick id, source id, multiplier class,
     party id, lever id and misperception id exists.
  3. Recomputes every derived value from figures.json and flags relative mismatches > 0.5%:
     yardsticks (formula), proposal conversions (days of spending, % of the 2025 deficit,
     EUR per inhabitant), lever ceilings defined as a share of a base figure, quiz answers
     that carry a formula.
  4. Greps the research markdown: every figures.json value must appear in its row of
     file 00 (canonical figures) or in its topic file (topic-file inputs); file 20 is
     scanned too and reported. Numbers in proposals and levers are checked against the
     research files they cite (warnings).
  5. Editorial rules: no unverified (warning-sign) items, every % figure says whether it
     is % of GDP or % of total spending, every proposal and lever has a counter-argument
     or caveat field, symmetry of the simulator menu and of the quiz pool.
  6. Quiz draw rule (quiz.json design.draw_rule): the bank holds as many left- as right-coded
     items, every draw size is feasible, and 500 seeded draws of the reference procedure never
     contain more right- than left-coded items, or vice versa.
  7. Rating history (figures.json rating_actions / rating_tables): ids, dates, and each action's
     match_text found in its research file.
  8. Chapters (fr/site/chapitres/*.md, outside HTML comments and inline code): every
     [[fig:]], [[yard:]] (also the alias [[yd:]], warned), [[prop:]], [[src:]], [[quiz:]] chip
     resolves, the ids used in [[calc:]] exist, and no placeholder remains ([[fig-a-creer:]],
     "EN ATTENTE DE DONNEES"). [[yard:id]] resolves against yardsticks[] first, then
     yardsticks.json parameters[] (e.g. household_monthly_income_eur). Chapter problems are
     reported as errors prefixed "chapters/"; --data-only skips this check.
  9. Chapter lints on the displayed text ("> " lines, outside comments, front matter and review notes);
     each message carries a [code]. Errors (always): [num-chip] a displayed number that does not
     round to its chip (value, range low/high, x100, x1000, day-of-year date) at its own decimals;
     [calc-value] a [[calc:]] whose stated result differs from the evaluated formula. With --strict,
     also errors (warnings otherwise): calc-no-id, calc-no-result, acronym (first occurrence not
     expanded), estimate-leak, internal-ref, word-count (1,500-2,200), level-shown. Warnings:
     chip-mismatch / chip-no-number (mark context chips [[fig:id|contexte]] or
     <!-- contexte: id -->), calc-rounding, calc-eval, calc-not-shown, unchipped (incl. chips only in
     Pastilles/Visuel lines), rounding (same id, different rounding across chapters; optional
     figures/yardsticks "display" field; yardstick display_decimals), same-number-ids,
     same-value-ids (unless the page says "coïncidence"), estimate-answer / estimate-repeat,
     denominator, typo-* (minus, Md€/Mds/bn, 2ème, straight quotes, em dash, hyphen ranges, italics of
     glossary §3 titles), box-* (title, bold thesis, italic source with a §1.13 label, « Ce qu’on peut
     répondre », <!-- box-side: gauche|droite|les-deux --> tag and site tally), orientation (§1.13
     labels), banned-word (§4.4), long-sentence (> 25 words), long-paragraph (> 60), reading-time
     (round(words / 240)), title / step-heading / chapter-ref (plan §2.1), symmetry-gate
     (<!-- symmetry-gate: ids=a,b | claim -->), quiz-rounding.
     Options: --strict, --no-lint, --details, --lint-only CODES, --chapters DIR.
 10. Lint exemptions (lint-exemptions.json, next to this script): documented, exact-match exemptions
     for legitimate coincidences. Today only same-number-ids is exemptable: an entry silences the
     warning only when the displayed number, the unit and the full set of chip ids all match; a third
     id with the same number is still reported. The file is validated (data error if malformed or if
     an id does not resolve), every applied exemption is listed as INFO, and an entry that matches no
     finding is reported as a stale-exemption warning (with --strict too: it is a warning, not an error).
"""
import argparse
import ast
import datetime as _dt
import fnmatch
import itertools
import json
import math
import operator
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RESEARCH = os.path.normpath(os.path.join(HERE, "..", "..", "research"))
CHAPTERS = os.path.normpath(os.path.join(HERE, "..", "..", "fr", "site", "chapitres"))
TOL = 0.005  # 0.5 %

DATASETS = {
    "figures": "figures.json",
    "yardsticks": "yardsticks.json",
    "levers": "simulator-levers.json",
    "quiz": "quiz.json",
    "proposals": "proposals.json",
    "sources": "sources.json",
}

ERRORS, WARNINGS, INFO = [], [], []


EXEMPTIONS_FILE = os.path.join(HERE, "lint-exemptions.json")
EXEMPTIONS = {"same_number_ids": [], "used": set()}


def load_exemptions(data):
    """Read and check lint-exemptions.json (check 10). Missing file = no exemption."""
    if not os.path.exists(EXEMPTIONS_FILE):
        INFO.append("lint exemptions: none (lint-exemptions.json absent)")
        return
    try:
        with open(EXEMPTIONS_FILE, encoding="utf-8") as f:
            ex = json.load(f)
    except (OSError, ValueError) as e:
        err(f"lint-exemptions.json: cannot be read ({e})")
        return
    fig_ids = {f["id"] for f in data["figures"]["figures"]}
    pools = {"fig": fig_ids | {t["id"] for t in data["figures"].get("rating_tables", [])},
             "yard": {y["id"] for y in data["yardsticks"]["yardsticks"]} |
                     {p["id"] for p in data["yardsticks"].get("parameters", [])}}
    seen = set()
    for i, e in enumerate(ex.get("same_number_ids", [])):
        w = f"lint-exemptions.json/same_number_ids[{i}]"
        missing = [k for k in ("number", "unit", "ids", "reason_en", "decided_by", "date") if not e.get(k)]
        if missing:
            err(f"{w}: missing {', '.join(missing)}")
            continue
        try:
            _dt.date.fromisoformat(e["date"])
        except ValueError:
            err(f"{w}: invalid date {e['date']}")
        ids = e["ids"]
        if len(set(ids)) < 2:
            err(f"{w}: needs at least two distinct ids")
            continue
        bad = [x for x in ids if ":" not in x or x.split(":", 1)[1] not in pools.get(x.split(":", 1)[0], set())]
        if bad:
            err(f"{w}: unknown chip id(s) {', '.join(bad)}")
            continue
        key = (_norm(e["number"]), e["unit"])
        if key in seen:
            err(f"{w}: duplicate entry for {e['number']} {e['unit']}")
        seen.add(key)
        EXEMPTIONS["same_number_ids"].append((key, frozenset(ids), e))


def exempt_same_number(txt, unit, ids):
    """True when (txt, unit, ids) is covered by a documented exemption."""
    for i, (key, allowed, e) in enumerate(EXEMPTIONS["same_number_ids"]):
        if key == (txt, unit) and set(ids) <= allowed:
            EXEMPTIONS["used"].add(i)
            INFO.append(f"lint exemption applied: same-number-ids {txt} {unit} ({', '.join(sorted(ids))}): "
                        f"{e['reason_en'][:90]}…")
            return True
    return False


def err(msg):
    ERRORS.append(msg)


def warn(msg):
    WARNINGS.append(msg)


# --------------------------------------------------------------------------- loading
def load(name):
    with open(os.path.join(HERE, name), encoding="utf-8") as f:
        return json.load(f)


def load_all():
    return {k: load(v) for k, v in DATASETS.items()}


# --------------------------------------------------------------------------- formula evaluation
_OPS = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul,
        ast.Div: operator.truediv, ast.Pow: operator.pow, ast.USub: operator.neg, ast.UAdd: operator.pos}


def formula_names(expr):
    return sorted({n.id for n in ast.walk(ast.parse(expr, mode="eval")) if isinstance(n, ast.Name)})


def evaluate(expr, env):
    """Evaluate an arithmetic formula over named values (no calls, no attributes)."""
    def ev(node):
        if isinstance(node, ast.Expression):
            return ev(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return float(node.value)
        if isinstance(node, ast.Name):
            if node.id not in env:
                raise KeyError(node.id)
            v = env[node.id]
            if v is None:
                raise ValueError(f"{node.id} has no point value")
            return float(v)
        if isinstance(node, ast.BinOp) and type(node.op) in _OPS:
            return _OPS[type(node.op)](ev(node.left), ev(node.right))
        if isinstance(node, ast.UnaryOp) and type(node.op) in _OPS:
            return _OPS[type(node.op)](ev(node.operand))
        raise ValueError(f"unsupported syntax in formula: {expr}")
    return ev(ast.parse(expr, mode="eval"))


def rel_diff(a, b):
    if a == b:
        return 0.0
    denom = max(abs(a), abs(b))
    return abs(a - b) / denom if denom else 0.0


def decimals_of(x):
    s = repr(float(x))
    if "e" in s:
        return 6
    return len(s.split(".")[1].rstrip("0")) if "." in s else 0


def matches_published(value, published):
    """A published (rounded) number matches if within 0.5 % or equal after rounding."""
    if rel_diff(value, published) <= TOL:
        return True
    d = decimals_of(published)
    return round(value, d) == round(published, d)


# --------------------------------------------------------------------------- environment
def figure_env(data):
    env = {f["id"]: f["value"] for f in data["figures"]["figures"]}
    for f in data["figures"]["figures"]:
        if f.get("range"):
            env[f["id"] + "__low"] = f["range"]["low"]
            env[f["id"] + "__high"] = f["range"]["high"]
    for p in data["yardsticks"].get("parameters", []):
        env[p["id"]] = p["value"]
    for mc in data["levers"].get("multiplier_classes", []):
        for h in ("y1", "y3_5"):
            if mc.get(h):
                for pos, suffix in (("default", ""), ("low", "_low"), ("high", "_high")):
                    if mc[h].get(pos) is not None:
                        env[f"mult_{mc['id']}_{h}{suffix}"] = mc[h][pos]
    return env


def compute_yardsticks(data):
    """Evaluate yardsticks in order (later ones may use earlier ones)."""
    env = figure_env(data)
    out = {}
    for y in data["yardsticks"]["yardsticks"]:
        try:
            v = evaluate(y["formula"], env)
        except Exception as e:  # noqa: BLE001
            err(f"yardsticks: {y['id']}: cannot evaluate formula '{y['formula']}': {e}")
            continue
        out[y["id"]] = v
        env[y["id"]] = v
    return out, env


def conversion_constants(data):
    """Denominators of the proposal checker, recomputed from figures.json."""
    env = {f["id"]: f["value"] for f in data["figures"]["figures"]}
    c = data["yardsticks"]["conversions"]
    return {
        "one_day": evaluate(c["one_day_spending_eur_bn"], env),
        "deficit": evaluate(c["deficit_eur_bn"], env),
        "population_m": evaluate(c["population_m"], env),
        "te": evaluate(c["te_eur_bn"], env),
        "gdp": evaluate(c["gdp_eur_bn"], env),
    }


def convert(amount, k):
    if amount is None:
        return None
    return {
        "days_of_spending": amount / k["one_day"],
        "pct_of_deficit": amount / k["deficit"] * 100,
        "eur_per_inhabitant": amount * 1000 / k["population_m"],
        "pct_of_total_spending": amount / k["te"] * 100,
        "pct_of_gdp": amount / k["gdp"] * 100,
    }


def convert_band(band, k):
    if not band:
        return None
    out = {}
    for pos in ("low", "central", "high"):
        c = convert(band.get(pos), k)
        if c is None:
            continue
        for metric, v in c.items():
            out.setdefault(metric, {})[pos] = v
    return out


ROUNDING = {"days_of_spending": 2, "pct_of_deficit": 2, "eur_per_inhabitant": 1,
            "pct_of_total_spending": 3, "pct_of_gdp": 3}


def round_band(d):
    if d is None:
        return None
    return {m: {p: round(v, ROUNDING[m]) for p, v in pos.items()} for m, pos in d.items()}


def proposal_bands(p):
    """Which amounts are converted: the party claim and the summary range."""
    bands = {}
    if p.get("claimed") and any(p["claimed"].get(x) is not None for x in ("low", "central", "high")):
        bands["claimed"] = p["claimed"]
    if p.get("range") and any(p["range"].get(x) is not None for x in ("low", "central", "high")):
        bands["range"] = p["range"]
    for pt in p.get("claimed_path") or []:
        bands[f"claimed_{pt['year']}"] = {"low": None, "central": pt["central"], "high": None}
    return bands


def lever_ceiling(lever, env):
    """Yield at the lever's maximum setting when it is defined as share x base figure."""
    ym = lever.get("yield_model") or {}
    if ym.get("kind") != "share_of_base":
        return None
    ids = [ym["base_figure_id"]] + list(ym.get("extra_base_figure_ids") or [])
    vals = [env.get(i) for i in ids]
    if any(v is None for v in vals):
        return None
    return sum(vals) * ym["max_share"]


# --------------------------------------------------------------------------- write-derived
def write_derived(data):
    ys, _ = compute_yardsticks(data)
    for y in data["yardsticks"]["yardsticks"]:
        if y["id"] in ys:
            y["value"] = round(ys[y["id"]], y.get("store_decimals", 4))
            if y.get("date_from_day_of_year"):
                y["value_date"] = day_to_date(y["value"], y["date_from_day_of_year"])
    k = conversion_constants(data)
    for p in data["proposals"]["proposals"]:
        p["derived"] = {name: round_band(convert_band(b, k)) for name, b in proposal_bands(p).items()}
    env = figure_env(data)
    for lv in data["levers"]["levers"]:
        c = lever_ceiling(lv, env)
        if c is not None:
            lv["yield_model"]["max_yield_eur_bn"] = round(c, 3)
    for name in ("yardsticks", "proposals", "levers"):
        with open(os.path.join(HERE, DATASETS[name]), "w", encoding="utf-8") as f:
            json.dump(data[name], f, ensure_ascii=False, indent=2)
            f.write("\n")


def day_to_date(day_offset, year):
    return (_dt.date(int(year), 1, 1) + _dt.timedelta(days=int(math.floor(day_offset)))).isoformat()


# --------------------------------------------------------------------------- 1. schemas
def _mini_validate(inst, schema, root, path="$"):
    """Subset of JSON Schema 2020-12 used by this project's schemas."""
    if "$ref" in schema:
        ref = schema["$ref"]
        assert ref.startswith("#/$defs/"), ref
        return _mini_validate(inst, root["$defs"][ref.split("/")[-1]], root, path)
    if "anyOf" in schema:
        errs = [_mini_validate(inst, s, root, path) for s in schema["anyOf"]]
        if all(errs):
            return [f"{path}: does not match anyOf"]
    out = []
    t = schema.get("type")
    if t:
        types = t if isinstance(t, list) else [t]
        ok = False
        for ty in types:
            if ty == "null" and inst is None: ok = True
            elif ty == "object" and isinstance(inst, dict): ok = True
            elif ty == "array" and isinstance(inst, list): ok = True
            elif ty == "string" and isinstance(inst, str): ok = True
            elif ty == "boolean" and isinstance(inst, bool): ok = True
            elif ty == "integer" and isinstance(inst, int) and not isinstance(inst, bool): ok = True
            elif ty == "number" and isinstance(inst, (int, float)) and not isinstance(inst, bool): ok = True
        if not ok:
            return [f"{path}: expected {t}, got {type(inst).__name__}"]
    if "enum" in schema and inst not in schema["enum"]:
        out.append(f"{path}: {inst!r} not in enum")
    if "const" in schema and inst != schema["const"]:
        out.append(f"{path}: expected const {schema['const']!r}")
    if isinstance(inst, str) and "pattern" in schema and not re.search(schema["pattern"], inst):
        out.append(f"{path}: {inst!r} does not match {schema['pattern']}")
    if isinstance(inst, (int, float)) and not isinstance(inst, bool):
        if "minimum" in schema and inst < schema["minimum"]:
            out.append(f"{path}: below minimum")
        if "maximum" in schema and inst > schema["maximum"]:
            out.append(f"{path}: above maximum")
    if isinstance(inst, dict):
        for r in schema.get("required", []):
            if r not in inst:
                out.append(f"{path}: missing required '{r}'")
        props = schema.get("properties", {})
        pats = schema.get("patternProperties", {})
        for k, v in inst.items():
            pat = next((pp for pp in pats if re.search(pp, k)), None)
            if k in props:
                out += _mini_validate(v, props[k], root, f"{path}.{k}")
            elif pat is not None:
                out += _mini_validate(v, pats[pat], root, f"{path}.{k}")
            elif schema.get("additionalProperties") is False:
                out.append(f"{path}: unexpected property '{k}'")
            elif isinstance(schema.get("additionalProperties"), dict):
                out += _mini_validate(v, schema["additionalProperties"], root, f"{path}.{k}")
    if isinstance(inst, list):
        if "minItems" in schema and len(inst) < schema["minItems"]:
            out.append(f"{path}: fewer than {schema['minItems']} items")
        if "items" in schema:
            for i, v in enumerate(inst):
                out += _mini_validate(v, schema["items"], root, f"{path}[{i}]")
    return out


def check_schemas(data):
    try:
        import jsonschema  # type: ignore
    except Exception:  # noqa: BLE001
        jsonschema = None
    engine = "jsonschema" if jsonschema else "built-in subset"
    for key, fname in DATASETS.items():
        sp = os.path.join(HERE, "schemas", fname.replace(".json", ".schema.json"))
        if not os.path.exists(sp):
            err(f"schema missing: {sp}")
            continue
        with open(sp, encoding="utf-8") as f:
            schema = json.load(f)
        if jsonschema:
            v = jsonschema.Draft202012Validator(schema)
            problems = [f"{'/'.join(map(str, e.absolute_path))}: {e.message}" for e in v.iter_errors(data[key])]
        else:
            problems = _mini_validate(data[key], schema, schema)
        for p in problems[:20]:
            err(f"schema {fname}: {p}")
        if len(problems) > 20:
            err(f"schema {fname}: ... {len(problems) - 20} more")
    INFO.append(f"schemas checked with {engine}")


# --------------------------------------------------------------------------- 2. references
def check_unique(items, label):
    seen = set()
    for it in items:
        if it["id"] in seen:
            err(f"{label}: duplicate id {it['id']}")
        seen.add(it["id"])
    return seen


def check_references(data):
    fig_ids = check_unique(data["figures"]["figures"], "figures")
    y_ids = check_unique(data["yardsticks"]["yardsticks"], "yardsticks")
    p_ids = {p["id"] for p in data["yardsticks"].get("parameters", [])}
    src_ids = set(data["sources"]["sources"].keys())
    mc_ids = check_unique(data["levers"]["multiplier_classes"], "multiplier_classes")
    lever_ids = check_unique(data["levers"]["levers"], "levers")
    party_ids = {p["id"] for p in data["proposals"]["proposers"]}
    misp_ids = check_unique(data["quiz"]["misperceptions"], "misperceptions")
    check_unique(data["quiz"]["questions"], "quiz")
    check_unique(data["proposals"]["proposals"], "proposals")
    mult_names = {f"mult_{m}_{h}{s}" for m in mc_ids for h in ("y1", "y3_5") for s in ("", "_low", "_high")}
    range_names = {f["id"] + suf for f in data["figures"]["figures"] if f.get("range") for suf in ("__low", "__high")}
    known = fig_ids | y_ids | p_ids | mult_names | range_names

    def need(ids, pool, where, what):
        for i in ids or []:
            if i not in pool:
                err(f"{where}: unknown {what} '{i}'")

    for f in data["figures"]["figures"]:
        need([f["source_id"]], src_ids, f"figures/{f['id']}", "source id")
    seen = set(fig_ids) | p_ids | mult_names | range_names
    for y in data["yardsticks"]["yardsticks"]:
        for n in formula_names(y["formula"]):
            if n not in known:
                err(f"yardsticks/{y['id']}: formula references unknown id '{n}'")
            elif n in y_ids and n not in seen:
                err(f"yardsticks/{y['id']}: uses yardstick '{n}' before it is defined")
        seen.add(y["id"])
        need(y.get("figure_ids"), fig_ids, f"yardsticks/{y['id']}", "figure id")
    for name, expr in data["yardsticks"]["conversions"].items():
        if name.endswith("_note"):
            continue
        for n in formula_names(expr):
            if n not in fig_ids:
                err(f"yardsticks/conversions/{name}: unknown figure id '{n}'")
    for lv in data["levers"]["levers"]:
        w = f"levers/{lv['id']}"
        need(lv.get("figure_ids"), fig_ids, w, "figure id")
        need(lv.get("source_ids"), src_ids, w, "source id")
        need([lv["multiplier_class"]], mc_ids, w, "multiplier class")
        need(lv.get("political_origin", {}).get("proposed_by"), party_ids, w, "party id")
        need(lv.get("political_origin", {}).get("opposite_direction_by"), party_ids, w, "party id")
        need(lv.get("related_proposal_ids"), {p["id"] for p in data["proposals"]["proposals"]}, w, "proposal id")
        ym = lv.get("yield_model") or {}
        if ym.get("base_figure_id"):
            need([ym["base_figure_id"]] + list(ym.get("extra_base_figure_ids") or []), fig_ids, w, "base figure id")
    for rule in data["levers"]["anti_double_counting"]:
        need(rule["levers"], lever_ids, f"anti_double_counting/{rule['id']}", "lever id")
    for mc in data["levers"]["multiplier_classes"]:
        need(mc.get("source_ids"), src_ids, f"multiplier_classes/{mc['id']}", "source id")
    for m in data["quiz"]["misperceptions"]:
        need(m.get("source_ids"), src_ids, f"misperceptions/{m['id']}", "source id")
        need(m.get("true_value_figure_ids"), fig_ids | y_ids, f"misperceptions/{m['id']}", "figure id")
    for q in data["quiz"]["questions"]:
        w = f"quiz/{q['id']}"
        need(q.get("figure_ids"), fig_ids | y_ids, w, "figure/yardstick id")
        need(q.get("source_ids"), src_ids, w, "source id")
        need(q.get("misperception_ids"), misp_ids, w, "misperception id")
        if q.get("formula"):
            for n in formula_names(q["formula"]):
                if n not in known:
                    err(f"{w}: formula references unknown id '{n}'")
    for p in data["proposals"]["proposals"]:
        w = f"proposals/{p['id']}"
        need(p.get("parties"), party_ids, w, "party id")
        need(p.get("source_ids"), src_ids, w, "source id")
        need(p.get("context_figure_ids"), fig_ids | y_ids, w, "figure id")
        for e in p.get("estimates", []):
            need(e.get("source_ids"), src_ids, w + "/estimates", "source id")
        need(p.get("lever_ids"), lever_ids, w, "lever id")
    for sid, s in data["sources"]["sources"].items():
        if sid != s["id"]:
            err(f"sources: key {sid} != id {s['id']}")
    act_ids = check_unique(data["figures"].get("rating_actions", []), "rating_actions")
    tab_ids = check_unique(data["figures"].get("rating_tables", []), "rating_tables")
    if tab_ids & fig_ids:
        err(f"rating_tables: ids clash with figure ids: {sorted(tab_ids & fig_ids)}")
    for t in data["figures"].get("rating_tables", []):
        need(t.get("figure_ids"), fig_ids, f"rating_tables/{t['id']}", "figure id")
        need(t.get("action_ids"), act_ids, f"rating_tables/{t['id']}", "rating action id")
    for a in data["figures"].get("rating_actions", []):
        try:
            _dt.date.fromisoformat(a["date"])
        except ValueError:
            err(f"rating_actions/{a['id']}: invalid date {a['date']}")


# --------------------------------------------------------------------------- 3. recompute
def check_derived(data):
    ys, env = compute_yardsticks(data)
    figs = {f["id"]: f for f in data["figures"]["figures"]}
    n = 0
    for y in data["yardsticks"]["yardsticks"]:
        if y["id"] not in ys:
            continue
        v = ys[y["id"]]
        n += 1
        if y.get("value") is None or rel_diff(v, y["value"]) > TOL:
            err(f"yardsticks/{y['id']}: stored {y.get('value')} vs recomputed {v:.6g} (> 0.5%)")
        pub = y.get("published_in_file20")
        if pub and pub.get("value") is not None and not matches_published(v, pub["value"]):
            err(f"yardsticks/{y['id']}: file 20 publishes {pub['value']} vs recomputed {v:.6g} (> 0.5%)")
        if y.get("date_from_day_of_year"):
            d = day_to_date(v, y["date_from_day_of_year"])
            if y.get("value_date") != d:
                err(f"yardsticks/{y['id']}: value_date {y.get('value_date')} vs recomputed {d}")
        chk = y.get("checks_figure_id")
        if chk and figs.get(chk, {}).get("value") is not None and not matches_published(v, figs[chk]["value"]):
            err(f"yardsticks/{y['id']}: recomputed {v:.6g} vs canonical {chk} = {figs[chk]['value']} (> 0.5%)")
    k = conversion_constants(data)
    for p in data["proposals"]["proposals"]:
        exp = convert_band_all(p, k)
        got = p.get("derived") or {}
        for band, metrics in exp.items():
            for metric, pos in metrics.items():
                for posn, v in pos.items():
                    n += 1
                    sv = got.get(band, {}).get(metric, {}).get(posn)
                    if sv is None or (rel_diff(v, sv) > TOL and abs(v - sv) > 10 ** -ROUNDING[metric]):
                        err(f"proposals/{p['id']}: derived.{band}.{metric}.{posn} stored {sv} vs recomputed {v:.4g}")
        for band in got:
            if band not in exp:
                err(f"proposals/{p['id']}: derived.{band} has no source amount")
        for pv in p.get("published_conversions", []):
            band = convert(abs(pv["eur_bn"]), k)
            n += 1
            metric = pv["metric"]
            if not matches_published(band[metric], abs(pv["value"])):
                err(f"proposals/{p['id']}: file 20 publishes {metric}={pv['value']} for {pv['eur_bn']} bn, recomputed {band[metric]:.4g}")
    for lv in data["levers"]["levers"]:
        c = lever_ceiling(lv, env)
        if c is None:
            continue
        n += 1
        stored = lv["yield_model"].get("max_yield_eur_bn")
        if stored is None or rel_diff(c, stored) > TOL:
            err(f"levers/{lv['id']}: max_yield_eur_bn {stored} vs recomputed {c:.4g}")
        pub = lv["yield_model"].get("published_max_eur_bn")
        if pub is not None and not matches_published(c, pub):
            err(f"levers/{lv['id']}: published ceiling {pub} vs recomputed {c:.4g}")
    for q in data["quiz"]["questions"]:
        if not q.get("formula"):
            continue
        n += 1
        try:
            v = evaluate(q["formula"], env)
        except Exception as e:  # noqa: BLE001
            err(f"quiz/{q['id']}: cannot evaluate formula: {e}")
            continue
        cv = q["correct_value"]
        target = cv.get("value") if cv.get("value") is not None else None
        if target is not None and not matches_published(v, target):
            err(f"quiz/{q['id']}: correct value {target} vs recomputed {v:.4g}")
        for pos, fexpr in (q.get("range_formulas") or {}).items():
            try:
                rv = evaluate(fexpr, env)
            except Exception as e:  # noqa: BLE001
                err(f"quiz/{q['id']}: range formula {pos}: {e}")
                continue
            if cv.get(pos) is None or not matches_published(rv, cv[pos]):
                err(f"quiz/{q['id']}: correct {pos} {cv.get(pos)} vs recomputed {rv:.4g}")
    INFO.append(f"derived values recomputed: {n}")


def convert_band_all(p, k):
    return {name: convert_band(b, k) for name, b in proposal_bands(p).items()}


# --------------------------------------------------------------------------- 4. grep research files
_FILE_CACHE = {}


def research_text(fname):
    if fname not in _FILE_CACHE:
        with open(os.path.join(RESEARCH, fname), encoding="utf-8") as f:
            _FILE_CACHE[fname] = f.read()
    return _FILE_CACHE[fname]


def number_forms(x):
    x = abs(float(x))
    forms = set()
    for d in range(0, 7):
        s = f"{x:.{d}f}"
        if float(s) == x:
            forms.add(s)
            forms.add(f"{x:,.{d}f}")
    return forms


def number_in(x, text):
    for s in number_forms(x):
        if re.search(r"(?<![\d.,])" + re.escape(s) + r"(?![\d]|[.,]\d)", text):
            return True
    return False


def file00_row_line(row):
    for line in research_text("00-reference-figures.md").splitlines():
        if re.match(rf"^\| {row} \|", line) and line.count("|") >= 9:
            return line
    return None


def check_grep(data):
    f20 = research_text("20-pedagogical-approach.md")
    in20 = total = 0
    for f in data["figures"]["figures"]:
        total += 1
        nums = [v for v in ([f["value"]] + ([f["range"]["low"], f["range"]["high"]] if f.get("range") else [])) if v is not None]
        if f["origin"] == "file00":
            hay = file00_row_line(f["file00_row"])
            where = f"file 00 row {f['file00_row']}"
            if hay is None:
                err(f"figures/{f['id']}: file 00 row {f['file00_row']} not found")
                continue
        else:
            hay = research_text(f["source_file"])
            where = f["source_file"]
        if f.get("match_text"):
            if f["match_text"] not in hay:
                err(f"figures/{f['id']}: match_text '{f['match_text']}' not found in {where}")
        else:
            for v in nums:
                if not number_in(v, hay):
                    err(f"figures/{f['id']}: value {v} not found in {where}")
        if f["origin"] == "topic_file" and f["source_file"] != "20-pedagogical-approach.md":
            pass
        if all(number_in(v, f20) for v in nums) or (f.get("match_text") and f["match_text"] in f20):
            in20 += 1
    INFO.append(f"figures found in file 20: {in20} of {total} (informational: file 20 does not quote every canonical row)")

    for a in data["figures"].get("rating_actions", []):
        if a["match_text"] not in research_text(a["research_file"]):
            err(f"rating_actions/{a['id']}: match_text '{a['match_text']}' not found in {a['research_file']}")

    # superseded values (file 00 §4) must not be the current value
    sec = research_text("00-reference-figures.md").split("## 4. Superseded values")[1].split("\n## ")[0]
    figs = {f["id"]: f for f in data["figures"]["figures"]}
    for s in data["figures"].get("superseded", []):
        f = figs.get(s["figure_id"])
        if f is None:
            err(f"superseded: unknown figure id {s['figure_id']}")
            continue
        if not number_in(s["superseded_value"], sec):
            err(f"superseded: {s['superseded_value']} ({s['figure_id']}) not listed in file 00 §4")
        cur = [v for v in ([f["value"]] + ([f["range"]["low"], f["range"]["high"]] if f.get("range") else [])) if v is not None]
        if any(abs(v) == abs(s["superseded_value"]) for v in cur):
            err(f"figures/{f['id']}: uses the superseded value {s['superseded_value']} (file 00 §4: {s['label_en']})")

    def check_amounts(where, amounts, files):
        texts = [research_text(x) for x in files] + [f20]
        for label, v in amounts:
            if v is None:
                continue
            if not any(number_in(v, t) for t in texts):
                warn(f"{where}: {label} = {v} not found in {', '.join(files)} or file 20")

    for p in data["proposals"]["proposals"]:
        files = [x for x in p.get("research_files", [])]
        am = []
        for b in ("claimed", "range"):
            for pos in ("low", "central", "high"):
                if p.get(b) and not p[b].get("computed_by_us") and not (pos == "central" and p[b].get("central_is_midpoint")):
                    am.append((f"{b}.{pos}", (p.get(b) or {}).get(pos)))
        for pt in p.get("claimed_path") or []:
            am.append((f"claimed_path[{pt['year']}]", pt["central"]))
        for e in p.get("estimates", []):
            if e.get("computed_by_us"):
                continue
            for pos in ("low", "central", "high"):
                am.append((f"estimate[{e['author']}].{pos}", e.get(pos)))
        check_amounts(f"proposals/{p['id']}", am, files)
    for lv in data["levers"]["levers"]:
        am = []
        for b in ("yield_static", "yield_behavioral"):
            band = lv.get(b) or {}
            for pos in ("low", "central", "high"):
                if pos == "central" and band.get("central_is_midpoint"):
                    continue
                if band.get("computed_by_us"):
                    continue
                am.append((f"{b}.{pos}", band.get(pos)))
        check_amounts(f"levers/{lv['id']}", am, lv.get("research_files", []))


# --------------------------------------------------------------------------- 5. editorial rules
def check_editorial(data):
    for f in data["figures"]["figures"]:
        blob = json.dumps(f, ensure_ascii=False)
        if "⚠" in blob:
            err(f"figures/{f['id']}: contains an unverified (warning-sign) item")
        if f["status"] not in ("verified", "caveat"):
            err(f"figures/{f['id']}: status must be verified or caveat")
        if f["unit"].strip().startswith("%") and f["base"] not in (
                "pct_gdp", "pct_total_spending", "pct_gni", "pct_population", "pct_of_gap",
                "pct_of_stock", "pct_yield", "pct", "pct_change"):
            err(f"figures/{f['id']}: unit is a % but base is {f['base']}")
        if f["base"] == "pct" and ("GDP" in f["unit"] or "total public expenditure" in f["unit"]):
            err(f"figures/{f['id']}: % of GDP / % of TE must use base pct_gdp / pct_total_spending")
        if f["base"] == "pct_gdp" and "GDP" not in f["unit"]:
            err(f"figures/{f['id']}: base pct_gdp but unit does not say GDP")
        if f["base"] == "pct_total_spending" and "total public expenditure" not in f["unit"]:
            err(f"figures/{f['id']}: base pct_total_spending but unit does not say total public expenditure")
        if f["value"] is None and not f.get("range"):
            err(f"figures/{f['id']}: neither value nor range")
    for p in data["proposals"]["proposals"]:
        if not (p.get("counter_argument_en") or p.get("caveats_en")):
            err(f"proposals/{p['id']}: no counter-argument or caveat")
    for lv in data["levers"]["levers"]:
        if not lv.get("notes_en"):
            err(f"levers/{lv['id']}: no note shown to the user")
    sides = {}
    for lv in data["levers"]["levers"]:
        sides[lv["side"]] = sides.get(lv["side"], 0) + 1
    INFO.append("levers by side: " + ", ".join(f"{k} {v}" for k, v in sorted(sides.items())))
    rv, sp = sides.get("revenue", 0), sides.get("spending", 0)
    if abs(rv - sp) > 6:
        warn(f"levers: revenue ({rv}) and spending ({sp}) menus are unbalanced")
    groups = data["levers"].get("menu_groups", [])
    for g in groups:
        if g.get("mirrors"):
            a = sum(1 for lv in data["levers"]["levers"] if lv.get("menu_group") == g["id"])
            INFO.append(f"menu group {g['id']} ({a} levers) mirrors {g['mirrors']}")
    camps = {}
    for q in data["quiz"]["questions"]:
        camps[q["camp_coding"]] = camps.get(q["camp_coding"], 0) + 1
    INFO.append("quiz items by camp challenged: " + ", ".join(f"{k} {v}" for k, v in sorted(camps.items())))
    if "⚠" in json.dumps(data["proposals"], ensure_ascii=False) or "⚠" in json.dumps(data["levers"], ensure_ascii=False):
        err("proposals/levers: contain an unverified (warning-sign) item")


# --------------------------------------------------------------------------- 6. quiz draw rule
def draw_bounds(n, n_left, n_right, n_neutral):
    k_min = max(0, -(-(n - n_neutral) // 2))
    k_max = min(n_left, n_right, n // 2)
    return k_min, k_max


def reference_draw(questions, n, neutral_codings, rng):
    """Reference implementation of design.draw_rule.procedure (the front end must match it)."""
    left = [q for q in questions if q["camp_coding"] == "left"]
    right = [q for q in questions if q["camp_coding"] == "right"]
    neutral = [q for q in questions if q["camp_coding"] in neutral_codings]
    k_min, k_max = draw_bounds(n, len(left), len(right), len(neutral))
    if k_min > k_max:
        return None
    k = rng.randint(k_min, k_max)
    out = rng.sample(left, k) + rng.sample(right, k) + rng.sample(neutral, n - 2 * k)
    rng.shuffle(out)
    return out


def check_quiz_draw(data):
    import random
    qs = data["quiz"]["questions"]
    rule = data["quiz"].get("design", {}).get("draw_rule")
    if not rule:
        err("quiz: design.draw_rule is missing (symmetry rule must be encoded)")
        return
    neutral_codings = set(rule.get("neutral_codings", []))
    coded = set(rule.get("coded_camps", []))
    if coded != {"left", "right"}:
        err(f"quiz: draw_rule.coded_camps must be ['left', 'right'], got {sorted(coded)}")
    for q in qs:
        if q["camp_coding"] not in neutral_codings | coded:
            err(f"quiz/{q['id']}: camp_coding '{q['camp_coding']}' is neither coded nor neutral in draw_rule")
    n_left = sum(q["camp_coding"] == "left" for q in qs)
    n_right = sum(q["camp_coding"] == "right" for q in qs)
    n_neutral = sum(q["camp_coding"] in neutral_codings for q in qs)
    if n_left != n_right:
        err(f"quiz: bank is unbalanced ({n_left} left-coded vs {n_right} right-coded items)")
    rng = random.Random(20261025)
    for mode, n in rule.get("draw_sizes", {}).items():
        k_min, k_max = draw_bounds(n, n_left, n_right, n_neutral)
        if n > len(qs) or k_min > k_max:
            err(f"quiz: draw of {n} items ({mode}) cannot satisfy the draw rule "
                f"(left {n_left}, right {n_right}, neutral {n_neutral})")
            continue
        for _ in range(500):
            d = reference_draw(qs, n, neutral_codings, rng)
            cl = sum(q["camp_coding"] == "left" for q in d)
            cr = sum(q["camp_coding"] == "right" for q in d)
            if cl != cr or len(d) != n or len({q["id"] for q in d}) != n:
                err(f"quiz: reference draw for {mode} broke the rule (left {cl}, right {cr}, size {len(d)})")
                break
        INFO.append(f"quiz draw rule OK for {mode} ({n} items): left = right = k with k in [{k_min}, {k_max}]")


# --------------------------------------------------------------------------- 8. chapters
CHIP = re.compile(r"\[\[([a-z][a-z-]*):([^\]]*)\]\]")
CALC_ID = re.compile(r"(?<![\w:*])(?:yd:|yard:|fig:)?([a-z][a-z0-9]*(?:_(?:[a-z0-9]+|\*))+)(?![\w*(])")
PLACEHOLDER = re.compile(r"EN ATTENTE DE DONN[ÉE]ES", re.IGNORECASE)


def _strip_comments_and_code(text):
    """Blank out HTML comments and inline code spans, keeping line numbers."""
    def blank(m):
        return re.sub(r"[^\n]", " ", m.group(0))
    text = re.sub(r"<!--.*?-->", blank, text, flags=re.S)
    text = re.sub(r"```.*?```", blank, text, flags=re.S)
    return re.sub(r"`[^`\n]*`", blank, text)


def check_chapters(data):
    if not os.path.isdir(CHAPTERS):
        warn(f"chapters: directory not found: {CHAPTERS}")
        return 0, 0
    figs = {f["id"] for f in data["figures"]["figures"]}
    tables = {t["id"] for t in data["figures"].get("rating_tables", [])}
    ys = {y["id"] for y in data["yardsticks"]["yardsticks"]}
    params = {p["id"] for p in data["yardsticks"].get("parameters", [])}
    props = {p["id"] for p in data["proposals"]["proposals"]}
    srcs = set(data["sources"]["sources"].keys())
    quiz = {q["id"] for q in data["quiz"]["questions"]} | {m["id"] for m in data["quiz"]["misperceptions"]}
    pools = {"fig": figs | tables, "yard": ys | params, "yd": ys | params, "prop": props, "src": srcs, "quiz": quiz}
    calc_pool = figs | ys | params | {f["id"] + s for f in data["figures"]["figures"] if f.get("range")
                                      for s in ("__low", "__high")}
    n_chips = n_err = 0
    for fname in sorted(os.listdir(CHAPTERS)):
        if not fname.endswith(".md"):
            continue
        with open(os.path.join(CHAPTERS, fname), encoding="utf-8") as fh:
            text = _strip_comments_and_code(fh.read())
        for lineno, line in enumerate(text.splitlines(), 1):
            where = f"chapters/{fname}:{lineno}"
            if PLACEHOLDER.search(line):
                err(f"{where}: placeholder 'EN ATTENTE DE DONNÉES' remains")
                n_err += 1
            for m in CHIP.finditer(line):
                kind, ref = m.group(1), m.group(2).strip()
                if kind != "calc":
                    ref = ref.split("|")[0].strip()  # [[fig:id|contexte]]: context-only marker (check 9)
                n_chips += 1
                if kind == "fig-a-creer":
                    err(f"{where}: placeholder [[fig-a-creer:{ref}]] remains"
                        + (f" (id now exists: use [[fig:{ref}]])" if ref in figs else ""))
                    n_err += 1
                elif kind == "calc":
                    unknown = sorted({i for i in CALC_ID.findall(ref) if i not in calc_pool
                                      and not ("*" in i and fnmatch.filter(calc_pool, i))})
                    if unknown:
                        err(f"{where}: [[calc:]] uses unknown id(s) {', '.join(unknown)}")
                        n_err += 1
                elif kind in pools:
                    if ref not in pools[kind]:
                        hint = ""
                        if kind == "fig" and ref in ys | params:
                            hint = " (it is a yardstick: use [[yard:...]])"
                        elif kind in ("yard", "yd") and ref in figs:
                            hint = " (it is a figure: use [[fig:...]])"
                        err(f"{where}: [[{kind}:{ref}]] does not resolve" + hint)
                        n_err += 1
                    elif kind == "yd":
                        warn(f"{where}: non-canonical prefix [[yd:{ref}]], use [[yard:{ref}]]")
                else:
                    err(f"{where}: unknown chip type [[{kind}:{ref}]]")
                    n_err += 1
    INFO.append(f"chapters: {n_chips} chips checked in {CHAPTERS}")
    return n_chips, n_err


# --------------------------------------------------------------------------- 9. chapter lints
# Editorial and numeric lints on the displayed text of the chapters ("> " blockquote lines,
# outside HTML comments, code, YAML front matter and review-notes sections).
# Severity: "error" = a displayed value that does not match its chip, or a [[calc:]] whose stated
# result is wrong (always an error); "strict" = an error with --strict, a warning otherwise;
# "warn" = always a warning. Every message carries a [code] so it can be filtered (--lint-only).
GLOSSARY = os.path.normpath(os.path.join(HERE, "..", "..", "fr", "glossaire-et-conventions.md"))
PEDAGOGY = os.path.normpath(os.path.join(HERE, "..", "..", "fr", "20-approche-pedagogique.md"))
LINT = {"strict": False, "details": False, "only": None, "counts": {}}
WORDS_MIN, WORDS_MAX, WORDS_PER_MIN = 1500, 2200, 240
SENT_MAX, PARA_MAX = 25, 60

SP = "    "
MONTHS = {m: i for i, m in enumerate(("janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août",
                                       "septembre", "octobre", "novembre", "décembre"), 1)}
NUM_TOKEN = re.compile(r"(?<![\w€$£.])([−\-+]?)(\d{1,3}(?:[    ]\d{3}(?!\d))+|\d+)(?:,(\d+))?")
APPROX = re.compile(r"(?:environ|près d[e’']|presque|quelque|de l[’']ordre de|autour de|un peu (?:plus|moins) de|"
                    r"plus d[e’']|moins d[e’']|au moins|au plus|jusqu[’']à|plus|moins)\W*$", re.I)
REF_BEFORE = re.compile(r"(?:\b[Cc]hapitres?|\b[ÉéEe]tapes?|\b[Qq]uestions?|\bn°|\bp\.|§|\b[Pp]ages?|\bpoints? à trancher|"
                        r"\b[Aa]rticle|\bart\.|\b[Ss]ection|\b[Ee]ncadré|\bniveau|\bclasse|\b[Ll]igne|\b[Nn]ote)"
                        r"[   ]*(?:\d+[   ]*(?:,|et|à|ou)[   ]*)*$")
ORD_AFTER = re.compile(r"^(?:er|re|e|ème|eme|ième|nd|nde)\b")
FRACTION_WORDS = {"un tiers": 1 / 3, "deux tiers": 2 / 3, "un quart": 0.25, "trois quarts": 0.75,
                  "la moitié": 0.5, "une moitié": 0.5, "un cinquième": 0.2, "un dixième": 0.1, "deux cinquièmes": 0.4}
NUM_WORDS = {"un": 1, "une": 1, "deux": 2, "trois": 3, "quatre": 4, "cinq": 5, "six": 6, "sept": 7, "huit": 8,
             "neuf": 9, "dix": 10, "onze": 11, "douze": 12, "quinze": 15, "vingt": 20, "trente": 30,
             "quarante": 40, "cinquante": 50, "cent": 100, "mille": 1000, "moitié": 0.5}
DENOM = re.compile(
    r"^(?:\S+\s+){0,6}?(?:du|de\s+la|de\s+l[’']|des|de\s+leurs?|de\s+son|de\s+sa|de\s+ses|d[’']|sur|parmi|en)\s*"
    r"(?:\w+\s+){0,2}?"
    r"(?:PIB|RNB|dépense|dépenses|déficit|personnes|population|prestations|coût du travail|foyers|ménages|revenus?|"
    r"écart|65 ans|recettes|prélèvements|dette|impôts?|emploi|actifs|salariés|habitants|retraités|patrimoines?|"
    r"total|richesse|masse salariale|budget|pensions?|niveau de vie|cotisations|élèves|patients|répondants|"
    r"Français|adultes|interrogés|valeur|montant|écart|hausse|baisse|charge|stock|PO|ressources|enfants|"
    r"jeunes|femmes|hommes|seniors|chômeurs|bénéficiaires|cas|demandes|lits|sociétés|entreprises|frais|"
    r"successions|héritages|fonctionnaires|agents|effectifs|soins|consultations|crédits|financement|"
    r"rendement|taux|intérêts|émissions|droits|retraite|bénéfices?|salaires?|surface|moyenne|médiane|niveau|"
    r"plafond|SMIC|smic|âge|classe|tranche|dixième|centile|décile|quart|tiers|moitié)\b", re.I)
DESCRIPTOR_AFTER = re.compile(r"^(?:les|des)?\s*(?:plus|moins)\s+(?:aisés|aisées|modestes|riches|pauvres|élevés)|"
                              r"^(?:restants|suivants|les plus|du haut|du bas)|^des\s+\d", re.I)
GROWTH_BEFORE = re.compile(r"(?:hausse|baisse|augment\w*|recul\w*|progress\w*|croissance|inflation|taux|rendement|"
                           r"intérêt|\+|−|de plus|de moins|varié|diminu\w*|réduit|réduction|passe[rz]? de|"
                           r"multiplicateur|probabilité|risque|chance)", re.I)
UNIT_LABELS = (("GDP", r"PIB"), ("GNI", r"RNB|revenu national"), ("total public expenditure", r"dépense"),
               ("population", r"population|personnes|habitants"), ("deficit", r"déficit"),
               ("gap", r"écart"), ("labor cost", r"coût du travail"), ("households", r"foyers|ménages"),
               ("income", r"revenu"), ("social protection", r"prestations|protection sociale"),
               ("levies", r"prélèvements"), ("employment", r"emploi"), ("stock", r"stock|dette"),
               ("persons", r"personnes"), ("revenue", r"recettes"), ("average", r"moyen|ensemble"),
               ("15-64", r"15-64|15 à 64"))
RATE_UNITS = ("yield", "change", "interest", "rate", "%)")
BAD_UNIT = re.compile(r"\b(?:Md€|Mds?|Mrds?|bn|G€|M€)(?!\w)")
BAD_ORD = re.compile(r"\b\d+[  ]?(?:ème|eme|ième|nd|nde)\b|\b\d+°(?!C)")
MINUS_RUNNING = re.compile(r"(?:^|[\s(«\[])[−\-][   ]?\d")
INTERNAL = re.compile(r"\bfichier[  ]+\d+|\bnotre base\b|research/|fig-a-creer", re.I)
ESTIMATE_LINE = re.compile(r"^(?:>\s*)?\*\*(?:Interaction\s+«\s*)?(?:Estimez|Devinez)\s+d[’']abord")
ANSWER_LINE = re.compile(r"(?:\b[Rr]éponses?(?:\s+attendues)?|\b[Vv]raie valeur)[   ]*(?:\([^)]*\))?[   ]*:")
ANSWER_COMMENT = re.compile(r"(?:estimez-r[ée]ponse|estimate-answer|r[ée]ponse-ids?)\s*:\s*([^>]*?)\s*-->", re.I)
CONTEXT_COMMENT = re.compile(r"(?:chip-context|contexte)\s*:\s*([^>]*?)\s*-->", re.I)
BOX_SIDE = re.compile(r"box-side\s*:\s*(gauche|droite|les-deux)", re.I)
SYM_GATE = re.compile(r"symmetry-gate\s*:\s*([^|\n>]*)(?:\|([^\n>]*))?", re.I)
NOTES_HEADING = re.compile(r"^#{1,3}\s+(?:Notes|Annexe|Journal|Points? (?:à trancher|ouverts?)|Relecture|Audit|"
                           r"Contrôle|Liste des identifiants|Sources et pastilles)", re.I)


def lint(level, code, where, msg):
    if LINT["only"] and code not in LINT["only"]:
        return
    LINT["counts"][code] = LINT["counts"].get(code, 0) + 1
    text = f"{where}: [{code}] {msg}"
    if level == "error" or (level == "strict" and LINT["strict"]):
        err(text)
    else:
        warn(text)


def fr(x, k):
    """French display of x with k decimals (narrow nbsp thousands are shown as plain spaces)."""
    s = f"{abs(x):,.{max(k, 0)}f}".replace(",", " ").replace(".", ",")
    return ("−" if x < 0 else "") + s


def _norm(s):
    return re.sub(r"[   ]", " ", s).replace("'", "’")


# ----------------------------------------------------------------- reference lists (glossary, plan)
def _section(text, start_pat, end_pat):
    m = re.search(start_pat, text, re.M)
    if not m:
        return ""
    rest = text[m.end():]
    e = re.search(end_pat, rest, re.M)
    return rest[:e.start()] if e else rest


def load_references():
    ref = {"acronyms": set(), "titles": [], "orientation": {}, "banned": [], "chapter_titles": {}}
    spec_acr = ("CICE OFCE OCDE RSA TVA CSG CRDS CDHR SMIC ISF IFI PFU OTAN FMI PISA PLF PLFSS HCFP COR IGF "
                "CEPEJ Ondam SPA ZE21 ZE20 PIB APU Insee Drees Unédic Urssaf Acoss Cades Cnav UE-27").split()
    ref["acronyms"].update(spec_acr)
    try:
        g = open(GLOSSARY, encoding="utf-8").read()
    except OSError:
        warn(f"chapters/lint: glossary not found: {GLOSSARY}")
        g = ""
    if g:
        s1 = _section(g, r"^## 1\. ", r"^## 2\. ")
        sigle_table = False
        for line in s1.splitlines():
            cells = [c.strip() for c in line.split("|")]
            if not line.startswith("|"):
                sigle_table = False
                continue
            if len(cells) > 3 and cells[3] == "Sigle":
                sigle_table = True
                continue
            if sigle_table and len(cells) > 4 and cells[3] not in ("", "–", "-", "---"):
                for tok in re.split(r"[/,;()]| ou ", cells[3]):
                    tok = tok.strip()
                    tok = re.sub(r"\s.*$", "", tok)  # "SEC 2010" -> "SEC", "notification PDE" -> skip below
                    if re.fullmatch(r"[A-Z][A-Za-zÀ-ÿ0-9-]{1,}", tok) and sum(c.isupper() for c in tok) >= 1 \
                            and tok not in ("LFI",) and not tok.islower():
                        ref["acronyms"].add(tok)
        s25 = _section(g, r"^### 2\.5 ", r"^### 2\.6 ")
        for m in re.finditer(r"\*\*Sigles :\*\*(.*)", s25):
            for tok in re.findall(r"\b([A-Z][A-Za-zé]{1,})\b", m.group(1)):
                if tok.isupper() or tok in ("Insee", "Drees", "Unédic", "Urssaf", "Acoss", "Cades", "Cnav", "Ondam"):
                    ref["acronyms"].add(tok)
        s3 = _section(g, r"^## 3\. ", r"^## 4\. ")
        for t in re.findall(r"(?<!\*)\*([^*\n]{6,}?)\*(?!\*)", s3):
            t = t.strip()
            t = re.split(r"\s+[–-]\s+", t)[0].strip()
            if len(t.split()) >= 2 and len(t) >= 10 and t not in ref["titles"]:
                ref["titles"].append(t)
        m = re.search(r"\*\*Étiquettes d’orientation[^:]*:\*\*(.*)", g)
        if m:
            for item in re.split("[\\s\u00a0\u202f]*;[\\s\u00a0\u202f]*", m.group(1)):
                item = item.strip().rstrip(".")
                mm = re.match(r"(.+?)\s*\(([^)]*)\)\s*$", item)
                if mm:
                    name = re.split(r"\s+pour\s+", mm.group(1))[0].strip()
                    ref["orientation"][name] = mm.group(2).strip()
        s44 = _section(g, r"^### 4\.4 ", r"^### 4\.5 ")
        for line in s44.splitlines():
            cells = [c.strip() for c in line.split("|")]
            if len(cells) > 3 and cells[1] and not cells[1].startswith(("Employer", "---")):
                for term in re.split(r",", cells[2]):
                    term = re.sub("[«»“”\"\u202f\u00a0]", " ", term)
                    term = re.sub(r"^\s*les\s+", "", re.sub(r"\s+", " ", term)).strip()
                    term = re.sub(r"\s*\(.*\)$", "", term)
                    if term and len(term) > 3:
                        ref["banned"].append(term)
        ref["banned"].append("suffisance")
    try:
        p = open(PEDAGOGY, encoding="utf-8").read()
        for num, title in re.findall(r"Ch\. (\d+) (.+?)(?: \(|$)", _section(p, r"^### 2\.1 ", r"^### 2\.2 "), re.M):
            ref["chapter_titles"][int(num)] = title.strip()
    except OSError:
        warn(f"chapters/lint: plan not found: {PEDAGOGY}")
    return ref


# ----------------------------------------------------------------- chip values
def _leaves(x, out):
    if isinstance(x, bool) or x is None:
        return out
    if isinstance(x, (int, float)):
        out.append(float(x))
    elif isinstance(x, dict):
        for k, v in x.items():
            if k not in ("year", "number", "eur_bn"):
                _leaves(v, out)
    elif isinstance(x, list):
        for v in x:
            _leaves(v, out)
    return out


class ChipIndex:
    def __init__(self, data):
        self.figs = {f["id"]: f for f in data["figures"]["figures"]}
        self.yards = {y["id"]: y for y in data["yardsticks"]["yardsticks"]}
        self.params = {p["id"]: p for p in data["yardsticks"].get("parameters", [])}
        self.props = {p["id"]: p for p in data["proposals"]["proposals"]}
        self.tables = {t["id"] for t in data["figures"].get("rating_tables", [])}
        ys, env = compute_yardsticks(data)
        self.env = env
        for k, v in ys.items():
            env[k] = v

    def exists(self, i):
        return i in self.figs or i in self.yards or i in self.params

    def info(self, kind, ref):
        """-> dict(values=[(value, which)], unit, rank_of, date, display_decimals, display) or None."""
        if kind == "fig" and ref in self.figs:
            f = self.figs[ref]
            vals = []
            if f["value"] is not None:
                vals.append((f["value"], "value"))
            if f.get("range"):
                vals += [(f["range"][k], k) for k in ("low", "high") if f["range"].get(k) is not None]
            return {"values": vals, "unit": f.get("unit") or "", "rank_of": f.get("rank_of"),
                    "is_rank": (f.get("unit") or "").startswith("rank"), "date": None,
                    "dd": f.get("display_decimals"), "display": f.get("display"), "year_ok": True}
        if kind in ("yard", "yd") and (ref in self.yards or ref in self.params):
            y = self.yards.get(ref) or self.params[ref]
            v = self.env.get(ref, y.get("value"))
            return {"values": [(v, "value")] if v is not None else [], "unit": y.get("unit") or "",
                    "rank_of": None, "is_rank": False, "date": y.get("value_date"),
                    "dd": y.get("display_decimals"), "display": y.get("display"), "year_ok": True}
        if kind == "prop" and ref in self.props:
            p = self.props[ref]
            vals = []
            for key in ("claimed", "range", "estimates", "derived", "published_conversions", "claimed_path"):
                vals += [(v, "prop") for v in _leaves(p.get(key), [])]
            for fid in p.get("context_figure_ids") or []:
                f = self.figs.get(fid)
                if f:
                    vals += [(v, "prop") for v in _leaves([f["value"], f.get("range")], [])]
            return {"values": vals, "unit": "EUR bn", "rank_of": None, "is_rank": False, "date": None,
                    "dd": None, "display": None, "year_ok": False}
        return None


# ----------------------------------------------------------------- [[calc:]] parsing and evaluation
CALC_TOKEN_ID = re.compile(r"(?:yd:|yard:|fig:)?([a-z][a-z0-9]*(?:_(?:[a-z0-9]+|\*))+)")
RESULT_NUM = re.compile(r"^\s*([−\-+]?)\s*(\d{1,3}(?:[   ]\d{3})+|\d+)(?:,(\d+))?\s*(%)?\s*$")


def _split_top(s, sep=";"):
    out, depth, cur = [], 0, ""
    for ch in s:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch == sep and depth == 0:
            out.append(cur)
            cur = ""
        else:
            cur += ch
    out.append(cur)
    return [x.strip() for x in out if x.strip()]


def _parse_results(rhs):
    out = []
    for part in re.split(r"\s+à\s+|\s+;\s+|;", rhs):
        m = RESULT_NUM.match(part)
        if not m:
            return None
        v = float(re.sub(r"\s", "", m.group(2)) + ("." + m.group(3) if m.group(3) else ""))
        if m.group(1) in ("−", "-"):
            v = -v
        out.append((v, len(m.group(3) or ""), bool(m.group(4))))
    return out


def parse_calc(body):
    """-> list of [lhs, results or None]; results = [(value, decimals, is_pct)]."""
    subs = []
    for part in _split_top(body):
        if "=" in part:
            lhs, rhs = part.rsplit("=", 1)
            subs.append([lhs.strip(), _parse_results(rhs) or rhs.strip()])
        else:
            nums = _parse_results(part)
            if nums is not None and subs and isinstance(subs[-1][1], list):
                subs[-1][1].extend(nums)
            else:
                subs.append([part.strip(), None])
    return subs


def eval_calc_lhs(lhs, idx):
    """-> (list of computed values over scenarios, ids found, problem or None)."""
    ids = [m.group(1) for m in CALC_TOKEN_ID.finditer(lhs)]
    expr = CALC_TOKEN_ID.sub(lambda m: "__ID%d__" % ids.index(m.group(1)), lhs)
    expr = re.sub(r"(\d)[   ](?=\d{3}\b)", r"\1", expr)
    expr = re.sub(r"(\d),(\d)", r"\1.\2", expr)
    expr = expr.replace("×", "*").replace("−", "-").replace("÷", "/").replace("–", "-")
    if re.search(r"[A-Za-zÀ-ÿ%]", re.sub(r"__ID\d+__", "", expr)):
        return [], ids, "free text in the formula (cannot evaluate)"
    choices = []
    for i in ids:
        if "*" in i:
            pat = re.compile("^" + re.escape(i).replace(r"\*", "[a-z0-9_]+") + "$")
            ms = sorted(k for k in idx.env if pat.match(k) and idx.env[k] is not None)
            if not ms:
                return [], ids, f"wildcard {i} matches no id"
            choices.append([idx.env[k] for k in ms])
            continue
        f = idx.figs.get(i)
        v = idx.env.get(i)
        alts = []
        if v is not None:
            alts.append(v)
        if f and f.get("range"):
            alts += [f["range"][k] for k in ("low", "high") if f["range"].get(k) is not None]
        if not alts:
            return [], ids, f"{i} has no value"
        choices.append(alts)
    results = []
    n = max([len(c) for c in choices] or [1])
    scenarios = [[c[min(j, len(c) - 1)] for c in choices] for j in range(n)]
    if any(len(c) > 1 for c in choices):  # also each choice independently (wildcards x ranges)
        scenarios += [list(t) for t in itertools.product(*choices)][:64]
    for sc in scenarios:
        env = {f"__ID{k}__": sc[k] for k in range(len(ids))}
        try:
            results.append(evaluate(expr, env))
        except Exception as e:  # noqa: BLE001
            return [], ids, f"cannot evaluate ({e})"
    return results, ids, None


def _rounds_to(c, d, k):
    return abs(abs(c) - abs(d)) <= 0.5 * 10 ** (-k) + 1e-9 * max(1.0, abs(d))


def check_calc(body, idx, where, displayed):
    """Check one [[calc:]] chip; returns (result values, input values) for the number check."""
    if not displayed:
        return [], []
    subs = parse_calc(body)
    all_ids = [m.group(1) for m in CALC_TOKEN_ID.finditer(body)]
    known = [i for i in all_ids if idx.exists(i) or ("*" in i)]
    if not known:
        lint("strict", "calc-no-id", where, f"[[calc:{body}]] contains no recognized data id")
        return [], []
    results, inputs = [], []
    for lhs, res in subs:
        for m in re.finditer(r"(?<![\w_])(\d+(?:,\d+)?)(?![\w_])", lhs):
            inputs.append(float(m.group(1).replace(",", ".")))
        computed, ids, problem = eval_calc_lhs(lhs, idx)
        for i in ids:
            if idx.env.get(i) is not None:
                inputs.append(idx.env[i])
        if res is None:
            if CALC_TOKEN_ID.search(lhs):
                lint("strict", "calc-no-result", where, f"[[calc:{body}]]: sub-formula '{lhs}' has no '= result'")
            continue
        if isinstance(res, str):
            lint("warn", "calc-result", where, f"[[calc:{body}]]: cannot read the stated result '{res}'")
            continue
        results += [r[0] for r in res]
        if problem:
            lint("warn", "calc-eval", where, f"[[calc:{body}]]: {problem}")
            continue
        for v, k, pct in res:
            cands = computed + ([c * 100 for c in computed] if pct or True else [])
            if any(_rounds_to(c, v, k) for c in cands):
                continue
            best = min(cands, key=lambda c: min(abs(abs(c) - abs(v)), abs(abs(c * 100) - abs(v))))
            if any(abs(abs(c) - abs(v)) <= 1.5 * 10 ** (-k) for c in cands):
                lint("warn", "calc-rounding", where,
                     f"[[calc:{lhs} = …]] states {fr(v, k)}, computed {fr(best, k + 2)} (off by one unit in the last place)")
            else:
                lint("error", "calc-value", where,
                     f"[[calc:{lhs} = …]] states {fr(v, k)} but the formula gives {fr(best, max(k, 2))}")
    return results, inputs


# ----------------------------------------------------------------- page model
class Tok:
    __slots__ = ("value", "dec", "text", "start", "end", "kind", "unit", "approx", "month", "sign")


def tokenize_numbers(s):
    toks = []
    for m in NUM_TOKEN.finditer(s):
        t = Tok()
        intpart = re.sub(r"[    ]", "", m.group(2))
        t.dec = len(m.group(3) or "")
        t.value = float(intpart + ("." + m.group(3) if m.group(3) else ""))
        t.sign = m.group(1)
        t.text = m.group(0).lstrip("+−-")
        t.start, t.end = m.start(), m.end()
        before, after = s[max(0, m.start() - 40):m.start()], s[m.end():m.end() + 30]
        if m.start() >= 2 and s[m.start() - 1] in "-–" and s[m.start() - 2].isalpha():
            continue  # UE-27, COVID-19
        if t.sign == "-" and m.start() > 0 and s[m.start() - 1].isdigit():
            continue
        if m.end() < len(s) and s[m.end()] in "_" or re.match(r"^[A-Za-z]{2,}\d", after):
            continue
        t.month = None
        am = re.match(r"^(?:er)?[   ]*([a-zéû]+)", after)
        word = am.group(1) if am else ""
        if word in MONTHS and t.dec == 0 and 1 <= t.value <= 31:
            t.kind, t.month = "date", MONTHS[word]
        elif ORD_AFTER.match(after):
            t.kind = "ordinal"
        elif REF_BEFORE.search(_norm(before)):
            t.kind = "ref"
        elif (t.dec == 0 and re.fullmatch(r"\d{4}", m.group(2)) and 1900 <= t.value <= 2100
              and not re.match(r"^[   ]*(?:€|euros?|milliards?|millions?|%|jours|personnes|foyers)", after)):
            t.kind = "year"
        elif re.match(r"^[   ]*(?:h\b|heures?)", after):
            t.kind = "time"
        elif re.search(r"(?:[Qq]|[Ss]|[Rr]|[Gg])$", before) or re.search(r"[{]$", before):
            continue
        elif t.dec == 0 and 14 <= t.value <= 80 and re.match(r"^[   ]*ans\b", after) \
                and re.search(r"(?:âge|retraite|départ|à|de|ou|et|entre)\W*$", before):
            t.kind = "age"
        else:
            t.kind = "plain"
        um = re.match(r"^[   ]*(%|Md€|M€|€|e\b|[A-Za-zÀ-ÿ]+)", after)
        unit = um.group(1) if um else ""
        unit = {"euro": "€", "euros": "€", "milliard": "Md€", "milliards": "Md€", "Md€": "Md€", "jour": "jours",
                "point": "pts", "points": "pts", "pt": "pts", "pts": "pts"}.get(unit, unit)
        t.unit = unit
        t.approx = bool(APPROX.search(_norm(re.sub(r"\*+", "", before))))
        toks.append(t)
    return toks


def word_match(info, text):
    """Spelled-out numbers and fractions in text (« deux jours », « un tiers », « un euro sur onze »)."""
    low = _norm(text).lower()
    vals = [v for v, _ in info["values"] if v is not None]
    for phrase, fval in FRACTION_WORDS.items():
        if re.search(r"(?<!\w)" + phrase + r"(?!\w)", low):
            for v in vals:
                for c in (v, v / 100):
                    if c and abs(abs(c) - fval) / fval <= 0.08:
                        return phrase
    for wd in re.findall(r"[a-zéè]+", low):
        if wd in NUM_WORDS and NUM_WORDS[wd] >= 2:
            if any(_rounds_to(v, NUM_WORDS[wd], 0) for v in vals):
                return wd
    return None


def fraction_match(info, seg, s):
    """'X … sur Y' displays (« 4 euros sur 10 », « 1 euro sur 11 »): Y or X/Y against the chip."""
    vals = [v for v, _ in info["values"] if v is not None]
    for a, b in zip(seg, seg[1:]):
        gap = s[a.end:b.start]
        if b.value and re.fullmatch(r"[   ]*(?:[a-zéè’']+[   ]+){0,3}sur[   ]*", gap):
            r = a.value / b.value
            for v in vals:
                for c in (v, v / 100):
                    if c and abs(abs(c) - r) / r <= 0.1:
                        return a, b
                if a.value == 1 and _rounds_to(v, b.value, b.dec):
                    return a, b
    return None


def unit_compatible(kind, unit, t):
    """Could displayed token t express a chip of this data unit?  (Used to call a mismatch an error.)"""
    u = (unit or "").lower()
    if kind == "calc" or not u:
        return t.unit not in ("ans", "années", "pays", "fois")
    if u.startswith("rank"):
        return t.kind == "ordinal"
    if "eur bn" in u or kind == "prop":
        return t.unit in ("Md€", "")
    if u.startswith("eur") or "eur per" in u:
        return t.unit in ("€", "")
    if "points" in u or u.startswith("pp"):
        return t.unit in ("pts", "")
    if "%" in u:
        return t.unit == "%"
    if "day" in u:
        return t.unit in ("jours", "") or t.kind == "date"
    if "year" in u:
        return t.unit in ("ans", "années", "")
    return True


def tok_matches(info, t, extra=(), scales=(1, 100, 1000)):
    """Does displayed token t round to one of the chip's values?  Returns the matching 'which' or None."""
    if info is None:
        return None
    if t.kind == "date":
        if info.get("date"):
            mo, da = int(info["date"][5:7]), int(info["date"][8:10])
            if (t.month, int(t.value)) == (mo, da):
                return "date"
        for v, _w in info["values"]:
            if v is not None and 1 <= v <= 366:
                d = _dt.date(2025, 1, 1) + _dt.timedelta(days=int(v))
                if (d.month, d.day) == (t.month, int(t.value)) or \
                        ((d - _dt.timedelta(days=1)).month, (d - _dt.timedelta(days=1)).day) == (t.month, int(t.value)):
                    return "date"
        return None
    cands = []
    for v, w in list(info["values"]) + [(e, "input") for e in extra]:
        if v is None:
            continue
        cands += [(v * k, w + ("" if k == 1 else f"×{k}")) for k in scales]
    d, k = t.value, t.dec
    for c, w in cands:
        if _rounds_to(c, d, k):
            return w
    if k == 0 and d >= 100:
        s = str(int(d))
        tz = len(s) - len(s.rstrip("0"))
        for n in range(1, min(tz, len(s) - 2) + 1):
            for c, w in cands:
                if abs(round(abs(c), -n) - d) < 1e-6:
                    return w
    if t.approx:
        for c, w in cands:
            if c and abs(abs(c) - d) / max(abs(c), d) <= 0.06:
                return w + "≈"
    return None


class Page:
    def __init__(self, path):
        self.path = path
        self.fname = os.path.basename(path)
        m = re.match(r"(\d+)", self.fname)
        self.num = int(m.group(1)) if m else None
        with open(path, encoding="utf-8") as fh:
            self.raw = fh.read()
        self.raw_lines = self.raw.splitlines()
        text = self.raw
        fm = re.match(r"---\n.*?\n---\n", text, re.S)
        self.front = fm.group(0) if fm else ""
        if fm:
            text = re.sub(r"[^\n]", " ", fm.group(0)) + text[fm.end():]
        self.lines = _strip_comments_and_code(text).splitlines()
        self.steps = []  # (start_lineno, heading)
        last_step, notes = 0, []
        for i, line in enumerate(self.lines, 1):
            if line.startswith("## "):
                self.steps.append((i, line))
                if re.match(r"^## [ÉE]tape", line):
                    last_step = i
            if NOTES_HEADING.match(line):
                notes.append(i)
        later = [i for i in notes if i > last_step]
        self.notes_from = later[0] if later else len(self.lines) + 1
        # displayed lines
        self.disp = []
        for i, line in enumerate(self.lines, 1):
            if i >= self.notes_from:
                break
            if re.match(r"^\s*>", line):
                self.disp.append((i, re.sub(r"^\s*>\s?", "", line)))
        self.context_ids = {}
        for i, line in enumerate(self.raw_lines, 1):
            for m in CONTEXT_COMMENT.finditer(line):
                for cid in re.split(r"[\s,]+", m.group(1)):
                    if cid:
                        self.context_ids.setdefault(cid, set()).update({i, i + 1, i + 2})

    def step_of(self, lineno):
        cur = (0, "")
        for s in self.steps:
            if s[0] <= lineno:
                cur = s
        return cur

    def step_range(self, lineno):
        start = self.step_of(lineno)[0]
        nxt = [s[0] for s in self.steps if s[0] > start]
        return start, (nxt[0] - 1 if nxt else len(self.lines))

    def paragraphs(self):
        """Displayed paragraphs: lists of (lineno, text); tables and blank '>' lines split them."""
        paras, cur, last = [], [], None
        for ln, t in self.disp:
            if last is not None and ln != last + 1:
                if cur:
                    paras.append(cur)
                cur = []
            last = ln
            if not t.strip() or t.lstrip().startswith("|"):
                if cur:
                    paras.append(cur)
                cur = []
                continue
            if re.match(r"^\s*(?:[-*•]|\d+\.)\s+", t) and not re.match(r"^\s*\*[^*\s]", t):
                if cur:
                    paras.append(cur)
                cur = []
            cur.append((ln, t))
        if cur:
            paras.append(cur)
        return paras


ABBREV = re.compile(r"(?:\b[A-Z]|\bp|\bn°|\bCh|\bcf|\betc|\bM|\bMme|\bart|\bvol|\béd|\bdir|\bprév|\bQ\d+)$")


def sentences(para):
    """Split a paragraph into sentences: list of (lineno, text)."""
    out = []
    for ln, line in para:
        start = 0
        for m in re.finditer(r"[.!?…](?:\*{1,2}|[   ]?»|\))*(?=[  ]+[A-ZÀ-ÖØ-Þ«*\[(\d])", line):
            pre = line[start:m.start()]
            if line[m.start()] == "." and ABBREV.search(pre):
                continue
            out.append((ln, line[start:m.end()].strip()))
            start = m.end()
        if line[start:].strip():
            out.append((ln, line[start:].strip()))
    return out


def visible(s):
    s = CHIP.sub(" ", s)
    s = re.sub(r"\*\[[^\]]*\]\*", " ", s)  # stage directions *[après la réponse]*
    s = re.sub(r"[*_`#|]", " ", s)
    return s


def word_count(s):
    return len(re.findall(r"[0-9A-Za-zÀ-ÖØ-öø-ÿŒœ]+(?:[’'\-][0-9A-Za-zÀ-ÖØ-öø-ÿŒœ]+)*", visible(s)))


# ----------------------------------------------------------------- the lint pass
def check_chapter_lints(data):
    if not os.path.isdir(CHAPTERS):
        return
    ref = load_references()
    idx = ChipIndex(data)
    pages = [Page(os.path.join(CHAPTERS, f)) for f in sorted(os.listdir(CHAPTERS)) if f.endswith(".md")]
    displays = {}      # (kind:id, which) -> [(page, line, text, dec, approx, unit)]
    by_value = {}      # (number text, unit) -> {(kind:id)}
    estimate = []      # (page, line, answer ids, answer tokens)
    box_tally = {"gauche": 0, "droite": 0, "les-deux": 0}
    labels_used = {}   # body -> {label: [page]}
    words_total = {}
    for pg in pages:
        P = f"chapters/{pg.fname}"
        page_disp = []  # (line, chip key, tok text, value) for same-page collisions
        first_acr, first_body = set(), set()
        long_sent, long_para = [], []
        n_words = 0
        src_only = 0
        prev_ptext = ""
        for para in pg.paragraphs():
            ptext = " ".join(t for _, t in para)
            para_ctx = _norm(visible(prev_ptext[-300:] + " " + ptext))
            prev_ptext = ptext
            per1000 = bool(re.search(r"1[ \u00a0\u202f]000[ \u00a0\u202f]*(?:€|euros)", ptext))
            pw = word_count(ptext)
            n_words += pw
            if pw > PARA_MAX:
                long_para.append((para[0][0], pw))
            for ln, sent in sentences(para):
                W = f"{P}:{ln}"
                sw = word_count(sent)
                if sw > SENT_MAX and not re.match(r"^\*", sent.strip()):
                    long_sent.append((ln, sw))
                vis_sent = CHIP.sub(lambda m: " " * len(m.group(0)), sent)
                chips = list(CHIP.finditer(sent))
                kinds = {c.group(1) for c in chips}
                if kinds and kinds <= {"src", "quiz"}:
                    src_only += 1
                # --- number vs chip
                toks = tokenize_numbers(vis_sent)
                runs, cur = [], []
                for c in chips:
                    if cur and sent[cur[-1].end():c.start()].strip() == "":
                        cur.append(c)
                    else:
                        if cur:
                            runs.append(cur)
                        cur = [c]
                if cur:
                    runs.append(cur)
                prev_end = 0
                for run in runs:
                    seg_start = prev_end
                    for m in re.finditer(r";|[   ]:[   ]", sent[prev_end:run[0].start()]):
                        seg_start = prev_end + m.end()
                    seg = [t for t in toks if seg_start <= t.start < run[0].start()]
                    prev_end = run[-1].end()
                    infos = []
                    for c in run:
                        kind, cref = c.group(1), c.group(2).strip()
                        ctx = cref.split("|")[1].strip().lower() if "|" in cref else ""
                        cref = cref.split("|")[0].strip()
                        is_ctx = ctx.startswith("context") or cref in pg.context_ids and ln in pg.context_ids[cref]
                        if kind == "calc":
                            results, inputs = check_calc(cref, idx, W, True)
                            info = {"values": [(v, "result") for v in results], "unit": "", "rank_of": None,
                                    "is_rank": False, "date": None, "dd": None, "display": None, "year_ok": False}
                            infos.append((c, kind, cref, info, inputs, is_ctx))
                        elif kind in ("fig", "yard", "yd", "prop"):
                            info = idx.info(kind, cref)
                            if info is not None and info["values"]:
                                infos.append((c, kind, cref, info, [], is_ctx))
                    if not infos:
                        continue
                    matched_toks, unmatched = set(), []
                    sent_toks = [t for t in toks if t.start < run[0].start()]
                    scales = (1, 10, 100, 1000) if per1000 else (1, 100, 1000)
                    for c, kind, cref, info, inputs, is_ctx in infos:
                        def usable(tt):
                            out = []
                            for t in tt:
                                if t.kind in ("ref", "time"):
                                    continue
                                if t.kind == "year" and not any(1900 <= (v or 0) <= 2100 for v, _ in info["values"]):
                                    continue
                                if info.get("rank_of") and t.value == info["rank_of"] and \
                                        re.search(r"sur\W*$", vis_sent[:t.start]):
                                    continue
                                out.append(t)
                            return out
                        cands = usable(seg)
                        hit = None
                        for pool in (cands, usable(sent_toks)):  # clause first, then the whole sentence
                            for t in reversed(pool):
                                w = tok_matches(info, t, scales=scales)
                                if w:
                                    hit = (t, w)
                                    break
                            if hit is None:
                                fm = fraction_match(info, pool, vis_sent)
                                if fm:
                                    matched_toks.update({fm[0].start, fm[1].start})
                                    hit = (None, "fraction")
                            if hit is None:
                                wm = word_match(info, vis_sent[seg_start if pool is cands else 0:c.start()])
                                if wm:
                                    hit = (None, "words")
                            if hit:
                                break
                        if hit is None and kind == "calc":
                            for t in reversed(cands):
                                if tok_matches({"values": [(x, "input") for x in inputs]}, t, scales=scales):
                                    hit = (t, "input")
                                    lint("warn", "calc-not-shown", W,
                                         f"[[calc:{cref}]]: the number before the chip ({t.text}) is an input; "
                                         f"the stated result is not displayed")
                                    break
                        if hit:
                            t, w = hit
                            if t is not None:
                                matched_toks.add(t.start)
                                if kind in ("fig", "yard", "yd") and w.rstrip("≈") in (
                                        "value", "low", "high", "value×100", "value×1000", "date"):
                                    key = (f"{kind if kind != 'yd' else 'yard'}:{cref}", w.rstrip("≈"))
                                    displays.setdefault(key, []).append((pg.fname, ln, _norm(t.text), t.dec,
                                                                         t.approx, t.unit, info))
                                    if t.kind not in ("ordinal", "date") and t.value >= 10:
                                        by_value.setdefault((_norm(t.text), t.unit), {}).setdefault(
                                            key[0], []).append(f"{pg.fname}:{ln}")
                                    page_disp.append((ln, key[0], t, info))
                        elif not is_ctx:
                            unmatched.append((c, kind, cref, info, cands))
                    leftover = [t for t in seg if t.start not in matched_toks and t.kind in ("plain", "ordinal", "date")]
                    for c, kind, cref, info, cands in unmatched:
                        vals = ", ".join(fr(v, 2).rstrip("0").rstrip(",") for v, _ in info["values"][:3])
                        label = f"[[{kind}:{cref}]]" if kind != "calc" else f"[[calc:… = {vals}]]"
                        mark = f"[[{kind}:{cref}|contexte]]" + ("" if kind == "calc" else f" or <!-- contexte: {cref} -->")
                        close = []
                        for t in leftover:
                            for v, _w in info["values"]:
                                for k in scales:
                                    cv = abs((v or 0) * k)
                                    if cv and t.kind != "date" and 0.67 <= t.value / cv <= 1.5 and \
                                            unit_compatible(kind, info["unit"], t):
                                        close.append(t)
                            if t.kind == "date" and (info.get("date") or cref.endswith("_day")):
                                close.append(t)
                        if close:
                            t = close[-1]
                            lint("error", "num-chip", W,
                                 f"displayed {t.text}{(' ' + t.unit) if t.unit else ''} does not round to {label} "
                                 f"(value {vals}); fix the number or the chip, or mark it {mark}")
                        elif leftover:
                            lint("warn", "chip-mismatch", W,
                                 f"{label} (value {vals}) matches no number in its clause "
                                 f"({', '.join(t.text for t in leftover)}); check it, or mark it {mark}")
                        else:
                            lint("warn", "chip-no-number", W,
                                 f"{label} (value {vals}): no number displayed for it; if it is context only, "
                                 f"mark it {mark}")
                # --- denominator lint
                sent_denom = False
                for t in toks:
                    if t.unit != "%" or t.kind not in ("plain",):
                        continue
                    after = _norm(visible(vis_sent[t.end:])).strip()
                    after = re.sub(r"^%\s*", "", after)
                    before = _norm(vis_sent[max(0, t.start - 50):t.start])
                    if DENOM.match(after) or DESCRIPTOR_AFTER.match(after):
                        sent_denom = True
                        continue
                    if GROWTH_BEFORE.search(before) or re.search(r"en[  ]+%[  ]+d", para_ctx):
                        continue
                    if sent_denom and re.search(r"\(\s*$", before):
                        continue
                    unit_ok = False
                    for pd in page_disp:
                        if pd[0] == ln and pd[2].start == t.start:
                            u = pd[3]["unit"]
                            if any(r in u for r in RATE_UNITS) and " of " not in u:
                                unit_ok = True
                            for en, frl in UNIT_LABELS:
                                if en in u and re.search(frl, sent + " " + para_ctx, re.I):
                                    unit_ok = True
                    if not unit_ok:
                        lint("warn", "denominator", W, f"'{t.text} %' has no stated denominator "
                                                       f"(du PIB, des dépenses publiques, de la population…)")
                # --- unchipped numbers
                if not chips and not re.search(r"Durée de lecture|Votre estimation", sent):
                    options = sent.count("·") >= 2
                    for t in toks:
                        if t.kind not in ("plain", "ordinal") or options:
                            continue
                        if t.kind == "ordinal" and re.search(r"(?:[Éé]tape|[Cc]hapitre)", vis_sent[:t.start][-20:]):
                            continue
                        if t.dec == 0 and t.value in (1, 10, 100, 1000) and t.unit in ("€", "euros", "") or \
                                t.unit in ("pays", "minutes"):
                            continue  # didactic scales (« sur 100 € »), group sizes (« 27 pays »)
                        hint = ""
                        for c in CHIP.finditer(ptext):
                            inf = idx.info(c.group(1), c.group(2).strip().split("|")[0])
                            if inf and tok_matches(inf, t):
                                hint = f"; its chip [[{c.group(1)}:{c.group(2).strip()}]] is in another sentence " \
                                       f"of the paragraph"
                                break
                        s0, s1 = pg.step_range(ln)
                        for j in range(s0, s1 + 1):
                            if hint:
                                break
                            line = pg.lines[j - 1] if j - 1 < len(pg.lines) else ""
                            if line.lstrip().startswith(">") or not re.search(r"Pastilles|Visuel|Fiche|Interaction", line):
                                continue
                            for c in CHIP.finditer(line):
                                inf = idx.info(c.group(1), c.group(2).strip())
                                if inf and tok_matches(inf, t):
                                    hint = f"; its chip [[{c.group(1)}:{c.group(2).strip()}]] is only in a " \
                                           f"Pastilles/Visuel line ({pg.fname}:{j}): move it into the text"
                                    break
                        lint("warn", "unchipped", W, f"number {t.text}{(' ' + t.unit) if t.unit else ''} has no "
                                                     f"chip in its sentence{hint}")
                # --- typography
                vis_line = re.sub(r"^\s*(?:[-*•]|\d+\.)\s+(?!\*)", "", CHIP.sub(" ", sent))
                if MINUS_RUNNING.search(vis_line):
                    lint("warn", "typo-minus", W, "minus sign before a number in running text "
                                                  "(write « un déficit de 5,1 % », signs only in tables and charts)")
                if BAD_UNIT.search(vis_line):
                    lint("warn", "typo-unit", W, f"'{BAD_UNIT.search(vis_line).group(0)}' in running text "
                                                 f"(write « milliards d’euros »)")
                if BAD_ORD.search(vis_line):
                    lint("warn", "typo-ordinal", W, f"ordinal '{BAD_ORD.search(vis_line).group(0)}' (write 2e, 1er, 1re)")
                if '"' in vis_line:
                    lint("warn", "typo-quotes", W, "straight quotes (use « » or “ ”)")
                if "—" in vis_line:
                    lint("warn", "typo-dash", W, "em dash (glossary §2.1: never)")
                if re.search(r"(?<![\d§.])\d+[  ]?-[  ]?\d+(?![\d,])", re.sub(r"[A-Za-z]+-\d+", "", vis_line)):
                    lint("warn", "typo-range", W, "hyphenated range in running text (write « de 35 à 58 »)")
                masked = vis_line.replace("**", "\x00\x00")
                spans = [(m.start(), m.end()) for m in re.finditer(r"\*[^*]+\*", masked)]
                for title in ref["titles"]:
                    for m in re.finditer(re.escape(title), _norm(vis_line)):
                        if not any(a <= m.start() and m.end() <= b for a, b in spans):
                            lint("warn", "typo-italics", W, f"publication title « {title} » should be in italics")
                            break
                if re.search(r"meilleur contre-argument", sent, re.I) and re.match(r"^\*\*", sent.strip()):
                    if not re.fullmatch(r"\*\*Le meilleur contre-argument\*\*", sent.strip()):
                        lint("warn", "box-title", W, "box title must be exactly **Le meilleur contre-argument** "
                                                     "(no guillemets, no suffix)")
                # --- acronyms
                nv = _norm(vis_line)
                for acr in sorted(ref["acronyms"]):
                    if acr in first_acr:
                        continue
                    m = re.search(r"(?<![\w-])" + re.escape(acr) + r"(?![\w-])", nv)
                    if not m:
                        continue
                    first_acr.add(acr)
                    opens = nv[:m.start()].count("(") - nv[:m.start()].count(")")
                    if opens > 0 or re.match(r"[  ]*\(", nv[m.end():]) or re.search(r"\(\s*$", nv[:m.start()]):
                        continue
                    lint("strict", "acronym", W, f"first occurrence of {acr} on the page is not expanded in "
                                                 f"parentheses in the same sentence")
                # --- orientation labels
                for body, label in ref["orientation"].items():
                    if body in first_body:
                        continue
                    m = re.search(r"(?<![\w-])" + re.escape(body) + r"(?![\w-])", nv)
                    if not m:
                        continue
                    first_body.add(body)
                    used = re.search(re.escape(body) + r"\s*;\s*([^)]*)\)", nv) or \
                        re.search(re.escape(body) + r"[^()]{0,60}?\(([^)]*)\)", nv)
                    lab = used.group(1).strip() if used else ""
                    lab = re.split(r"\s*;\s*", lab)[-1]
                    labels_used.setdefault(body, {}).setdefault(lab, []).append(f"{pg.fname}:{ln}")
                    if _norm(lab) != _norm(label):
                        lint("warn", "orientation", W, f"first mention of {body}: use the glossary label "
                                                       f"« {body} ({label}) »" + (f", not « ({lab}) »" if lab else ""))
                # --- banned words and internal references
                outside = re.sub(r"«[^»]*»|“[^”]*”", " ", vis_line)
                for term in ref["banned"]:
                    if re.search(r"(?<![\w-])" + re.escape(term) + r"(?![\w-])", outside, re.I):
                        lint("warn", "banned-word", W, f"« {term} » (glossary §4.4: avoid outside an attributed quotation)")
                im = INTERNAL.search(sent)
                if im:
                    lint("strict", "internal-ref", W, f"internal reference '{im.group(0)}' in displayed text")
                if re.search(r"Niveau[  ]*:\**[  ]*B[12]", sent):
                    lint("strict", "level-shown", W, "'Niveau : B1' must not be displayed")
        words_total[pg.fname] = n_words
        # --- readability
        if long_sent:
            ex = ", ".join(f"l.{a} ({b})" for a, b in sorted(long_sent, key=lambda x: -x[1])[:6])
            lint("warn", "long-sentence", P, f"{len(long_sent)} displayed sentences over {SENT_MAX} words: {ex}")
            if LINT["details"]:
                for a, b in long_sent:
                    lint("warn", "long-sentence", f"{P}:{a}", f"sentence of {b} words")
        if long_para:
            ex = ", ".join(f"l.{a} ({b})" for a, b in sorted(long_para, key=lambda x: -x[1])[:6])
            lint("warn", "long-paragraph", P, f"{len(long_para)} displayed paragraphs over {PARA_MAX} words: {ex}")
            if LINT["details"]:
                for a, b in long_para:
                    lint("warn", "long-paragraph", f"{P}:{a}", f"paragraph of {b} words")
        INFO.append(f"chapters/{pg.fname}: {n_words} visible words (target {WORDS_MIN}-{WORDS_MAX}); "
                    f"{src_only} displayed sentences backed only by [[src:]]")
        if not WORDS_MIN <= n_words <= WORDS_MAX:
            lint("strict", "word-count", P, f"{n_words} visible words, outside {WORDS_MIN}-{WORDS_MAX}")
        expected = round(n_words / WORDS_PER_MIN)
        found = False
        for i, line in enumerate(pg.lines, 1):
            m = re.search(r"Durée de lecture[  ]*:?\**[  ]*:?[  ]*(?:environ[  ]+)?(\S+)[  ]+min", line)
            if m and i < pg.notes_from:
                found = True
                if not m.group(1).isdigit():
                    lint("warn", "reading-time", f"{P}:{i}", f"reading time placeholder '{m.group(1)}': "
                                                              f"write « environ {expected} minutes » ({n_words} words / 240)")
                elif int(m.group(1)) != expected:
                    lint("warn", "reading-time", f"{P}:{i}", f"reading time says {m.group(1)} minutes; "
                                                              f"{n_words} words / 240 = {expected}")
        fm = re.search(r"duree_lecture:\s*environ\s+(\d+)", pg.front)
        if fm and int(fm.group(1)) != expected:
            lint("warn", "reading-time", f"{P}:front-matter", f"duree_lecture says {fm.group(1)} minutes; "
                                                              f"{n_words} words / 240 = {expected}")
        if not found and not fm:
            lint("warn", "reading-time", P, f"no « Durée de lecture : environ {expected} minutes. » line")
        # --- same page: two ids with the same displayed value
        if "coïncidence" not in pg.raw:
            seen = {}
            for ln, key, t, info in page_disp:
                if t.kind in ("ordinal", "date") or t.value < 10:
                    continue
                for (ln2, key2, t2) in seen.get(t.unit, []):
                    if key2 != key and t2.text != t.text:
                        k = min(t.dec, t2.dec)
                        if _rounds_to(t.value, round(t2.value, k), k) and _rounds_to(t2.value, round(t.value, k), k) \
                                and abs(t.value - t2.value) > 1e-9:
                            lint("warn", "same-value-ids", f"{P}:{ln}",
                                 f"{t.text} {t.unit} ({key}) and {t2.text} {t2.unit} ({key2}, l.{ln2}) look like "
                                 f"the same number; add a « coïncidence » note or align them")
                seen.setdefault(t.unit, []).append((ln, key, t))
        # --- boxes
        disp_idx = {ln: t for ln, t in pg.disp}
        box_lines = [ln for ln, t in pg.disp if re.match(r"^\*\*«?[   ]*Le meilleur contre-argument", t.strip())]
        for bi, b in enumerate(box_lines):
            s0, s1 = pg.step_range(b)
            end = min([x - 1 for x in box_lines[bi + 1:]] + [s1])
            body = [(ln, disp_idx[ln]) for ln in range(b + 1, end + 1) if ln in disp_idx]
            rep = [ln for ln, t in body if re.match(r"^\*\*Ce qu[’']on peut répondre", t.strip())]
            before = [(ln, t) for ln, t in body if not rep or ln < rep[0]]
            W = f"{P}:{b}"
            if not any(re.match(r"^\*\*(?!Ce qu)", t.strip()) for _, t in before):
                lint("warn", "box-thesis", W, "box has no bold thesis line")
            srcl = [t for _, t in before if re.match(r"^\*(?!\*)", t.strip()) and re.search(r"Sources?", t)]
            if not srcl:
                lint("warn", "box-source", W, "box has no italic source line (*Source : …*)")
            elif not any(_norm(lab) in _norm(s) for s in srcl for lab in ref["orientation"].values()):
                lint("warn", "box-source", W, "box source line carries no orientation label from glossary §1.13")
            if not rep:
                lint("warn", "box-reply", W, "box is not followed by « Ce qu’on peut répondre »")
            raw_zone = "\n".join(pg.raw_lines[max(0, s0 - 1):end])
            sides = BOX_SIDE.findall("\n".join(pg.raw_lines[max(0, b - 4):end]))
            if not sides:
                lint("warn", "box-side", W, "no <!-- box-side: gauche | droite | les-deux --> tag for this box")
            else:
                box_tally[sides[0].lower()] += 1
            del raw_zone
        # --- canonical titles
        canon = ref["chapter_titles"]
        h1 = [(i, l) for i, l in enumerate(pg.lines, 1) if l.startswith("# ")]
        if not h1:
            lint("warn", "title", P, "no H1 « # Chapitre N. Titre »")
        else:
            i, l = h1[0]
            m = re.match(r"^# Chapitre (\d+)\. (.+?)\s*$", l)
            if not m:
                lint("warn", "title", f"{P}:{i}", "H1 must read « # Chapitre N. Titre »")
            elif canon.get(int(m.group(1))) and _norm(m.group(2)) != _norm(canon[int(m.group(1))]):
                lint("warn", "title", f"{P}:{i}", f"H1 title « {m.group(2)} » differs from the plan "
                                                  f"(« {canon[int(m.group(1))]} », fr/20-approche-pedagogique.md §2.1)")
        nums = []
        for i, l in pg.steps:
            if i >= pg.notes_from or not re.match(r"^## [ÉE]tape", l):
                continue
            m = re.match(r"^## Étape (\d+)\. \S", l)
            if not m:
                lint("warn", "step-heading", f"{P}:{i}", f"step heading must read « ## Étape N. Titre »: {l[:60]}")
                m = re.match(r"^## [ÉE]tape (\d+)", l)
            if m:
                nums.append(int(m.group(1)))
        if nums and nums != list(range(nums[0], nums[0] + len(nums))):
            lint("warn", "step-heading", P, f"step numbers are not consecutive: {nums}")
        for i, l in enumerate(pg.lines, 1):
            if i >= pg.notes_from or not (l.lstrip().startswith(">") or re.search(r"Bouton|bouton", l)):
                continue
            for m in re.finditer(r"[Cc]hapitre[  ](\d)(?:,[  ]*«|[  ]*:[  ]*|[  ]+«)[   ]*"
                                 r"([^»”\"\n)]+?)[   ]*(?:»|”|\"|\)|$)", l):
                n, t = int(m.group(1)), _norm(m.group(2)).strip(" ,.")
                c = canon.get(n)
                if not t[:1].isupper() or len(t) > len(c or "") + 25:
                    continue  # prose after « chapitre N : », not a title
                if c and not t.startswith(_norm(c)):
                    lint("warn", "chapter-ref", f"{P}:{i}", f"« chapitre {n} » is called « {t} »; canonical title "
                                                           f"is « {c} »")
        # --- estimate-first blocks
        for s_i, (st, head) in enumerate(pg.steps):
            if st >= pg.notes_from:
                break
            s0, s1 = pg.step_range(st)
            ask = None
            if re.search(r"(?:Estimez|Devinez) d[’']abord", head):
                ask = st
            for j in range(s0, s1 + 1):
                if ask is None and ESTIMATE_LINE.match(pg.lines[j - 1].strip()):
                    ask = j
            if ask is None:
                continue
            ids, ans_toks, calc_answer, cut = set(), [], False, None
            for j in range(s0, s1 + 1):
                for m in ANSWER_COMMENT.finditer(pg.raw_lines[j - 1] if j - 1 < len(pg.raw_lines) else ""):
                    ids.update(x for x in re.split(r"[\s,]+", m.group(1)) if x)
                    cut = cut or j
            if not ids:
                for j in range(s0, s1 + 1):
                    line = pg.lines[j - 1]
                    am = ANSWER_LINE.search(line)
                    if not am:
                        continue
                    group = [line]
                    cut = cut or j
                    k = j + 1
                    while line.rstrip().endswith(":") and k <= s1 and re.match(r"^\s+[-*]", pg.lines[k - 1]):
                        group.append(pg.lines[k - 1])
                        k += 1
                    tail = re.split(r"(?<=[.!?])\**\s", line[am.end():], maxsplit=1)[0]
                    head_toks = [t for t in tokenize_numbers(CHIP.sub(" ", tail)) if t.kind in ("plain", "ordinal")]
                    chips_here = [(c.group(1), c.group(2).strip()) for g in group for c in CHIP.finditer(g)]
                    for kind, cref in chips_here:
                        if kind == "calc":
                            calc_answer = True  # the answer is the calc result: checked by displayed value
                            continue
                        inf = idx.info(kind, cref)
                        if inf is None:
                            continue
                        if not head_toks or any(tok_matches(inf, t) for t in head_toks):
                            ids.add(cref)
                    ans_toks += [(_norm(t.text), t.unit) for t in head_toks]
            if not ids and not (calc_answer and ans_toks):
                lint("warn", "estimate-answer", f"{P}:{ask}", "« Estimez d’abord » block declares no answer id "
                                                             "(add <!-- estimez-réponse: id --> or a 'Réponse :' line with its chip)")
                continue
            estimate.append((pg, ask, ids, ans_toks, cut or ask))
        # --- data symmetry gate
        for i, line in enumerate(pg.raw_lines, 1):
            for m in SYM_GATE.finditer(line):
                missing = [x for x in re.split(r"[\s,]+", m.group(1).replace("ids=", "")) if x and not idx.exists(x)]
                if missing:
                    lint("warn", "symmetry-gate", f"{P}:{i}", f"publication gate: {(m.group(2) or '').strip(' -') or 'claim'}"
                                                             f" waits for data id(s) {', '.join(missing)}")
    # --- cross-page checks
    pnum = {pg.num: pg for pg in pages}

    def disp_chips(pg, upto=None):
        out = {}
        for ln, t in pg.disp:
            if upto is not None and ln >= upto:
                break
            for c in CHIP.finditer(t):
                out.setdefault(c.group(2).strip().split("|")[0], ln)
                if c.group(1) == "calc":
                    for m in CALC_TOKEN_ID.finditer(c.group(2)):
                        out.setdefault(m.group(1), ln)
        return out

    seen_answer = {}
    for pg, ask, ids, ans_toks, cut in estimate:
        P = f"chapters/{pg.fname}"
        s0 = cut  # everything displayed before the answer is revealed
        earlier = disp_chips(pg, s0)
        prev = pnum.get((pg.num or 0) - 1)
        prev_chips = disp_chips(prev) if prev else {}
        for i in sorted(ids):
            if i in earlier:
                lint("strict", "estimate-leak", f"{P}:{ask}", f"answer {i} is already shown at line {earlier[i]}, "
                                                             f"before the « Estimez d’abord » question")
            if i in prev_chips:
                lint("strict", "estimate-leak", f"{P}:{ask}", f"answer {i} is shown in the previous chapter "
                                                             f"({prev.fname}:{prev_chips[i]})")
            for other in seen_answer.get(i, []):
                if other != pg.fname:
                    lint("warn", "estimate-repeat", f"{P}:{ask}", f"same « Estimez d’abord » answer ({i}) as {other}")
            seen_answer.setdefault(i, []).append(pg.fname)
        earlier_txt = " ".join(t for ln, t in pg.disp if ln < s0)
        for txt, unit in ans_toks:
            if unit and re.search(r"(?<![\d,])" + re.escape(txt).replace(r"\ ", r"[   ]") +
                                  r"[   ]*" + re.escape(unit if unit != "Md€" else "milliards"),
                                  _norm(CHIP.sub(" ", earlier_txt))):
                lint("strict", "estimate-leak", f"{P}:{ask}", f"answer value {txt} {unit} already displayed earlier "
                                                             f"in the chapter")
    # rounding table
    canonical = {}
    for (key, which), rows in sorted(displays.items()):
        info = rows[0][6]
        exact = {(r[2], r[3]) for r in rows if not r[4]}
        forms = sorted({("environ " if r[4] else "") + r[2] for r in rows})
        if which == "value":
            canonical[key] = forms
        if len({d for _, d in exact}) > 1 or (len(exact) >= 1 and any(r[4] and r[3] < max(d for _, d in exact)
                                                                       for r in rows)):
            locs = "; ".join(f"{('environ ' if r[4] else '') + r[2]} ({r[0]}:{r[1]})" for r in rows)
            lint("warn", "rounding", f"chapters/{key}", f"displayed with different roundings: {locs}")
        dd, display = info.get("dd"), info.get("display")
        if which == "value" and display:
            for r in rows:
                if r[2] != _norm(display) and not r[4]:
                    lint("warn", "rounding", f"chapters/{r[0]}:{r[1]}", f"{key} shown as {r[2]}; canonical "
                                                                         f"display is {display}")
        elif which == "value" and dd is not None and key.startswith("yard:"):
            v = info["values"][0][0]
            want = fr(round(v, dd), dd)
            for r in rows:  # only over-precise displays: coarser rounding in a sentence is a style choice
                if not r[4] and r[3] > max(dd, 0) and _norm(r[2]) != _norm(want):
                    lint("warn", "rounding", f"chapters/{r[0]}:{r[1]}", f"{key} shown as {r[2]}; canonical display "
                                                                         f"(display_decimals {dd}) is {want}")
    for (txt, unit), ids in sorted(by_value.items()):
        if len(ids) > 1:
            if exempt_same_number(txt, unit, ids):
                continue
            locs = "; ".join(f"{k} ({', '.join(v[:2])})" for k, v in sorted(ids.items()))
            lint("warn", "same-number-ids", f"chapters/{txt} {unit}".rstrip(), f"same displayed number chipped with "
                                                                                f"different ids: {locs}")
    if not LINT["only"] or "same-number-ids" in LINT["only"]:
        for i, (key, allowed, e) in enumerate(EXEMPTIONS["same_number_ids"]):
            if i not in EXEMPTIONS["used"]:
                warn(f"lint-exemptions.json: [stale-exemption] same-number-ids {e['number']} {e['unit']} "
                     f"({', '.join(sorted(allowed))}) matches no finding; remove it or update it")
    for body, labs in sorted(labels_used.items()):
        if len(labs) > 1:
            lint("warn", "orientation", f"chapters/{body}", "labelled differently across chapters: " +
                 "; ".join(f"« {k or '(none)'} » ({', '.join(v)})" for k, v in labs.items()))
    n_boxes = sum(box_tally.values())
    INFO.append(f"chapters: « Le meilleur contre-argument » boxes tagged: gauche {box_tally['gauche']}, "
                f"droite {box_tally['droite']}, les-deux {box_tally['les-deux']} ({n_boxes} tagged)")
    if abs(box_tally["gauche"] - box_tally["droite"]) > 2:
        lint("warn", "box-balance", "chapters", f"box sides unbalanced: gauche {box_tally['gauche']} vs "
                                                f"droite {box_tally['droite']}")
    # quiz: explanations vs canonical rounding
    for q in data["quiz"]["questions"]:
        txt = " ".join(str(x or "") for x in (q.get("explanation_fr"), (q.get("correct_value") or {}).get("text_fr")))
        for fid in q.get("figure_ids") or []:
            forms = canonical.get(f"fig:{fid}")
            if not forms or len(forms) != 1 or forms[0].startswith("environ"):
                continue
            info = idx.info("fig", fid)
            for t in tokenize_numbers(txt):
                if t.kind == "plain" and tok_matches(info, t) and _norm(t.text) != forms[0] and not t.approx:
                    lint("warn", "quiz-rounding", f"quiz/{q['id']}", f"{fid} shown as {t.text}; chapters show {forms[0]}")
    INFO.append("chapters lint: " + (", ".join(f"{k} {v}" for k, v in sorted(LINT["counts"].items())) or "no finding")
                + (" (strict)" if LINT["strict"] else ""))


# --------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--write-derived", action="store_true", help="recompute derived values in place before validating")
    ap.add_argument("--data-only", action="store_true", help="skip the chapter checks (8 and 9)")
    ap.add_argument("--chapters", metavar="DIR", help="chapter directory (default: fr/site/chapitres)")
    ap.add_argument("--no-lint", action="store_true", help="skip the chapter lints (9)")
    ap.add_argument("--strict", action="store_true", help="chapter lints marked 'strict' become errors")
    ap.add_argument("--details", action="store_true", help="list every long sentence and paragraph")
    ap.add_argument("--lint-only", metavar="CODES", help="comma-separated lint codes to report (e.g. num-chip,calc-value)")
    args = ap.parse_args()
    global CHAPTERS
    if args.chapters:
        CHAPTERS = os.path.abspath(args.chapters)
    LINT["strict"], LINT["details"] = args.strict, args.details
    LINT["only"] = set(args.lint_only.split(",")) if args.lint_only else None
    data = load_all()
    if args.write_derived:
        write_derived(data)
        data = load_all()
        INFO.append("derived values rewritten (yardsticks.json, proposals.json, simulator-levers.json)")
    check_schemas(data)
    check_references(data)
    check_derived(data)
    check_grep(data)
    check_editorial(data)
    check_quiz_draw(data)
    load_exemptions(data)
    n_data_errors = len(ERRORS)
    if not args.data_only:
        check_chapters(data)
        if not args.no_lint:
            check_chapter_lints(data)
    counts = {
        "figures.json": len(data["figures"]["figures"]),
        "yardsticks.json": len(data["yardsticks"]["yardsticks"]),
        "simulator-levers.json": len(data["levers"]["levers"]),
        "quiz.json": len(data["quiz"]["questions"]),
        "proposals.json": len(data["proposals"]["proposals"]),
        "sources.json": len(data["sources"]["sources"]),
    }
    print("Datasets: " + "; ".join(f"{k} {v}" for k, v in counts.items()))
    for i in INFO:
        print("INFO   " + i)
    for w in WARNINGS:
        print("WARN   " + w)
    for e in ERRORS:
        print("ERROR  " + e)
    n_chapter_errors = len(ERRORS) - n_data_errors
    print(f"Data errors: {n_data_errors}; chapter errors: {n_chapter_errors}"
          + (" (chapter check skipped)" if args.data_only else ""))
    print(f"Result: {'PASS' if not ERRORS else 'FAIL'} ({len(ERRORS)} errors, {len(WARNINGS)} warnings)")
    return 1 if ERRORS else 0


if __name__ == "__main__":
    sys.exit(main())
