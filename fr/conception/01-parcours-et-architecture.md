# Conception du site, étape 1 : parcours et architecture

*Document de travail, 31 octobre 2026. Il reprend l'architecture prévue au fichier 20 (§2) et la révise à la lumière du prototype « retraites » et des décisions du 31 octobre 2026 (voir `STATUS.md`, §2). Il précède toute maquette graphique.*

## 1. Ce que le site doit faire

**Une phrase.** Donner à chacun les ordres de grandeur pour juger seul une promesse budgétaire : combien elle rapporte ou coûte, face à quoi, et comment la France se situe par rapport aux autres pays.

**Ce que le lecteur doit retenir après cinq minutes :**

1. La dépense publique est d'environ 1 700 Md€ par an ; près des deux tiers vont à la protection sociale et à la santé.
2. Le déficit (environ 150 Md€ en 2025) est beaucoup plus grand que la plupart des recettes ou économies « faciles » proposées, quel que soit le camp qui les propose.
3. La France est l'un des pays qui protègent le plus, et elle le resterait même après la plupart des réformes discutées. Le choix porte sur le niveau de protection et sur la façon de le financer : c'est un choix politique, que le site ne fait pas à la place du lecteur.

## 2. Règles de conception (issues des décisions du 31 octobre 2026)

| Règle | Conséquence pour l'interface |
|---|---|
| **Aucune idée n'est étiquetée « de gauche » ou « de droite »** | Pas de badge de camp sur les cartes « Oui, mais… », ni dans les chapitres. L'équilibre entre camps reste une règle de rédaction interne, vérifiée par `validate.py`. Les organismes cités gardent leur étiquette d'orientation (glossaire §1.13), sous réserve de confirmation. |
| **Une seule unité principale par page** | Chaque type de page a son unité (§5). Les autres conversions restent accessibles dans la pastille, pas dans le texte. |
| **« Et ailleurs ? » partout où les données existent** | Chaque page de sujet et chaque page de réponse se termine par une comparaison France / UE-27 / panel (Allemagne, Italie, Espagne, Pays-Bas, Belgique, Suède, Danemark) et, si possible, OCDE et reste du monde. |
| **Montrer le rang après la mesure** | Voir §6 : « Même après cette mesure, la France resterait Xe de l'UE. » Le même outil s'applique aux dépenses et aux impôts. |
| **Un fait, pas un verdict, en tête de page** | « Les retraites sont le premier poste de la dépense » plutôt que « les retraites coûtent trop cher ». |

## 3. Les lecteurs et leurs parcours

Les cinq profils du fichier 20 (§2.2) restent valables. Le prototype montre que deux parcours portent l'essentiel du trafic attendu ; ils doivent être conçus en premier.

### 3.1 Parcours A : « J'ai entendu une promesse » (prioritaire)

*Qui :* un électeur qui a entendu « il suffit de taxer les riches » ou « il suffit de lutter contre la fraude », souvent sur téléphone, depuis un réseau social ou une recherche.

1. Il arrive sur une **page de réponse** (lien direct, partagé ou trouvé par recherche).
2. Il lit, dans l'ordre : ce qui est vrai, combien cela représente (une seule unité, une barre), les limites, qui dit quoi, « Et ailleurs ? ».
3. Il remonte vers la **page de sujet** (« Retraites ») pour voir les autres réponses fréquentes.
4. Il ouvre le **simulateur** avec la mesure déjà activée (« Ajouter à mon budget »).

*Réussite :* il ouvre une deuxième réponse ou le simulateur. Temps : 3 à 6 minutes.

### 3.2 Parcours B : « Je veux comprendre » (prioritaire)

*Qui :* un citoyen curieux, un enseignant, un élève.

1. Accueil → quiz d'accroche (trois questions, estimation d'abord).
2. Calendrier de la dépense (« à partir du 29 novembre, tout est emprunté »).
3. Une **page de sujet** choisie dans le calendrier (retraites, santé, école…).
4. Le récit en sept chapitres, pour qui veut aller plus loin.

*Réussite :* il termine le quiz et ouvre au moins une page de sujet. Temps : 5 à 15 minutes.

### 3.3 Parcours secondaires

