# Plateforme « finances publiques 2027 » : index des livrables en français et des données

*Index établi le 25 octobre 2026, mis à jour le même jour après la passe transversale (plan de site) et le contrôle final qui l’a suivie. Il n’ajoute aucun chiffre : les seuls nombres ci-dessous sont des décomptes de fichiers, de mots ou d’entrées, ou des identifiants. Les chiffres font foi dans [`../research/00-reference-figures.md`](../research/00-reference-figures.md) (fichier canonique) et dans sa version machine [`../platform/data/figures.json`](../platform/data/figures.json). Les mots font foi dans [`glossaire-et-conventions.md`](glossaire-et-conventions.md).*

Règles éditoriales valables pour tous les fichiers listés : chaque ratio dit son dénominateur (« % du PIB » ou « % des dépenses publiques ») ; fourchette quand les experts divergent ; le meilleur contre-argument sur chaque page ; même traitement pour les promesses d’« argent facile » de gauche et de droite. Les décisions du plan de site (D-ownership, D-rounding, D-titles-and-transitions, D-boxes, D-labels, D-return60, D-data-pass, D-reading-time, D-quiz, D-vocabulary) s’appliquent à tous les chapitres.

---

## 1. Traductions françaises de la base de recherche (`fr/`)

Mots : décompte `wc -w` du fichier entier, 25 octobre 2026 (contrôle final).

| Fichier | Contenu | Mots |
|---|---|---|
| [`LISEZMOI.md`](LISEZMOI.md) | Traduction de [`research/README.md`](../research/README.md) : synthèse, organisation, ordres de grandeur, divergences, débats, éléments non vérifiés, prochaines étapes. | 11 127 |
| [`00-chiffres-de-reference.md`](00-chiffres-de-reference.md) | Traduction du fichier 00 : valeurs canoniques, conventions, journal de réconciliation, valeurs périmées. | 7 824 |
| [`20-approche-pedagogique.md`](20-approche-pedagogique.md) | Traduction du fichier 20, §0 à §4 : principes, architecture du site, étalons, fiches thématiques. | 18 109 |
| [`20-approche-pedagogique-partie2.md`](20-approche-pedagogique-partie2.md) | Traduction du fichier 20, §5 à la fin : simulateur, quiz, garde-fous de crédibilité, accessibilité, maintenance, journal de vérification, sources. | 16 321 |

## 2. Glossaire

| Fichier | Contenu | Mots |
|---|---|---|
| [`glossaire-et-conventions.md`](glossaire-et-conventions.md) | Équivalents français de tous les termes techniques, typographie (espaces insécables, signe moins, format des nombres), titres originaux des sources françaises, ton et niveau de langue (B1, vouvoiement), mentions de certitude, étiquettes d’orientation (§1.13, révisées selon D-labels), règles de l’encadré « Le meilleur contre-argument » (§4.6, dont « Ce qu’on peut répondre » limité à la thèse de l’encadré). Fait foi pour les mots ; fixe notamment le libellé « Estimez d’abord ». | 15 211 |

## 3. Les 7 chapitres du récit (`fr/site/chapitres/`)

Scripts de récit défilant (scrollytelling), statut : **brouillon pour relecture externe**. La passe transversale du plan de site est appliquée aux sept chapitres (chaque chapitre le détaille dans ses notes de relecture). Seuls les blocs de texte affiché sont publics ; le reste est de la spécification. Chaque chiffre porte une pastille source (`[[fig:…]]`, `[[yard:…]]`, `[[prop:…]]`, `[[src:…]]`, `[[quiz:…]]`, `[[calc:…]]` « illustratif ») ; aucun espace réservé ni alias `[[yd:…]]` (contrôle final `validate.py` du 25 octobre 2026 : 1 094 pastilles dans les chapitres, 0 erreur).

