# Finances publiques françaises : ordres de grandeur

Base documentaire sourcée, données et contenus pédagogiques pour une plateforme grand public sur les finances publiques françaises, en vue de l'élection présidentielle de 2027.

L'objectif : rendre concrets les ordres de grandeur de la dépense publique, des prélèvements, du déficit et de la dette, et confronter les principales propositions des programmes à ces ordres de grandeur. Chaque chiffre est sourcé, daté et rattaché à une source officielle ou reconnue (Insee, Drees, Cour des comptes, COR, HCFP, Eurostat, OCDE…). Les points de désaccord entre économistes et les meilleurs contre-arguments sont présentés de façon symétrique.

> **Suivi du projet :** demande initiale, décisions, travail fait et reste à faire dans [`STATUS.md`](STATUS.md).

> **Statut (octobre 2026) :** travail en cours. La base documentaire est vérifiée ; les chapitres du site sont des brouillons relus, pas encore publiés. Quelques passages attendent encore des données (voir `fr/LISEZMOI-site.md`).

## Contenu

| Dossier | Contenu | Langue |
|---|---|---|
| [`research/`](research/) | Base documentaire : 18 dossiers thématiques (dépense, protection sociale, retraites, fonction publique et résultats, fiscalité, déficit et dette, chiffrage des propositions, comparaisons internationales, controverses…), chiffres de référence (`00-reference-figures.md`), approche pédagogique (`20-pedagogical-approach.md`), données dérivées (`data/`) et scripts (`scripts/`). Commencer par [`research/README.md`](research/README.md). | anglais |
| [`platform/data/`](platform/data/) | Source unique de vérité du site : chiffres, étalons (« jours de dépense », € par habitant…), leviers du simulateur, quiz, propositions chiffrées, sources ; schémas JSON et script de validation. | JSON |
| [`fr/`](fr/) | Traductions (chiffres de référence, approche pédagogique, index), glossaire et conventions éditoriales, et les 7 chapitres du récit grand public (`fr/site/chapitres/`). Commencer par [`fr/LISEZMOI-site.md`](fr/LISEZMOI-site.md). | français |

## Vérifier les données

```bash
python3 -I platform/data/validate.py           # cohérence des données et des chapitres
python3 -I platform/data/validate.py --strict  # contrôles éditoriaux en plus
```

Les scripts de `research/scripts/` se lancent depuis la racine du dépôt. Les téléchargements bruts (`research/data/raw/`, environ 2 Go) ne sont pas versionnés : ils se régénèrent à partir des sources citées.

## Licences

- **Code** (scripts, `validate.py`) : [MIT](LICENSE).
- **Textes et données produits ici** (`research/`, `platform/data/`, `fr/`) : [CC BY 4.0](LICENSE-CONTENT.md).
- Les données sources restent soumises à la licence de leur producteur (Eurostat, OCDE, Insee… : réutilisation libre avec mention de la source).

## Contribuer

Une erreur, une source plus récente, un contre-argument mal présenté ? Ouvrez une *issue* avec la source primaire (lien et date).