- **Campagne 2027 :** recherche « chiffrage programme X » → carte du programme → pages de réponse des mesures → simulateur.
- **Journaliste :** fiche chiffre → source → téléchargement CSV.
- **Sceptique :** « Qui sommes-nous ? » → méthode → « Débats » → journal des corrections.

## 4. Architecture révisée

Changements par rapport au fichier 20 (§2.1) : les **pages de sujet** et les **pages de réponse** deviennent le cœur du site ; la page « Débats » disparaît comme page unique et alimente les pages de réponse ; le « vérificateur de promesses » est absorbé par les pages de réponse et le simulateur.

```
Accueil : quiz d'accroche (3 questions) + calendrier de la dépense + accès aux sujets
│
├── SUJETS (une page par grand poste ou grande question ; environ 10 à la première version)
│   │   Retraites · Santé · École · Chômage et minima sociaux · Fonction publique
│   │   Impôts et cotisations · Déficit et dette · Intérêts · Aides aux entreprises · Immigration
│   │
│   └── Chaque sujet : le fait principal → le calendrier ou la barre de taille
│       → « Oui, mais… » (4 à 8 cartes) → « Et ailleurs ? » → chapitre lié
│
├── RÉPONSES (une page par objection fréquente ; environ 40 à 60 à terme)
│       Ce qui est vrai → Combien → Les limites → Qui dit quoi → Et ailleurs ?
│       → Ajouter à mon budget
│       Une réponse peut être reliée à plusieurs sujets (« taxer les plus riches »
│       répond aux retraites, au déficit, à la dette).
│
├── LE RÉCIT (7 chapitres, inchangés ; ils renvoient aux sujets et aux réponses)
│
├── OUTILS
│   ├── Simulateur « Équilibrez vous-même le budget »
│   ├── Quiz complet
│   └── Comparateur de pays
│
├── PROGRAMMES 2027 (une carte par candidat ; chaque mesure renvoie à sa page de réponse)
│
└── CONFIANCE
    ├── Méthode et unités
    ├── Sources et données (CSV)
    ├── Débats : index des points contestés (renvoie vers les pages de réponse)
    └── Charte, financement, journal des corrections
```

**Ce que devient la page « Débats ».** Ses 103 points se répartissent ainsi : les points sur une promesse ou une objection deviennent le bloc « Qui dit quoi » d'une page de réponse ; les points de méthode (périmètres, années de référence, conventions) vont dans « Méthode » ; la page « Débats » devient un index court. Cela règle aussi sa longueur (41 000 mots).

## 5. Les types de page et leur unité principale

| Type de page | Question du lecteur | Unité principale | Autres unités (dans la pastille) |
|---|---|---|---|
| Accueil, calendrier | « Où va l'argent ? » | Jours du calendrier (sur 365) | Md€, % de la dépense |
| Page de sujet | « Combien pèse ce poste ? » | Part de la dépense publique (« un euro sur quatre ») | Md€, % du PIB, jours |
| Page de réponse | « Est-ce que cela suffirait ? » | Part du déficit à combler | Md€, jours, € par habitant |
| Comparaison « Et ailleurs ? » | « Est-ce beaucoup ? » | % du PIB et rang dans l'UE | € par habitant en SPA |
| Simulateur | « Puis-je équilibrer ? » | Md€ et déficit en % du PIB | Jours |

Point à trancher : le % du PIB est l'unité des comparaisons internationales, mais il est mal compris (voir fichier 14). Proposition : toujours l'accompagner d'une phrase-repère (« le PIB, c'est la richesse produite en un an en France »).

## 6. Composant « Et ailleurs ? » et rang après la mesure

**But.** Répondre à « est-ce beaucoup ? » sans adjectif, et montrer qu'une réforme modeste ne change souvent pas la position de la France.

**Contenu :**