Forme commune vérifiée au contrôle final : titre « # Chapitre N. Titre » (titres du fichier 20 §2.1) ; titres d’étape « ## Étape N. Titre » (88 au total) ; ligne affichée « Durée de lecture : environ N minutes. » cohérente avec le décompte (240 mots par minute) ; « Niveau : B1 » jamais affiché ; aucune apostrophe droite dans le texte affiché ; aucun « gisement », « crans » ou « Justice ou suffisance » dans le texte affiché.

**Mots affichés** : décompte « visible words » de `validate.py` au contrôle final (texte affiché au lecteur, hors commentaires HTML, notes, pastilles, didascalies, titres d’étape et spécifications). Cible : 1 500 à 2 200 mots par chapitre ; **les sept chapitres sont dans la cible**. **Fichier** : `wc -w` du fichier entier, notes comprises.

| # | Fichier | En une ligne | Mots affichés | Lecture | Fichier |
|---|---|---|---|---|---|
| 1 | [`01-combien.md`](site/chapitres/01-combien.md) | « Combien ? » : taille de la dépense publique, étalons (jour de dépense, euros par habitant), bloc du déficit 2025 et image du ménage (propriétaire), écart avec la zone euro. | 1 762 | 7 min | 5 796 |
| 2 | [`02-ou-va-l-argent.md`](site/chapitres/02-ou-va-l-argent.md) | « Où va l’argent ? » : calendrier de la dépense, répartition de 1 000 € de dépense publique, retraites et convention de solde, santé, tailles des « économies faciles » en jours. | 2 142 | 9 min | 7 162 |
| 3 | [`03-qui-paie.md`](site/chapitres/03-qui-paie.md) | « Qui paie ? » : prélèvements obligatoires, rang OCDE (propriétaire), « reçu de vos impôts », plus aisés et taxe Zucman, niches fiscales et sociales. | 2 129 | 9 min | 9 220 |
| 4 | [`04-pourquoi-le-deficit.md`](site/chapitres/04-pourquoi-le-deficit.md) | « Pourquoi le déficit ? » : deux récits (dépense ou recettes), baisses d’impôts depuis 2017, année de référence, remède Cour/FMI, déficit par sous-secteur. | 1 918 | 8 min | 9 196 |
| 5 | [`05-dette-et-interets.md`](site/chapitres/05-dette-et-interets.md) | « La dette et ses intérêts » : niveau de la dette, charge d’intérêts, effort de stabilisation, curseurs r et g, notation. | 2 045 | 9 min | 7 717 |
| 6 | [`06-ce-que-l-on-obtient.md`](site/chapitres/06-ce-que-l-on-obtient.md) | « Qu’obtient-on en échange ? » : résultats forts, moyens et faibles (santé, pauvreté, éducation, emploi, justice), pistes d’efficacité présentées comme plafonds ou scénarios. | 1 903 | 8 min | 8 206 |
| 7 | [`07-les-choix.md`](site/chapitres/07-les-choix.md) | « Les choix » : trois objectifs, multiplicateurs, retraites et âge de départ, emploi, rendements des promesses d’« argent facile » de gauche (étape 8) et de droite (étape 9), transition vers le simulateur. | 2 189 | 9 min | 9 919 |

Total : 14 088 mots affichés (environ 59 minutes de lecture pour le parcours complet) ; 57 216 mots en comptant les notes et spécifications.

## 4. Données de la plateforme (`platform/data/`)

Source unique de vérité lisible par machine, construite le 25 octobre 2026 à partir de `research/`. Mode d’emploi : [`../platform/data/README.md`](../platform/data/README.md).

