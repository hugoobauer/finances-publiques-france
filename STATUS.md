# Suivi du projet

Ce fichier retrace le projet depuis le début : la demande initiale, les décisions prises, ce qui a été fait et ce qu'il reste à faire. Il sert de point d'entrée pour reprendre le travail.

*Dernière mise à jour : 30 octobre 2026.*

---

## 1. La demande

**Contexte.** À l'approche de la présidentielle de 2027, créer une plateforme web pédagogique sur les finances publiques françaises. Constat de départ : beaucoup de propositions (hausses d'impôts, taxe Zucman, gel des prix des carburants ou des loyers, retraite à 60 ans…) promettent de rétablir les comptes ou d'améliorer le pouvoir d'achat sans remettre en question la structure de la dépense publique. Une partie du débat reposerait sur une mauvaise perception des ordres de grandeur, par exemple l'idée que taxer les plus riches suffirait à ramener les comptes à l'équilibre.

**Objectif de la plateforme.** Rendre les ordres de grandeur de la dépense publique concrets et compréhensibles pour le grand public, de façon ludique (comparaisons parlantes, schémas, animations, simulateurs), et confronter les principales propositions des programmes à ces ordres de grandeur.

**Phase 1, collecte des données et des sources (prioritaire) :**
1. décomposition de la dépense publique par grande catégorie, en euros et en % du PIB, sur 20 à 30 ans ;
2. protection sociale en détail (retraites, maladie, famille, chômage, pauvreté, logement), avec comparaison européenne ;
3. fonction publique (effectifs par versant, évolution, comparaison internationale) et indicateurs de qualité des services publics (PISA, accès aux soins, délais…) ;
4. fiscalité : niveau et structure des prélèvements obligatoires, comparaison OCDE ;
5. chiffrage des principales propositions des partis, mis en regard du déficit et de la dette ;
6. tout autre sujet pertinent.

**Phase 2, approche pédagogique :** pour chaque sujet, l'angle, la comparaison ou la métaphore qui rend le chiffre tangible, et le format (graphique, animation, simulateur « équilibrez le budget vous-même »…).

**Exigences :**
- sources officielles ou reconnues uniquement, datées et vérifiables, avec les divergences entre sources ;
- toujours distinguer % du PIB et % de la dépense publique ;
- signaler les désaccords entre économistes et présenter les meilleurs contre-arguments aux thèses du site ;
- situer la France pour chaque indicateur : UE-27, zone euro, OCDE et un panel (Allemagne, Italie, Espagne, Pays-Bas, Belgique, Suède, Danemark) ; moyenne, médiane, rang ; % du PIB et euros par habitant en SPA ; évolution de l'écart sur 20 ans ; un indicateur de résultat quand c'est possible.

Le texte original de la demande figure en annexe.

---

## 2. Décisions prises en cours de route