1. Une barre horizontale par pays (France en évidence, UE-27, panel ; OCDE si disponible).
2. Le rang de la France aujourd'hui.
3. Sur une page de réponse, un second repère : **la position de la France si la mesure était appliquée.**
   - Exemple de dépense : la France consacre 1,76 % du PIB à l'indemnisation du chômage (UE : 1,08 %, 1re sur 27, Eurostat Sespros 2024). Une baisse de 10 % la laisserait vers 1,6 %, toujours très au-dessus de la moyenne. Le rang exact sera calculé à partir des données Eurostat.
   - Exemple d'impôt : avec la taxe sur les plus fortunés, les prélèvements obligatoires passeraient de 43,6 % à environ 44 % du PIB (10 à 25 Md€ de plus). Le rang dans l'OCDE sera calculé de la même façon, avec la mesure de l'OCDE (fichier 18).
4. Une phrase neutre : « Même après cette mesure, la France resterait Xe sur 27. » Pas de commentaire sur ce que cela signifie.

**Symétrie.** Le composant s'applique de la même façon aux baisses de dépenses et aux hausses d'impôts. Il montre dans les deux cas que la France reste à un niveau élevé, de dépense comme de prélèvements.

**Données à préparer.** Séries Eurostat et OCDE par poste (fichier 09 en a la plupart) ; pour le reste du monde, OIT (*World Social Protection Report*) et base de l'OCDE sur les prestations (durée et taux de remplacement). Chaque série passe par `figures.json` et `validate.py`, comme les autres chiffres.

## 7. Page de sujet et page de réponse : structure détaillée

### 7.1 Page de sujet

1. **Le fait** (titre) et trois chiffres : montant, part de la dépense, comparaison UE en une ligne.
2. **La taille** : calendrier ou barre (une seule image).
3. **« Oui, mais… »** : 4 à 8 cartes, chacune avec la phrase entendue, une ligne de réponse et une mini-barre (part du déficit). Pas d'étiquette de camp ; l'ordre des cartes est tiré au sort à chaque visite, pour ne favoriser aucun camp par la position.
4. **« Et ailleurs ? »**.
5. **Pour aller plus loin** : chapitre lié, sources.

### 7.2 Page de réponse

1. **La phrase entendue**, entre guillemets, sans attribution.
2. **Ce qui est vrai** : toujours en premier, et toujours non vide.
3. **Combien** : un chiffre, une barre, l'unité de la page ; fourchette si les estimations divergent (barre de fourchette du fichier 20, §2.3).
4. **Les limites**.
5. **Qui dit quoi** : auteurs nommés, étiquette d'organisme, montant, lien.
6. **Et ailleurs ?** avec le rang après la mesure.
7. **Ajouter à mon budget** : ouvre le simulateur avec la mesure activée.

## 8. Décisions prises le 31 octobre 2026 (déléguées par le porteur du projet)

1. **Étiquettes des organismes cités : conservées** (« Terra Nova, centre gauche », « Fondation iFRAP, libérale », glossaire §1.13). Elles disent *qui parle*, pas à quel camp appartient une idée ; elles permettent au lecteur de juger un chiffre quand son auteur a un intérêt. Les idées et les objections, elles, ne portent jamais d'étiquette.
2. **Ordre des cartes « Oui, mais… » : par montant, du plus grand au plus petit**, et la règle est écrite sur la page (« classées par montant »). Un ordre fixé par une règle mesurable est vérifiable et ne dépend d'aucun choix éditorial ; le tirage au sort aurait gêné la comparaison. Les cartes sans montant (« le système est presque à l'équilibre ») viennent après, par ordre alphabétique. `validate.py` vérifiera l'ordre.
3. **Déficit de référence des pages de réponse : le dernier déficit constaté**, notifié à Eurostat (aujourd'hui 2025 : 151,6 Md€). Il est mis à jour à chaque notification (avril et octobre). Les prévisions (2026, 2027) restent dans le simulateur, où leurs hypothèses sont affichées. Raison : un chiffre constaté se vérifie ; une prévision dépend d'hypothèses discutées.

## 9. Points ouverts pour l'étape suivante

1. **Liste des 10 sujets** et des objections par sujet : à établir à partir des fichiers 07, 08, 16 et de la page « Débats ».
2. **Étapes suivantes de la conception :** revue des sites existants (`02-revue-des-sites.md`) à compléter dans un vrai navigateur, puis charte graphique et style des graphiques, puis maquettes à tester sur téléphone.