| Fichier | Contenu | Entrées |
|---|---|---|
| [`figures.json`](../platform/data/figures.json) | Chaque ligne canonique du fichier 00 et les données vérifiées des fichiers thématiques ; liste des valeurs périmées. | 321 chiffres |
| [`yardsticks.json`](../platform/data/yardsticks.json) | Étalons du site (jour de dépense, par habitant, ménage, calendrier, objectifs du simulateur), avec formule et valeur recalculée. | 50 étalons |
| [`simulator-levers.json`](../platform/data/simulator-levers.json) | Leviers du simulateur « Équilibrez vous-même le budget » (recettes 13, dépenses 19, structurels 2), classes de multiplicateurs, bascules, règles anti-double compte. | 34 leviers |
| [`quiz.json`](../platform/data/quiz.json) | Erreurs de perception documentées et banque de questions du quiz, avec codage du camp visé. | 41 questions, 14 erreurs de perception |
| [`proposals.json`](../platform/data/proposals.json) | Propositions chiffrées (montant annoncé, estimations indépendantes, fourchette, contre-argument, conversions). | 96 propositions |
| [`sources.json`](../platform/data/sources.json) | Registre des sources citées. | 279 sources |
| [`schemas/`](../platform/data/schemas/) | Un schéma JSON par jeu de données. | 6 schémas |
| [`validate.py`](../platform/data/validate.py) | Contrôles : schémas, identifiants, recalcul des valeurs dérivées (1 102), présence dans les fichiers de recherche, règles éditoriales, règle de tirage du quiz, pastilles, espaces réservés, arrondis, étiquettes, encadrés et fuites de réponses des chapitres. | |
| [`REVIEW.md`](../platform/data/REVIEW.md) | Relecture contradictoire des données (erreurs corrigées, points pour l’équipe éditoriale). | |

**Contrôle final (25 octobre 2026) :** `python3 -I platform/data/validate.py` et `python3 -I platform/data/validate.py --strict` → `Data errors: 0; chapter errors: 0` ; `Result: PASS (0 errors, 0 warnings)` dans les deux modes (contre 146 avertissements et 15 erreurs `--strict` à la passe d’équilibre ; nouvelle vérification après la passe « ids de données créés » du 25 octobre 2026). Les trois avertissements de la passe précédente sont réglés côté données (`display_decimals` à 1 ; deux exemptions dans `lint-exemptions.json`) :

1. `rounding` (chapitre 7, étape 2) : `gap_to_3pct_eur_bn` est affiché avec une décimale, comme l’impose D-rounding (pour éviter la collision avec les baisses d’impôts de 2018 à 2023), mais `yardsticks.json` lui donne `display_decimals` 0. Correction côté données : passer `display_decimals` à 1.
2. `same-number-ids` « 25 Md€ » : haut de la fourchette des promoteurs de la taxe Zucman et haut de l’ensemble « plus aisés » ; deux valeurs exactes et distinctes. À exempter dans le validateur.
3. `same-number-ids` « 47,2 % » : coïncidence entre la part des foyers imposables (chapitre 3) et le coin fiscal de l’OCDE (chapitre 7). À exempter dans le validateur.

Aucune correction de forme n’a été nécessaire dans les chapitres au contrôle final.

## 5. Points résolus, points ouverts et prochaines étapes

### 5.0 Résolus au 25 octobre 2026

