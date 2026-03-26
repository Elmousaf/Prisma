# Prisma
Ressource diagramme Prisma

# Workflow PRISMA semi-automatisé pour le screening bibliographique en maladies cardiovasculaires et intelligence artificielle

## Présentation

Ce dépôt contient les scripts Python et les fichiers de travail utilisés pour soutenir un processus de sélection bibliographique inspiré des recommandations PRISMA. Le projet a été conçu pour organiser, fusionner, dédupliquer et présélectionner des articles scientifiques portant sur les maladies cardiovasculaires, l'intelligence artificielle, le machine learning, le deep learning et le suivi des patients.

Le workflow combine une phase de filtrage initial directement sur les plateformes bibliographiques, une phase de structuration des références dans un fichier commun, une détection automatique des doublons, puis une présélection thématique fondée sur des critères d'inclusion et d'exclusion. L'objectif est de fournir une base reproductible et traçable pour la lecture intégrale finale des études retenues.

## Objectif du dépôt

Ce projet a pour finalité de documenter et d'outiller une démarche méthodologique de screening bibliographique. Il permet notamment :

- d'importer des références issues de PubMed, ScienceDirect et Scopus ;
- de fusionner les enregistrements dans une base unique ;
- de détecter les doublons à partir des DOI, des PMID et des titres ;
- d'appliquer une présélection automatisée à partir de mots-clés thématiques ;
- de conserver les articles pertinents dans un fichier final dédié à la revue manuelle.

Ce dépôt constitue un outil d'aide à la sélection, et non un substitut à l'évaluation scientifique réalisée par le chercheur.

## Sources documentaires

Les références bibliographiques ont été identifiées à partir des sources suivantes :

- PubMed : 1 187 références initialement identifiées ;
- ScienceDirect : 327 références initialement identifiées ;
- Scopus : 275 références initialement identifiées ;
- autres sources : 3 références complémentaires ajoutées secondairement.

Après un premier filtrage réalisé directement sur les plateformes documentaires, 354 références ont été exportées pour traitement algorithmique :

- 69 références issues de PubMed ;
- 10 références issues de ScienceDirect ;
- 275 références issues de Scopus.

## Stratégies de recherche

Les recherches ont été conduites à partir de requêtes ciblant les maladies cardiovasculaires, les approches d'intelligence artificielle et le suivi des patients.

### PubMed

La recherche PubMed a été réalisée à l'aide de la requête suivante :

```text
("cardiovascular diseases"[MeSH Terms] OR "heart disease"[Title/Abstract]) AND ("machine learning"[Title/Abstract] OR "artificial intelligence"[Title/Abstract] OR "deep learning"[Title/Abstract]) AND ("humans"[MeSH Terms]) AND ("patient monitoring"[Title/Abstract] OR "follow-up"[Title/Abstract] OR "remote monitoring"[Title/Abstract] OR "self-management"[Title/Abstract]) AND ("2016/01/01"[Date - Publication] : "2026/12/31"[Date - Publication])
```

La sélection des références PubMed a ensuite été appuyée par les scripts Python du projet, utilisés pour structurer les données, détecter les doublons, évaluer la pertinence thématique à partir du titre et, lorsque disponible, du résumé, puis attribuer un score sur une échelle allant jusqu'à 5.

### ScienceDirect

La recherche ScienceDirect a été conduite à l'aide de la requête suivante :

```text
("cardiovascular disease" OR "heart disease") AND ("machine learning" OR "artificial intelligence" OR "deep learning") AND ("patient follow-up") AND ("risk prediction" OR "clinical decision")
```

Pour ScienceDirect, le traitement initial a été réalisé manuellement sur la plateforme. Dix articles ont été retenus après application des filtres documentaires, puis ajoutés au fichier Excel commun afin d'être soumis au même processus de vérification automatique des doublons et d'évaluation par critères que les autres références.

### Scopus

La recherche Scopus a été réalisée à l'aide de la requête suivante :

