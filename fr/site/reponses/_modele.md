<!-- page
slug: nom-du-fichier-sans-md
phrase: La phrase entendue, telle qu’on l’entend
sujets: sujet-principal, autre-sujet
montant: identifiant_du_montant_eur_bn
levier: R0, S0
debats: 0.0, 0.0
-->

<!--
MODÈLE DE PAGE DE RÉPONSE (non publié : les fichiers dont le nom commence par « _ » sont ignorés
par validate.py et par le site). Format : fr/conception/05-pages-de-reponse.md.

Mode d’emploi
- Copier ce fichier en fr/site/reponses/<slug>.md (slug de fr/conception/04-sujets-et-objections.md).
- Métadonnées ci-dessus :
  - slug : identique au nom du fichier, sans « .md » (vérifié : [answer-meta]).
  - phrase : la phrase entendue, sans guillemets ; c’est aussi le titre affiché.
  - sujets : slugs des sujets qui montrent la page (04-sujets-et-objections.md §3), séparés par des virgules.
  - montant (facultatif) : identifiant de figures.json, yardsticks.json ou proposals.json ; il est affiché
    dans la liste des réponses.
  - levier (facultatif) : identifiants de simulator-levers.json ; le site en tire le bouton
    « Ajouter à mon budget » (ne pas l’écrire dans le texte). Supprimer la ligne s’il n’y a pas de levier.
  - debats (facultatif) : points de fr/site/debats.md.
- Seules les lignes « > » sont affichées. Ordre obligatoire, une fois chacun ([answer-structure]) :
  titre « # « … » », paragraphe « **En bref.** », puis ## Ce qui est vrai, ## Combien,
  ## Les limites, ## Qui dit quoi, ## Et ailleurs ? ; chaque section a du texte.
- Longueur : 300 à 900 mots affichés (cible 450 à 700). Phrases de 25 mots au plus, paragraphes de
  60 mots au plus. Sigle développé à la première occurrence. Typographie : glossaire §2.
- Tout chiffre affiché a sa pastille : [[fig:id]], [[yard:id]], [[prop:id]], [[calc:formule = résultat]],
  [[src:id]] pour une source sans chiffre. Pastille de contexte (pas de nombre affiché) : [[fig:id|contexte]].
- Aucun chiffre inventé, aucun chiffre sans identifiant : l’omettre et le consigner sous
  « Données manquantes » ci-dessous.
- Aucune étiquette de camp sur une idée ou une objection ; les organismes gardent leur étiquette du
  glossaire §1.13, mot pour mot. Un fait, pas un verdict.
- Vérifier : python3 -I platform/data/validate.py --strict --reponses fr/site/reponses/<slug>.md

NOTES POUR L’ÉQUIPE
- Sources lues : (fichiers de research/ et sources.json consultés, avec leur date).
- Données manquantes : (chiffres utiles sans identifiant dans figures.json ; à verser avant publication).
- Choix faits : (fourchette retenue, chiffrages écartés et pourquoi, unité de complément utilisée).
-->

> # « La phrase entendue, telle qu’on l’entend »
>
> **En bref.** Une ou deux phrases de réponse, avec le montant annuel en milliards d’euros [[fig:identifiant_du_montant_eur_bn]] et sa part du déficit de référence [[calc:identifiant_du_montant_eur_bn / deficit_2025_eur_bn * 100 = X]]. Un fait, pas un verdict.
>
> ## Ce qui est vrai
>
> Ce que la phrase a de juste, chiffré et sourcé [[fig:identifiant_du_constat]]. Toujours présent, jamais vide.
>
> ## Combien
>
> Le montant annuel, en fourchette si les estimations divergent : de X à Y milliards d’euros par an [[fig:identifiant_du_montant_eur_bn]]. Rapporté au déficit de l’an dernier, notifié à Eurostat (X milliards d’euros [[fig:deficit_2025_eur_bn]]), cela représente de X à Y % du déficit [[calc:identifiant_du_montant_eur_bn__low / deficit_2025_eur_bn * 100 = X ; identifiant_du_montant_eur_bn__high / deficit_2025_eur_bn * 100 = Y]].
>
> Une seule autre unité, une fois, en complément (% du PIB ou euros par habitant).
>
> ## Les limites
>
> Ce qui rend le chiffre incertain ou non additionnable : réactions des contribuables ou des bénéficiaires, montée en charge, risque juridique, double compte avec une autre mesure, effet sur la croissance.
>
> ## Qui dit quoi
>
> - **Auteur ou organisme (étiquette du glossaire §1.13, mot pour mot)** : montant, date, ce qu’il retient [[prop:identifiant_de_la_proposition]].
> - **Autre auteur ou organisme (étiquette du glossaire §1.13)** : montant, date, ce qu’il retient [[src:identifiant_de_la_source]].
>
> Au moins deux lectures quand elles existent ; si une seule position publiée a été trouvée, l’écrire.
>
> ## Et ailleurs ?
>
> La France comparée à l’Union européenne à 27 (UE-27), à la zone euro, à l’Organisation de coopération et de développement économiques (OCDE) et au panel (Allemagne, Italie, Espagne, Pays-Bas, Belgique, Suède, Danemark) [[fig:identifiant_de_la_comparaison]].
>
> Quand les données existent : « Même après cette mesure, la France resterait Xe sur 27 », sans commentaire.