| Sujet | Décision |
|---|---|
| Langue | La base de recherche (`research/`) est en anglais (règle de l'organisation pour les documents). Les contenus destinés au public (`fr/`) et les fichiers du dépôt sont en français ; les noms de fichiers sont en anglais. |
| Chiffres qui font foi | Pour la recherche, `research/00-reference-figures.md` l'emporte sur les dossiers thématiques. Pour le site, `platform/data/` est la source unique : aucun chiffre n'est affiché sans pastille qui renvoie à une entrée vérifiée. |
| Millésime | Notification d'octobre 2026 à Eurostat (21 octobre 2026) pour le déficit et la dette 2025 ; zone euro à 21 pays (ZE21) comme référence. |
| Chiffres non vérifiés | Signalés « ⚠ unverified » dans la recherche, jamais repris dans `platform/data/` ni sur le site. |
| Symétrie | Même traitement des promesses d'« argent facile » de gauche (taxe Zucman, aides aux entreprises, fraude fiscale…) et de droite (fraude sociale, immigration, contribution à l'UE…). Encadrés « Le meilleur contre-argument » répartis entre les deux camps (7 gauche, 6 droite, 1 les deux) ; quiz équilibré (11 questions visant chaque camp) et règle de tirage qui garde l'équilibre. |
| Étiquettes d'orientation | Une étiquette par organisme, formulée de façon comparable à gauche et à droite (glossaire §1.13). |
| Pas d'étiquette gauche/droite sur les idées | Décision du 31 octobre 2026 : le site n'attribue jamais une idée ou un argument à « la gauche » ou à « la droite ». La symétrie reste une règle de rédaction interne (encadrés, quiz, cartes « Oui, mais… »), invisible pour le lecteur. Les étiquettes d'orientation des organismes cités (glossaire §1.13) restent, sous réserve de confirmation. À appliquer : environ 34 occurrences dans les chapitres 2, 4, 6, 7 et la page « Débats ». |
| Comparaisons internationales | Chaque page compare la France à l'UE et, si possible, au reste du monde (OCDE, autres régions), dès que des données comparables existent. Une seule unité principale par page. |
| Conception du site | Le prototype retraites (31 octobre 2026) sert seulement à valider le format « fait + Oui, mais… ». Une phase de conception dédiée (parcours, architecture, charte graphique, visualisation des données) précède la construction du site avec Astro. |
| Retraite à 60 ans | Retour général : 43 à 58 Md€ par an (Fipeco, Institut Montaigne). L'ancienne borne de 35 Md€ n'avait pas de source ; 26 à 35 Md€ ne vaut que pour les versions partielles. |
| Multiplicateurs | Le simulateur montre l'effet sur la croissance, activé par défaut (environ 0,6 la première année pour un ensemble mixte ; valeurs par instrument dans `research/17-fiscal-multipliers-for-simulator.md`). À désactiver par défaut si l'on préfère afficher d'abord les montants bruts. |
| Durée de lecture | Environ 7 à 9 minutes par chapitre (le parcours complet fait environ 14 000 mots), et non « 12 minutes au total » comme prévu au départ. |
| Dépôt | Public, sur le compte personnel : `hugoobauer/finances-publiques-france`. Licences : MIT pour le code, CC BY 4.0 pour les textes et données. Téléchargements bruts (`research/data/raw/`, environ 2 Go) exclus et régénérables. |

---

## 3. Ce qui a été fait (25 et 26 octobre 2026)