```text
TITLE-ABS-KEY ( "cardiovascular disease" OR "heart disease" ) AND TITLE-ABS-KEY ( "machine learning" OR "deep learning" OR "artificial intelligence" ) AND TITLE-ABS-KEY ( "remote monitoring" OR "patient monitoring" OR telemedicine ) AND TITLE-ABS-KEY ( human OR humans OR patient ) AND PUBYEAR > 2015 AND ( LIMIT-TO ( DOCTYPE,"ar" ) ) AND ( LIMIT-TO ( SUBJAREA,"MEDI" ) OR LIMIT-TO ( SUBJAREA,"COMP" ) OR LIMIT-TO ( SUBJAREA,"ENGI" ) ) AND ( LIMIT-TO ( LANGUAGE,"English" ) OR LIMIT-TO ( LANGUAGE,"French" ) )
```

Les références Scopus exportées après filtrage sur la plateforme ont ensuite été intégrées au même pipeline de traitement que les références issues de PubMed et de ScienceDirect.

## Critères de sélection

### Critères d'inclusion

Les références étaient considérées comme potentiellement éligibles lorsqu'elles répondaient à un ou plusieurs des critères suivants :

- publication au cours des dix dernières années ;
- publication en français ou en anglais ;
- étude menée dans un cadre scientifique ;
- population humaine adulte ;
- présence de mots-clés ou de contenus liés aux maladies cardiovasculaires ;
- présence de mots-clés ou de contenus liés à l'intelligence artificielle, au machine learning ou au deep learning ;
- pertinence pour le suivi, le monitoring, la prédiction ou l'aide à la décision en santé cardiovasculaire.

### Critères d'exclusion

Les références pouvaient être exclues dans les cas suivants :

- étude animale ou préclinique ;
- population pédiatrique ou enfant ;
- publication hors du cadre scientifique retenu ;
- article antérieur à 2016 ;
- absence de mots-clés pertinents en lien avec les maladies cardiovasculaires, l'intelligence artificielle, le machine learning ou le deep learning ;
- absence de pertinence thématique dans le titre ou le résumé.

## Workflow méthodologique

Le workflow général du projet suit les étapes suivantes :

1. filtrage initial des résultats directement sur PubMed, ScienceDirect et Scopus ;
2. exportation des références retenues après ce premier tri ;
3. parsing et structuration des références dans un fichier Excel commun ;
4. fusion des références issues des différentes bases de données ;
5. détection automatique des doublons ;
6. application de critères d'inclusion et d'exclusion ;
7. attribution d'un score de pertinence aux articles ;
8. conservation des articles maintenus dans un fichier final ;
9. ajout secondaire de 3 références provenant d'autres sources ;
10. constitution du corpus final destiné à la lecture intégrale.

Dans ce processus, les références exportées depuis PubMed, ScienceDirect et Scopus sont intégrées dans la même base de travail. Les articles retenus après filtrage sur plateforme sont donc maintenus dans un pipeline commun jusqu'à la vérification automatique des doublons, puis jusqu'à la présélection finale fondée sur le score de pertinence.

## Résumé PRISMA

Au total, 1 789 références ont été identifiées à partir des bases principales, soit 1 187 depuis PubMed, 327 depuis ScienceDirect et 275 depuis Scopus. Après application d'un premier filtre documentaire sur les plateformes, 354 références ont été exportées pour traitement algorithmique.

La fusion des références dans une base unique a permis d'identifier 2 doublons, réduisant le nombre d'enregistrements à 352. Les critères d'inclusion et d'exclusion ont ensuite conduit à l'exclusion de 288 références et au maintien de 64 articles issus des bases principales. À ce corpus ont été ajoutées 3 références provenant d'autres sources, aboutissant à un total final de 67 articles retenus pour la lecture intégrale.

## Structure du projet

### Scripts Python

- `Papers_Parsing.py`  
  Importe et structure les références issues de plusieurs sources. Le script lit un export texte PubMed, un fichier CSV Scopus et un fichier Excel ScienceDirect, puis fusionne les données dans un fichier Excel unique de screening.