1. **Chiffres manquants** : toutes les pastilles `[[fig-a-creer:…]]`, les blocs « EN ATTENTE DE DONNÉES » et l’annexe A du chapitre 3 ont une entrée dans `platform/data` ou ont été réécrits ; les alias `[[yd:…]]` sont devenus `[[yard:…]]`.
2. **Titres** : « Chapitre N. Titre », « Étape N. Titre » et lignes de transition au format D-titles-and-transitions dans les sept chapitres.
3. **Corrections du fichier 20** (§4.10 S9 et S10, S2, Q20, S3, `rn_back_to_62`, S5) : reportées.
4. **Longueur** : les sept chapitres sont dans la cible de 1 500 à 2 200 mots affichés (le chapitre 7 est revenu sous 2 200) ; durées de lecture recalculées sur le décompte final (D-reading-time).
5. **Doublons (D-ownership)** : les blocs répétés (déficit 2025, image du ménage, écart international, intérêts, effort de stabilisation, « économies faciles », ensemble « plus aisés » et taxe Zucman, 980 000 emplois) ont un chapitre propriétaire ; ailleurs, une ligne et un renvoi « (chapitre N) ».
6. **Retraite à 60 ans (D-return60)** : borne basse de `return_60_general_cost_eur_bn` corrigée dans `figures.json` (fourchette Fipeco – Institut Montaigne) et reprise au chapitre 7.
7. **Étiquettes (D-labels)** : glossaire §1.13 révisé ; étiquettes reprises mot pour mot dans les chapitres ; plus d’avertissement `orientation` du validateur.
8. **Encadrés « Le meilleur contre-argument » (D-boxes)** : 14 encadrés, tous avec le titre affiché exact et l’étiquette `box-side` (y compris ceux des chapitres 4 et 5, qui échappaient aux contrôles). Décompte par côté (camp dont la thèse est défendue) :
   - **Gauche : 7** (ch. 1 SPA par habitant ; ch. 2 étape 10 SOCX ; ch. 3 étape 9 milliardaires ; ch. 4 étape 5 année de référence ; ch. 5 étape 12 r < g ; ch. 7 étape 6 âge de départ ; ch. 7 étape 7 heures travaillées).
   - **Droite : 6** (ch. 2 étape 7 « déficit caché » des retraites ; ch. 3 étape 5 niveau des prélèvements ; ch. 4 étape 4 pic de 2017 ; ch. 6 étape 9 argent mal employé ; ch. 7 étape 4 plan crédible ; ch. 7 étape 5 ajustement automatique des retraites).
   - **Les deux : 1** (ch. 7 étape 10). Écart d’un encadré, conforme au plan (seuil d’alerte du validateur : plus de deux).
9. **« Économies faciles » : symétrie rétablie.** Chapitre 2, étape 9 (tailles en jours de dépense) : **5 cibles citées à gauche** (aides aux entreprises, niches fiscales, niches sociales, fraude fiscale, impôt sur la fortune) et **5 citées à droite** (« train de vie de l’État », fraude sociale, contribution à l’UE, aide au développement, AME). Chapitre 7 (rendements) : **étape 8, gauche, 5 puces** (taxe Zucman, test réel CDHR, fraude fiscale, aides aux entreprises, niches fiscales) **et étape 9, droite, 5 puces** (fraude sociale, test réel antifraude, immigration et AME, contribution à l’UE, État et agences), chacune suivie d’un « Au total » et de « Juste, ou suffisant ? ». La liste du chapitre 5 est supprimée. Aucun autre chapitre ne présente de liste de cibles.
10. **Quiz** : banque de 40 questions, camp visé : **gauche 11, droite 11**, les deux 3, anti-impôts 2, pessimisme 2, général 11. Règle de tirage (gauche = droite) vérifiée pour les quatre formats (aperçu, complet, classe, par électorat). Dans les chapitres : Q01, Q02 (générales), M6, M8, M10 (chapitres 2 et 3) ; au chapitre 7, deux « Selon vous » symétriques sur un rendement annuel : taxe Zucman (croyance de gauche) et nouveau plan antifraude (croyance de droite).
11. **Fuites de réponses** : aucune (`estimate-leak`) ; tous les blocs « Estimez d’abord » contrôlés déclarent leur réponse (plus aucun avertissement `estimate-answer`).
12. **Contrôles éditoriaux du validateur** (sigles, dénominateurs, phrases de plus de 25 mots, lignes de source, pastilles `|contexte`, nombres sans pastille, formules) : plus aucun avertissement dans les chapitres.
13. **Validateur et données (forme), ancien point ouvert 1** : `gap_to_3pct_eur_bn.display_decimals` vaut 1 ; exemptions `same-number-ids` « 25 Md€ » et « 47,2 % » appliquées. `validate.py` et `validate.py --strict` : 0 erreur, 0 avertissement.
14. **Retraite à 60 ans, contrôle de reprise** : plus aucune valeur « générale » fondée sur 35 dans les chapitres, `platform/data` et le fichier 20 (anglais et français) ; les seules mentions « 35 à 58 » restantes sont des notes « corrigé, c’était… » et les notes de relecture historiques. 26 à 35 milliards reste la fourchette des versions partielles (type RN). Provenance des conversions de `retirement_60_general_nfp` (`proposals.json`) mise à jour (« file 20 still shows the unsourced 35 » → corrigé).
15. **Nouveaux ids insérés dans les chapitres (ancien point ouvert 4, en partie)** : chapitre 1, étape 11 (réponse sur le dénominateur : 1,4 % par an en volume, HCSP ; +3,0 points de PIB de dépense contre +1,4 point de recettes, Eurostat) ; chapitre 5, étape 6 (durée de vie moyenne de la dette négociable de l’État, 8,4 ans au 30 septembre 2026, AFT) ; chapitre 7, étape 5 (projections du COR, 14,2 % du PIB en 2045, 15,3 % en 2070) et étape 9 (mesure antifraude de 1,5 milliard du budget 2026, HCFP).