1. **Base documentaire (phase 1).** Dix dossiers thématiques rédigés en parallèle, puis quatre dossiers complémentaires identifiés par une relecture d'exhaustivité (programmes 2027, santé, fonction publique et éducation, perception du public). Chaque dossier a été relu par un vérificateur chargé de réfuter ses chiffres : environ 140 corrections. 22 incohérences entre dossiers ont été réconciliées dans `research/00-reference-figures.md`.
2. **Vérification des points restants.** Les chiffres signalés « non vérifiés » ont été repris un à un sur leurs sources primaires (navigateur utilisé quand les sites bloquaient). Quatre nouveaux dossiers : immigration et finances publiques (15), cibles d'« économies faciles » (16), multiplicateurs pour le simulateur (17), passerelles entre définitions (18).
3. **Approche pédagogique (phase 2).** `research/20-pedagogical-approach.md` : principes, architecture du site, étalons communs (jour de dépense, euros par habitant, part du déficit, « la France comme un ménage »), une fiche par sujet, spécification du simulateur, quiz, garde-fous de crédibilité, accessibilité, calendrier de mise à jour. Mis en cohérence avec les dossiers 15 à 18.
4. **Données de la plateforme.** `platform/data/` : 321 chiffres, 50 étalons, 34 leviers du simulateur, 41 questions de quiz, 96 propositions chiffrées, 279 sources, avec schémas et `validate.py`. Une relecture contradictoire a corrigé 10 erreurs que le validateur ne voyait pas ; le validateur contrôle désormais aussi les chiffres affichés dans les chapitres.
5. **Version française.** Glossaire et conventions, traduction des chiffres de référence, de l'approche pédagogique et de l'index, et rédaction des 7 chapitres du récit grand public (`fr/site/chapitres/`).
6. **Audits des chapitres.** Quatre relectures croisées (économiste de gauche, économiste de droite, contrôle des chiffres, éditeur grand public) : 102 remarques, appliquées en plusieurs passes, avec un plan d'ensemble pour les doublons, les arrondis et l'équilibre des contre-arguments. `validate.py --strict` : 0 erreur, 0 avertissement.
7. **Publication.** Dépôt public créé et poussé : https://github.com/hugoobauer/finances-publiques-france
8. **Confrontation aux sources publiques (30 octobre 2026).** Aucun relecteur sollicité : chaque point contesté des chapitres 1 à 7 et des données (`proposals.json`, `simulator-levers.json`) a été confronté aux positions publiées d'économistes et d'institutions d'orientations différentes (gauche, droite, institutions), à partir de textes ouverts et datés ; les sources et les dates figurent dans les notes de relecture de chaque chapitre. Bilan, d'après les rapports de relecture par chapitre :
   - **Points corrigés** (non soutenus ou partiellement soutenus par une source publiée) : ch. 1 : 9 ; ch. 2 : 10 ; ch. 3 : 11 ; ch. 4 : 8 ; ch. 5 : 12 ; ch. 6 : 10 (3 maintenus avec justification) ; ch. 7 : 8 ; données : 9 points (propositions et leviers).
   - **Contre-arguments publiés ajoutés** : 32 dans les chapitres (ch. 1 : 4 ; ch. 2 : 7 ; ch. 3 : 4 ; ch. 4 : 4 ; ch. 5 : 2 ; ch. 6 : 6 ; ch. 7 : 5) et 9 dans les données.
   - **Critiques** : les critiques de gauche et de droite ont été traitées, presque toutes appliquées en totalité ou en partie ; les refus partiels sont motivés dans les notes de relecture (par exemple, l'absence d'identifiant chiffré pour certaines valeurs).
   - **Validateur** : `validate.py --strict` et `validate.py` affichent 0 erreur, 2 avertissements (étiquette « Cour des comptes », voir §4.1) ; code de sortie 0 dans les deux modes.
   - **Page « Débats »** (`fr/site/debats.md`) : rédigée, couvre les sept chapitres et huit thèmes (103 points).

---

## 4. Ce qu'il reste à faire

### 4.1 Avant de publier les chapitres

