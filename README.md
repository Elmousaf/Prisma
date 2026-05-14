Workflow PRISMA semi-automatisé pour la sélection d’articles sur la prédiction des maladies cardiovasculaires
Présentation

Ce dépôt contient les scripts Python, les fichiers de données et les ressources méthodologiques utilisés pour construire un workflow semi-automatisé inspiré du cadre PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses).

L’objectif principal est d’aider à identifier, organiser, dédupliquer, scorer et présélectionner des études scientifiques portant sur :

les maladies cardiovasculaires ;
la prédiction des maladies cardiaques ;
l’intelligence artificielle (IA) ;
le machine learning (ML) ;
le deep learning (DL) ;
le suivi des patients (patient monitoring) ;
le monitoring à distance (remote monitoring) ;
la stratification du risque cardiovasculaire.

Le workflow combine des traitements automatisés avec une validation scientifique manuelle. Les scripts accélèrent les premières étapes du screening bibliographique, mais les décisions finales d’inclusion restent réalisées par le chercheur.

Objectif du projet

Ce projet vise à fournir un workflow reproductible et transparent pour le screening bibliographique dans le cadre d’une revue systématique portant sur la prédiction des maladies cardiovasculaires à l’aide de méthodes d’intelligence artificielle.

Le workflow permet notamment de :

importer les références exportées depuis PubMed et Scopus ;
fusionner les références dans une base de screening unique ;
détecter automatiquement les doublons à partir des DOI, PMID et titres ;
appliquer un score de pertinence basé sur des mots-clés ;
exclure automatiquement certains articles selon des critères prédéfinis ;
générer des fichiers Excel exploitables pour la vérification manuelle ;
améliorer la traçabilité et la reproductibilité du processus PRISMA.
Cadre méthodologique PRISMA

Le projet suit le cadre méthodologique PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses), largement utilisé dans les revues systématiques.

Cette approche permet d’assurer :

la transparence ;
la reproductibilité ;
la rigueur méthodologique ;
la traçabilité du processus de sélection ;
la justification des articles inclus et exclus.

Le workflow couvre les principales étapes PRISMA :

identification des études ;
suppression des doublons ;
screening automatisé ;
scoring de pertinence ;
réévaluation manuelle ;
lecture intégrale ;
inclusion finale.
Sources de données

Les références bibliographiques proviennent principalement de deux bases scientifiques majeures :

Base de données	Références identifiées
PubMed	192
Scopus	749

Des références supplémentaires ont également été ajoutées depuis d’autres sources :

Autres sources	Nombre
Références complémentaires	3

Nombre total de références identifiées avant déduplication :

941 références
Stratégie de recherche

Les requêtes de recherche ciblaient les études combinant :

les maladies cardiovasculaires ;
le machine learning ou l’intelligence artificielle ;
la prédiction du risque ou le pronostic ;
le patient monitoring ou le télémonitoring ;
des publications entre 2016 et 2026 ;
des articles en anglais.
Requêtes de recherche
Requête PubMed
("Cardiovascular Diseases"[MeSH] OR "cardiovascular disease"[Title/Abstract] OR "heart disease"[Title/Abstract] OR "arrhythmia"[Title/Abstract])
AND ("machine learning"[Title/Abstract] OR "artificial intelligence"[Title/Abstract] OR "deep learning"[Title/Abstract])
AND ("risk"[Title/Abstract] OR "prediction"[Title/Abstract] OR "prognosis"[Title/Abstract] OR "early detection"[Title/Abstract] OR "risk stratification"[Title/Abstract])
AND ("patient monitoring"[Title/Abstract] OR "remote monitoring"[Title/Abstract] OR "continuous monitoring"[Title/Abstract] OR "real-time monitoring"[Title/Abstract] OR "telemonitoring"[Title/Abstract] OR "ambulatory monitoring"[Title/Abstract])
AND ("2016/01/01"[Date - Publication] : "2026/04/30"[Date - Publication])
AND (English[Language])
Requête Scopus
TITLE-ABS-KEY ( "cardiovascular disease" OR "heart disease" OR "arrhythmia" )
AND TITLE-ABS-KEY ( "machine learning" OR "artificial intelligence" OR "deep learning" )
AND TITLE-ABS-KEY ( "risk" OR "prediction" OR "prognosis" OR "early detection" OR "risk stratification" )
AND TITLE-ABS-KEY ( "patient monitoring" OR "remote monitoring" OR "continuous monitoring" OR "real-time monitoring" OR "telemonitoring" OR "ambulatory monitoring")
AND PUBYEAR > 2015
AND PUBYEAR < 2027
AND ( LIMIT-TO ( LANGUAGE, "English" ))
Processus de sélection des études

Au total :

941 articles

ont été exportés depuis PubMed et Scopus.

Les références ont ensuite été fusionnées dans une base unique puis traitées à l’aide de scripts Python automatisés permettant :

la détection des doublons ;
la présélection thématique ;
le scoring de pertinence ;
les décisions préliminaires d’inclusion ou d’exclusion.
Détection des doublons

Le processus automatique de déduplication a permis d’identifier :

123 doublons

La détection des doublons repose sur :

la comparaison des DOI ;
la comparaison des PMID ;
la comparaison des titres normalisés.

