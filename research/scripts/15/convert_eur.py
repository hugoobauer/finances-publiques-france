import csv, sys
GDP25 = 1714.1 / 0.573          # EUR bn, implied by file 00 row 1 (TE 1,714.1 bn = 57.3% of GDP)
POP25 = 68.852                   # million, Insee 2025 provisional (page 3633212)
GDP27, GDP32 = 3135.0, 3582.0    # file 11 R1 (2032 = file 11's own assumption)
rows = [
 ("OECD A: individual items only (FB)", 1.020), ("OECD B: + congestible public goods per capita (FB)", 0.253),
 ("OECD: + pure public goods except defence and debt (FB)", -0.299), ("OECD: + pure public goods except debt (FB)", -0.530),
 ("OECD C2: all public goods per capita (FB)", -0.846), ("OECD C2: native-born", -3.252),
 ("OECD Table 4.2 A: FB + native-born children", 0.459), ("OECD Table 4.2 B: FB + children", -0.308), ("OECD Table 4.2 C2: FB + children", -1.406),
 ("OECD Table 4.6: closing the employment gap (prime-aged)", 0.223),
 ("CEPII 2018 lower bound", -0.5), ("CEPII 2018 upper bound", 0.05),
]
out = []
for lab, pct in rows:
    out.append([lab, pct, round(pct / 100 * GDP25, 1)])
pc = GDP25 * 1000 / POP25
for lab, pct in (("FB per capita, C2 (% of GDP pc)", -6.535), ("NB per capita, C2", -3.735), ("Gap FB - NB per capita, C2", -2.800)):
    out.append([lab + " -> EUR per person", pct, round(pct / 100 * pc)])
out += [["GDP 2025 (EUR bn)", "", round(GDP25, 1)], ["GDP per capita 2025 (EUR)", "", round(pc)],
        ["RN immigration 2027 15.1 bn, % of 2027 GDP", "", round(15.1 / GDP27 * 100, 2)], ["RN immigration 2031 29.0 bn, % of 2032 GDP", "", round(29.0 / GDP32 * 100, 2)],
        ["RN reserved benefits 18.1 bn (2031), % of 2032 GDP", "", round(18.1 / GDP32 * 100, 2)], ["RN 2026 immigration 11.9 bn, % of 2025 GDP", "", round(11.91 / GDP25 * 100, 2)],
        ["AME->AMU 1.3 bn / PLF 2027 AME credits 1.2083 bn (%)", "", round(1.3 / 1.2083 * 100)], ["AME->AMU 1.3 bn / AME spending 2025 1.340 bn (%)", "", round(1.3 / 1.340 * 100)],
        ["AME spending 2025 % of GDP 2025", "", round(1.340 / GDP25 * 100, 3)], ["AME spending 2025 % of TE 2025", "", round(1.340 / 1714.1 * 100, 3)],
        ["Cour 2019 DPT 6.57 bn as % of 2019-scope (reported 1.41% of general budget gross spending)", "", ""]]
w = csv.writer(open(sys.argv[1], "w", newline="")); w.writerow(["item", "pct_of_GDP", "EUR_bn_or_value"]); w.writerows(out)
for r in out: print(r)