### 5.1 Encore ouverts avant publication des chapitres

1. **Validateur et données (forme)** : résolu (voir §5.0, point 13). Nouvelle contrainte : le chapitre 7 est à 2 198 mots affichés (plafond 2 200) ; tout ajout demande une coupe.
2. **Quiz** : résolu le 25 octobre 2026 (Q40, Q38, Q39, Q18, Q25, Q37 corrigées ; étiquette de Rexecode alignée sur le glossaire ; nouvelle question Q41 visant la gauche pour garder l’équilibre). Banque de 41 questions : gauche 11, droite 11, les deux 4.
3. **Fichier 20 et glossaire** : résolu le 25 octobre 2026 (« environ 7 à 9 minutes par chapitre » en anglais et en français ; « réservoir » ajouté au glossaire ; Q36 à Q40 listées au §6.3). Reste à régénérer `research/data/20_pedagogical_conversions.csv`.
4. **Données manquantes (D-data-pass), propriétaire : données** : `judges_per_100k_2022` et `cepej_median_judges_2022` (toujours absents de `figures.json` ; source primaire CEPEJ inaccessible ; graphique justice du chapitre 6 bloqué par la règle de publication) ; `net_investment_2025_pct_gdp` et `ea20_public_gfcf_2025_pct_gdp` (absents ; porte de publication du chapitre 5, étape 6, où l’investissement brut est affiché seul) ; `pension_resources_2025_pct_gdp` et `pension_resources_2070f_pct_gdp` existent mais ne sont pas affichés au chapitre 7 (plafond de mots, décision éditoriale) ; productivité horaire 2019-2025, pyramide des âges, taux d’emploi des 60-64 ans (chapitre 7). Résolus et insérés : maturité moyenne (chapitre 5), dénominateur (chapitre 1), projections du COR et mesure antifraude (chapitre 7), voir §5.0, point 15. Restent aussi : séries de graphique (27 pays, écart avec la ZE21, OCDE par pays, dixièmes Insee) ; champ `year` de `finland_te_2025_pct_gdp` ; note de `cdhr_observed_2025_eur_bn` ; champ `source` de `zucman_critics_eur_bn` à harmoniser (chapitre 7, points ouverts).
5. **Règle de publication (D-data-pass)** : aucun chapitre en ligne tant que la contre-preuve d’un camp est chiffrée et pas celle de l’autre (chapitre 5 étape 6, chapitre 6 étapes 6, 8 et 9). Le chapitre 6, étape 6 (justice), reste qualitatif tant que le point 4 n’est pas réglé.
6. **Notations 2023-2024** (Fitch, S&P, Moody’s) : non vérifiées sur une source primaire ; ne pas les afficher avant vérification. L’affirmation de Moody’s du 23 octobre 2026 reste « caveat » tant que la page de l’AFT n’est pas à jour.
7. **Décisions éditoriales** : vérification juridique de l’étape 10 du chapitre 6 ; message de partage du chapitre 6 généré à partir du score réel ; étiquette de Fipeco (« site indépendant » n’est pas son auto-description) à revoir par le propriétaire du glossaire.
8. **Liens « Pour aller plus loin »** : à poser quand les fiches thématiques auront leurs URL.
9. **Audit de symétrie et relecture contradictoire** (fichier 20 §7.1) : les décomptes ci-dessus sont équilibrés ; il reste la relecture humaine de chaque chapitre (§5.3).