- **Justice (chapitre 6, étape 6) :** les juges pour 100 000 habitants (France 11,3 ; médiane du Conseil de l'Europe 17,6 ; 2022) sont ajoutés aux données le 31 octobre 2026, lus sur le tableau de bord public de la CEPEJ. Reste à les intégrer au texte du chapitre et à débloquer le graphique ; la médiane des délais civils n'est pas confirmée.
- **Investissement (chapitre 5, étape 6) :** l'investissement public net et la comparaison avec la zone euro manquent.
- **Notations 2023-2024** (Fitch, S&P, Moody's) : confirmées seulement par la presse ; à vérifier sur les communiqués des agences avant affichage.
- **Chapitre 7 :** à 2 198 mots affichés pour un plafond de 2 200 ; tout ajout demande une coupe.
- **Libellé « Cour des comptes » :** le chapitre 1 (ligne 86) doit employer « Cour des comptes (juridiction financière) » à sa première mention ; les chapitres 2 à 7 écrivent « juridiction financière » seul. Avertissements du validateur, non corrigés dans cette passe.
- **Chiffres manquants (confrontation) :** investissement public net 2025 (ch. 5, étape 6) ; répartition de la charge d'intérêts et PIB potentiel de l'OFCE (ch. 4, critiques G2 et G8) ; écart de recettes avec la ZE21 (ch. 4, G11) ; ligne 2010 du tableau du chapitre 4 (rejetée faute d'identifiant) ; chiffrage de cinq critiques de gauche du chapitre 2 (n° 1, 5, 6, 8, 10), traitées sans identifiant chiffré.
- **Sources non ouvertes :** Banque de France et FMI (accès refusé ; rien n'est cité) ; Institut Montaigne, Rexecode et Observatoire des inégalités non rouverts pour le chapitre 1 ; Observatoire des inégalités non cité au chapitre 4 (pas d'étiquette au glossaire §1.13), de même que la CGT.
- **Divers :** régénérer `research/data/20_pedagogical_conversions.csv` ; séries de données pour les graphiques ; vérification juridique de l'étape 10 du chapitre 6 ; étiquette de Fipeco à revoir ; liens « Pour aller plus loin » à poser quand les fiches thématiques auront leurs URL.

Le détail est dans `fr/LISEZMOI-site.md` §5.1.

### 4.2 Étapes suivantes, par priorité

0. **Conception du site** : étape 1 (parcours et architecture) rédigée dans `fr/conception/01-parcours-et-architecture.md` ; revue des sites existants en cours ; puis charte graphique et maquettes.
1. **Prototypes** du calendrier budgétaire (« à partir du 29 novembre, tout est emprunté »), du simulateur et du quiz, construits sur `platform/data/` ; test auprès de quelques lecteurs non spécialistes.
2. **Relecture par les sources publiques : faite le 30 octobre 2026** (§3, étape 8). Reste à faire :
   - page « Débats » complète (103 points, 8 thèmes, 116 sources), mais trop longue pour une seule page (environ 41 000 mots, 2 h 50 de lecture) : la découper en une page par thème, et vérifier que chaque « Ce que dit le site » reprend bien la formulation corrigée des chapitres ;
   - relire les chapitres touchés une fois ces compléments ajoutés, puis relancer `validate.py --strict`.
3. **Enquête de perception : abandonnée (décision du 31 octobre 2026).** Le projet s'appuie seulement sur les sources publiques existantes (sondages publiés, fichier 14). Conséquence : la prémisse d'une mauvaise perception des ordres de grandeur repose sur des indices indirects, et le site doit le dire au lieu de l'affirmer comme un fait mesuré.
4. **Mises à jour des données :**

   | Attendu | Publication | Ce qui change |
   |---|---|---|
   | Déc. 2026 | Drees, *La protection sociale en France et en Europe* (édition 2026) | Prestations de protection sociale 2025 |
   | Déc. 2026 | Insee, dépenses par fonction (COFOG) 2025 | Parts fonctionnelles, calendrier budgétaire |
   | Déc. 2026 | OCDE, *Revenue Statistics 2026* | Prélèvements 2025 et rangs OCDE |
   | Déc. 2026 | CEPEJ, cycle 2026 | Justice (débloque le chapitre 6) |
   | Déc. 2026 | Adoption (ou non) des lois de finances 2027 | Objectifs 2027, AME, aide au développement |
   | Mars-avr. 2027 | Insee et Eurostat, comptes 2026 | Déficit, dette, dépense, prélèvements 2026 |
   | Juin 2027 | Rapport du COR ; Cour des comptes | Retraites ; effort de stabilisation de la dette |

   Procédure : fichier 00, puis `figures.json`, puis `validate.py --write-derived` et `validate.py --strict`, puis relecture des chapitres concernés.
5. **Veille sur les programmes 2027 :** au 25 octobre 2026, aucun programme n'a de chiffrage indépendant (IPP, OFCE, Institut Montaigne, Fipeco, Cour des comptes). Chiffrage complet de LFI promis pour début 2027 ; dossier de presse du RN pas encore en ligne.

---

## 5. Pour reprendre le travail

1. Ce fichier, puis [`README.md`](README.md) pour l'organisation du dépôt.
2. [`research/00-reference-figures.md`](research/00-reference-figures.md) : les chiffres qui font foi.
3. [`research/20-pedagogical-approach.md`](research/20-pedagogical-approach.md) : le plan éditorial (ou sa traduction dans `fr/`).
4. [`fr/LISEZMOI-site.md`](fr/LISEZMOI-site.md) : l'état détaillé des chapitres et des données.
5. Avant toute modification de chiffre : `python3 -I platform/data/validate.py --strict`.

---

## Annexe : texte original de la demande

> # Contexte
>
> À l'approche de l'élection présidentielle de 2027, je veux créer une plateforme web pédagogique sur les finances publiques françaises.
>
> Mon constat de départ : beaucoup de propositions politiques (hausse d'impôts, taxe Zucman sur les très hauts patrimoines, gel des prix des carburants ou des loyers, retour de la retraite à 60 ans, etc.) promettent de rétablir les comptes ou d'améliorer le pouvoir d'achat sans remettre en question la structure de la dépense publique. Je pense qu'une partie du débat repose sur une mauvaise perception des ordres de grandeur : l'idée, par exemple, que taxer les plus riches suffirait à ramener les comptes de l'État à l'équilibre.
>
> Quelques repères (à vérifier et mettre à jour avec les dernières publications) :
> - Dépenses publiques 2025 : environ 1 714 Md€, soit 57,3 % du PIB (Insee).
> - Prestations de protection sociale 2024 : 31,9 % du PIB, l'un des niveaux les plus élevés d'Europe (Drees).
> - Taux de prélèvements obligatoires 2025 : 43,6 % du PIB (Insee), parmi les plus élevés de l'OCDE.
>
> # Objectif de la plateforme
>
> Rendre les ordres de grandeur de la dépense publique concrets et compréhensibles pour le grand public, de façon ludique (comparaisons parlantes, schémas, animations, simulateurs), et confronter les principales propositions des programmes à ces ordres de grandeur.
>
> # Ce que j'attends de toi, en deux phases
>
> ## Phase 1 : collecte des données et des sources (prioritaire)
> Avant toute réflexion sur le site, constituer une base documentaire solide :
> 1. Décomposition complète de la dépense publique par grande catégorie (protection sociale, santé, éducation, défense, charge de la dette, collectivités, etc.), en euros et en % du PIB, avec l'évolution sur 20-30 ans.
> 2. Focus détaillé sur la protection sociale : retraites, maladie, famille, chômage, pauvreté/exclusion, logement. Montants, évolution, comparaison européenne.
> 3. Fonction publique : effectifs par versant (État, territoriale, hospitalière), évolution dans le temps, comparaison internationale, et indicateurs de qualité des services publics (délais, classements PISA, accès aux soins, etc.) pour mettre en regard moyens et résultats.
> 4. Fiscalité : niveau et structure des prélèvements obligatoires, comparaison OCDE.
> 5. Chiffrage des principales propositions des partis : rendement estimé (taxe Zucman, ISF, etc.) ou coût (retraite à 60 ans, gels de prix), mis en regard du déficit et de la dette.
> 6. Tout autre sujet pertinent que je n'aurais pas cité : la liste ci-dessus indique une direction, elle n'est pas exhaustive.
>
> Pour chaque donnée : la source primaire (Insee, Drees, Cour des comptes, Eurostat, OCDE, Conseil d'orientation des retraites, Institut des politiques publiques, etc.), l'année, le lien, et les éventuelles divergences entre sources.
>
> ## Phase 2 : approche pédagogique
> À partir de ces données, proposer comment présenter chaque sujet sur la plateforme : quel angle, quelle comparaison ou métaphore pour rendre le chiffre tangible, quel format (graphique, animation, simulateur « équilibrez le budget vous-même », etc.).
>
> # Exigences
> - Sources officielles ou reconnues uniquement, datées et vérifiables.
> - Distinguer clairement % du PIB et % de la dépense publique.
> - Signaler les points où les économistes ne sont pas d'accord, et présenter les meilleurs contre-arguments aux thèses du site : une plateforme qui y répond sera bien plus difficile à disqualifier.
> - Pour chaque indicateur, situer la France par rapport aux autres pays :
>   - groupes de comparaison : UE-27, zone euro, OCDE, et un panel de pays comparables (Allemagne, Italie, Espagne, Pays-Bas, Belgique, Suède, Danemark) ;
>   - moyenne, médiane et rang de la France dans chaque groupe ;
>   - en % du PIB et en euros par habitant (PPA) quand c'est pertinent ;
>   - évolution de l'écart sur 20 ans ;
>   - quand c'est possible, mettre en regard un indicateur de résultat (ce qu'on obtient pour ce niveau de dépense).