- `RechercheDuplicates.py`  
  Normalise les DOI, les PMID et les titres afin de construire une clé de déduplication. Le script marque les doublons, regroupe les enregistrements concernés et génère un rapport détaillé.

- `CriteriaExclusion.py`  
  Réalise une présélection automatisée à partir de listes de mots-clés associés au domaine cardiovasculaire, à l'intelligence artificielle, au monitoring et à la population humaine. Il attribue à chaque enregistrement une décision préliminaire, une justification et un score.

- `ArticlesMaintenus.py`  
  Sélectionne les articles conservés après scoring en filtrant les enregistrements dont le score est supérieur ou égal à 3. Il produit le fichier final contenant les articles maintenus pour analyse approfondie.

### Fichiers de données et de sortie

- `Pubmed1.txt`  
  Export brut des références issues de PubMed.

- `ScopusList.csv`  
  Export tabulaire des références issues de Scopus.

- `ScienceDirectListe.xlsx`  
  Fichier contenant les références issues de ScienceDirect retenues après filtrage initial.

- `AffichageARticlesTotal.xlsx`  
  Fichier Excel de screening contenant les références fusionnées et structurées.

- `duplicates_report_by_doi.xlsx`  
  Rapport de déduplication généré après normalisation des identifiants et des titres.

- `ExclusionCriteres_Final.xlsx`  
  Fichier de sortie contenant la décision préliminaire, la raison du classement et le score attribué à chaque article.

- `Articles_Maintenus.xlsx`  
  Fichier final regroupant les articles conservés après filtrage par score.

- `prisma.txt`  
  Notes méthodologiques et éléments textuels liés au processus PRISMA.

## Logique de scoring

La présélection automatisée repose sur des listes de mots-clés relatives :

- au domaine cardiovasculaire ;
- aux méthodes d'intelligence artificielle, de machine learning et de deep learning ;
- au monitoring, à la télémédecine et au suivi des patients ;
- à la population humaine adulte.

Les études animales sont exclues. Chaque article reçoit ensuite un score de pertinence. Les articles les plus pertinents sont classés comme inclus, les cas intermédiaires peuvent être conservés pour réévaluation, et les articles insuffisamment pertinents sont exclus. Le script final de maintien retient les articles ayant un score supérieur ou égal à 3.

## Prérequis

Environnement recommandé :

- Python 3.10 ou version ultérieure ;
- `pandas` ;
- `openpyxl`.

Installation des dépendances :

```bash
pip install pandas openpyxl
```

## Utilisation

Les scripts peuvent être exécutés dans l'ordre suivant :

```bash
python Papers_Parsing.py
python RechercheDuplicates.py
python CriteriaExclusion.py
python ArticlesMaintenus.py
```

Selon l'organisation locale des fichiers, certains chemins ou noms de fichiers peuvent nécessiter une adaptation avant exécution.

## Limites

Ce workflow constitue un outil de soutien au screening et non un système autonome de sélection définitive. Les décisions finales doivent être validées par une lecture manuelle des titres, des résumés, puis des textes intégraux lorsque cela est nécessaire.

Le système de score repose sur des règles heuristiques et sur la présence de mots-clés. Il améliore l'efficacité du tri, mais ne remplace pas le jugement méthodologique du chercheur.

## Reproductibilité

Ce dépôt vise à améliorer la traçabilité et la reproductibilité du processus de sélection bibliographique. Néanmoins, les résultats peuvent varier selon :

- la date d'interrogation des bases de données ;
- les filtres appliqués sur les plateformes ;
- le format des exports bibliographiques ;
- les arbitrages effectués lors de la validation manuelle ;
- l'évolution du contenu des bases documentaires.

## Citation

Si vous utilisez ou adaptez ce workflow dans un cadre académique ou scientifique, merci de citer le travail de recherche associé ou de mentionner explicitement ce dépôt.