Après suppression des doublons :

818 références uniques

sont restées pour le screening.

Critères d’exclusion

Les critères d’exclusion suivants ont été appliqués :

Critère d’exclusion	Nombre exclu
Études animales	61
Études centrées uniquement sur l’IoT ou les wearables	165
Études pédiatriques	8
Revues et méta-analyses	29
Études hors des domaines combinés	467
Publications antérieures à 2016	0
Articles non anglophones	0

Nombre total d’articles exclus :

730 articles
Critères d’inclusion

Les études étaient considérées comme pertinentes lorsqu’elles combinaient :

une problématique cardiovasculaire ;
des approches IA / ML / DL ;
du monitoring patient ;
de la prédiction ou de l’évaluation du risque ;
une publication récente ;
une publication en anglais.

Exemple de combinaison pertinente :

risk + cardiovascular disease + machine learning + patient monitoring
Système de scoring

Chaque article reçoit automatiquement un score de pertinence compris entre 1 et 5.

Critères utilisés
Critère	Score
Pertinence cardiovasculaire	+2
Pertinence IA / ML / DL	+2
Pertinence monitoring patient	+1

Le score maximal est limité à :

5
Interprétation des scores
Score	Décision
Score ≥ 4	Inclusion pour lecture intégrale
Score = 3	Vérification manuelle nécessaire
Score < 3	Exclusion
Résultats du screening

Après application des critères d’exclusion et du scoring :

Étape	Nombre
Articles exclus	730
Articles inclus automatiquement	62
Articles classés “Maybe”	26
Articles évalués en texte intégral	88

Après lecture intégrale :

Résultat final	Nombre
Articles retenus depuis PubMed et Scopus	39
Articles ajoutés depuis d’autres sources	3
Corpus final de la revue systématique	42
Workflow général

Le workflow suit les étapes suivantes :

recherche bibliographique dans PubMed et Scopus ;
export des références ;
fusion des références ;
suppression automatique des doublons ;
scoring thématique par mots-clés ;
application des critères d’inclusion et d’exclusion ;
vérification manuelle des articles incertains ;
lecture intégrale ;
inclusion finale des études retenues.
Structure du projet
Scripts principaux
Papers_Parsing.py

Ce script constitue la première étape du workflow.

Il :

importe les fichiers exportés depuis PubMed et Scopus ;
extrait les métadonnées principales ;
fusionne les références dans un fichier unique de screening.

Fichiers d’entrée :

Pubmed1.txt
Scopus.csv

Fichier généré :

AffichageArticlesTotal.xlsx
RechercheDuplicates.py

Ce script détecte et supprime les doublons.

Méthodes utilisées :

comparaison DOI ;
comparaison PMID ;
comparaison des titres normalisés.

Fichier généré :

Deduplicated_Final.xlsx
CriteriaExclusion.py

Ce script applique :

les critères d’exclusion ;
le scoring automatique ;
les décisions préliminaires.

Décisions possibles :

Include
Maybe
Exclude

Fichier généré :

Filtered_Final_PRISMA_Strict.xlsx
ArticlesMaintenus.py

Ce script conserve les articles dont le score est supérieur ou égal à 3.

Fichier généré :

Articles_Maintenus.xlsx
RetenusArticles.py

Variante permettant de conserver uniquement les articles :

Include
Maybe

Fichier généré :

Articles_Retenus.xlsx
Prisma.py

Ce script génère automatiquement le diagramme PRISMA du workflow.

Methodstatistics.py

Produit des statistiques sur les méthodes IA les plus utilisées :

Random Forest ;
SVM ;
CNN ;
XGBoost ;
LSTM ;
ANN ;
RNN ;
etc.
diagramme2.py

Produit un graphique des bases de données les plus utilisées :

Cleveland ;
MIT-BIH ;
Kaggle ;
PhysioNet ;
Framingham ;
MIMIC-III ;
UK Biobank.
Ordre d’exécution recommandé
python Papers_Parsing.py
python RechercheDuplicates.py
python CriteriaExclusion.py
python ArticlesMaintenus.py

Visualisations :

python Prisma.py
python Methodstatistics.py
python diagramme2.py
Prérequis

Environnement recommandé :

Python 3.10 ou supérieur.

Bibliothèques nécessaires :

pandas
openpyxl
matplotlib
numpy
pillow
requests

Installation :

pip install pandas openpyxl matplotlib numpy pillow requests
Limites

Ce workflow constitue un outil d’aide au screening bibliographique et ne remplace pas l’évaluation scientifique manuelle.

Le scoring repose sur :

des règles heuristiques ;
des listes de mots-clés ;
des critères automatiques.

Les décisions finales doivent toujours être validées par :

la lecture du titre ;
la lecture du résumé ;
la lecture intégrale des articles.
Reproductibilité

Le projet vise à améliorer :

la transparence ;
la traçabilité ;
la reproductibilité du screening bibliographique.

Chaque étape produit un fichier intermédiaire permettant de suivre l’évolution des références depuis l’import initial jusqu’à la sélection finale.

Citation

Si vous utilisez ou adaptez ce workflow dans un cadre académique ou scientifique, merci de citer le travail de recherche associé ou de mentionner explicitement ce dépôt GitHub.