### 5.2 Prototypes (prochaine étape)

- **Calendrier budgétaire** (ruban « à partir de quel jour tout est emprunté ») : convention sur 365 jours, rendu commun aux chapitres 1, 2 et 7.
- **Simulateur** : à partir de `simulator-levers.json` et des classes de multiplicateurs ; bascules (comportements, multiplicateurs, annonces des partis grisées par défaut) ; affichage du solde statique, du solde net après bouclage et de la fourchette (glossaire).
- **Quiz de perception** : à partir de `quiz.json`, interaction « Estimez d’abord », tirage respectant la symétrie gauche = droite.
- **Composants des chapitres** : pastilles source cliquables, encadrés « Le meilleur contre-argument », barres des « économies faciles » à échelle commune (chapitre 7, étape 10). Tester la lisibilité B1 et l’accessibilité sur un premier chapitre avant de généraliser.

### 5.3 Relecture externe

- Relecture par des économistes d’orientations différentes (au moins un proche de chaque lecture du débat « problème de dépense / problème de recettes »), sur les chapitres, les leviers et les fourchettes de `proposals.json`. Publier la liste des relecteurs et leurs désaccords. Priorités : encadrés des deux côtés, listes des étapes 8 et 9 du chapitre 7, multiplicateurs.

### 5.4 Enquête de perception

- Commander l’enquête d’estimation chiffrée prévue au fichier 20 §6.4 : aucun sondage français depuis 2023 ne demande d’estimer un chiffre budgétaire, la prémisse d’« erreur de perception » repose donc sur des indices indirects. Reprendre les questions de `quiz.json` pour mesurer l’écart avant et après lecture.

### 5.5 Calendrier de mise à jour des données (décembre 2026 – juin 2027)

D’après `research/README.md` §9.2 et le fichier 20 §9.1. Chaque publication remplace des chiffres clés : mettre à jour d’abord le fichier 00, puis `figures.json`, puis `validate.py --write-derived`, puis relancer `validate.py --strict` et relire les pastilles concernées dans les chapitres.

| Attendu | Publication | Ce qui change |
|---|---|---|
| Déc. 2026 | Drees, *La protection sociale en France et en Europe* (édition 2026) | Prestations de protection sociale 2025 |
| Déc. 2026 | Insee, COFOG 2025 | Toutes les parts fonctionnelles et le calendrier budgétaire |
| Déc. 2026 | OCDE, *Revenue Statistics 2026* | Taux de prélèvements 2025 et rangs OCDE |
| Déc. 2026 | CEPEJ, cycle 2026 | Indicateurs de justice (débloque le chapitre 6, étape 6) |
| Déc. 2026 | Adoption (ou non) des LFI / LFSS 2027 | Objectifs 2027, crédits AME et APD, mesure antifraude |
| Mars-avr. 2027 | Insee, premiers comptes 2026 ; Eurostat, notification d’avril | Déficit, dette, dépense et PO 2026 |
| Juin 2027 | Rapport annuel du COR ; Cour des comptes, RSPFP | Retraites ; effort de stabilisation de la dette |

### 5.6 Suivi des chiffrages des programmes 2027

- Veille mensuelle des chiffrages indépendants (IPP, OFCE, Institut Montaigne, Fipeco, Cour des comptes, CPO) ; au 25 octobre 2026, aucun programme n’a été chiffré de façon indépendante.
- Ajouter le chiffrage complet promis par LFI pour « début 2027 » et le dossier de presse du RN s’il est mis en ligne ; chaque ajout passe par `proposals.json` avec contre-argument et fourchette, et garde la symétrie des étapes 8 et 9 du chapitre 7.
