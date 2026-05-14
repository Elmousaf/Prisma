Semi-Automated PRISMA Workflow for Cardiovascular Disease Prediction Literature Screening
Overview

This repository contains the Python scripts, datasets, and methodological resources used to build a semi-automated workflow inspired by the PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses) framework.

The main objective is to assist in identifying, organizing, deduplicating, scoring, and preselecting scientific studies related to:

cardiovascular diseases;
heart disease prediction;
artificial intelligence (AI);
machine learning (ML);
deep learning (DL);
patient monitoring;
remote monitoring;
cardiovascular risk stratification.

The workflow combines automated processing with manual scientific validation. The scripts accelerate the initial screening stages, while the final inclusion decisions remain under the responsibility of the researcher.

Project Objective

This project aims to provide a reproducible and transparent workflow for bibliographic screening within the context of a systematic review focused on cardiovascular disease prediction using artificial intelligence methods.

The workflow enables researchers to:

import references exported from PubMed and Scopus;
merge references into a unified screening database;
automatically detect duplicates using DOI, PMID, and titles;
apply a relevance score based on thematic keywords;
automatically exclude certain studies according to predefined criteria;
generate Excel files for manual verification and full-text review;
improve transparency and reproducibility of the PRISMA process.
PRISMA Methodological Framework

The project follows the PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses) methodological framework, which is widely adopted in systematic reviews.

This approach ensures:

transparency;
reproducibility;
methodological rigor;
traceability of the selection process;
justification of included and excluded studies.

The workflow covers the main PRISMA stages:

study identification;
duplicate removal;
automated screening;
relevance scoring;
manual reassessment;
full-text review;
final inclusion.
Data Sources

The bibliographic references were collected primarily from two major scientific databases:

Database	Identified References
PubMed	192
Scopus	749

Additional references were also included from other relevant sources:

Other Sources	Number
Additional references	3

Total number of identified records before deduplication:

941 records
Search Strategy

The search equations targeted studies combining:

cardiovascular diseases;
machine learning or artificial intelligence;
risk prediction or prognosis;
patient monitoring or telemonitoring;
publications between 2016 and 2026;
English-language articles.
Search Queries
PubMed Query
("Cardiovascular Diseases"[MeSH] OR "cardiovascular disease"[Title/Abstract] OR "heart disease"[Title/Abstract] OR "arrhythmia"[Title/Abstract])
AND ("machine learning"[Title/Abstract] OR "artificial intelligence"[Title/Abstract] OR "deep learning"[Title/Abstract])
AND ("risk"[Title/Abstract] OR "prediction"[Title/Abstract] OR "prognosis"[Title/Abstract] OR "early detection"[Title/Abstract] OR "risk stratification"[Title/Abstract])
AND ("patient monitoring"[Title/Abstract] OR "remote monitoring"[Title/Abstract] OR "continuous monitoring"[Title/Abstract] OR "real-time monitoring"[Title/Abstract] OR "telemonitoring"[Title/Abstract] OR "ambulatory monitoring"[Title/Abstract])
AND ("2016/01/01"[Date - Publication] : "2026/04/30"[Date - Publication])
AND (English[Language])
Scopus Query
TITLE-ABS-KEY ( "cardiovascular disease" OR "heart disease" OR "arrhythmia" )
AND TITLE-ABS-KEY ( "machine learning" OR "artificial intelligence" OR "deep learning" )
AND TITLE-ABS-KEY ( "risk" OR "prediction" OR "prognosis" OR "early detection" OR "risk stratification" )
AND TITLE-ABS-KEY ( "patient monitoring" OR "remote monitoring" OR "continuous monitoring" OR "real-time monitoring" OR "telemonitoring" OR "ambulatory monitoring")
AND PUBYEAR > 2015
AND PUBYEAR < 2027
AND ( LIMIT-TO ( LANGUAGE, "English" ))
Study Selection Process

A total of:

941 articles

were exported from PubMed and Scopus.

The references were merged into a single database and processed using automated Python scripts enabling:

duplicate detection;
thematic preselection;
relevance scoring;
preliminary inclusion and exclusion decisions.
Duplicate Detection

The automated deduplication process identified:

123 duplicates

Duplicate detection was based on:

DOI comparison;
PMID comparison;
normalized title comparison.

After duplicate removal:

818 unique records

remained for screening.

Exclusion Criteria

The following exclusion criteria were applied:

Exclusion Criterion	Excluded Articles
Animal studies	61
Studies focused only on IoT or wearable devices	165
Pediatric studies	8
Reviews and meta-analyses	29
Studies outside the combined domains	467
Publications older than 10 years	0
Non-English articles	0

Total excluded articles:

730 articles
Inclusion Criteria

Studies were considered relevant when they combined:

a cardiovascular disease topic;
AI / ML / DL approaches;
patient monitoring concepts;
prediction or risk assessment tasks;
recent publication dates;
English-language publication.

Example of a relevant keyword combination:

risk + cardiovascular disease + machine learning + patient monitoring
Scoring System

Each article automatically receives a relevance score ranging from 1 to 5.

Scoring Criteria
Criterion	Score
Cardiovascular relevance	+2
AI / ML / DL relevance	+2
Patient monitoring relevance	+1

Maximum score:

5
Score Interpretation
Score	Decision
Score ≥ 4	Included for full-text review
Score = 3	Requires manual reassessment
Score < 3	Excluded
Screening Results

After applying exclusion criteria and automated scoring:

Step	Number
Excluded articles	730
Automatically included articles	62
“Maybe” articles	26
Full-text assessed articles	88

After full-text review:

Final Result	Number
Articles retained from PubMed and Scopus	39
Additional articles from other sources	3
Final systematic review corpus	42
General Workflow

The workflow follows these steps:

bibliographic search in PubMed and Scopus;
export of references;
reference merging;
automatic duplicate removal;
keyword-based thematic scoring;
application of inclusion and exclusion criteria;
manual verification of uncertain articles;
full-text reading;
final inclusion of retained studies.
Project Structure
Main Scripts
Papers_Parsing.py

This script represents the first stage of the workflow.

It:

imports exported files from PubMed and Scopus;
extracts the main metadata;
merges all references into a unified screening file.

Input files:

Pubmed1.txt
Scopus.csv

Generated file:

AffichageArticlesTotal.xlsx
RechercheDuplicates.py

This script detects and removes duplicate references.

Methods used:

DOI comparison;
PMID comparison;
normalized title comparison.

Generated file:

Deduplicated_Final.xlsx
CriteriaExclusion.py

This script applies:

exclusion criteria;
automated scoring;
preliminary decisions.

Possible decisions:

Include
Maybe
Exclude

Generated file:

Filtered_Final_PRISMA_Strict.xlsx
ArticlesMaintenus.py

This script retains articles with a score greater than or equal to 3.

Generated file:

Articles_Maintenus.xlsx
RetenusArticles.py

Alternative filtering script retaining only articles classified as:

Include
Maybe

Generated file:

Articles_Retenus.xlsx
Prisma.py

This script automatically generates the PRISMA flow diagram of the workflow.

Methodstatistics.py

Produces statistics regarding the most frequently used AI methods, including:

Random Forest;
SVM;
CNN;
XGBoost;
LSTM;
ANN;
RNN;
etc.
diagramme2.py

Generates a graphical representation of the most commonly used datasets:

Cleveland;
MIT-BIH;
Kaggle;
PhysioNet;
Framingham;
MIMIC-III;
UK Biobank.
Recommended Execution Order
python Papers_Parsing.py
python RechercheDuplicates.py
python CriteriaExclusion.py
python ArticlesMaintenus.py

Visualization scripts:

python Prisma.py
python Methodstatistics.py
python diagramme2.py
Requirements

Recommended environment:

Python 3.10 or higher.

Required libraries:

pandas
openpyxl
matplotlib
numpy
pillow
requests

Installation:

pip install pandas openpyxl matplotlib numpy pillow requests
Limitations

This workflow is intended as a bibliographic screening support tool and does not replace manual scientific evaluation.

The scoring system relies on:

heuristic rules;
keyword lists;
automated criteria.

Final inclusion decisions must always be validated through:

title reading;
abstract reading;
full-text review.
Reproducibility

The project aims to improve:

transparency;
traceability;
reproducibility of bibliographic screening.

Each stage generates an intermediate file, allowing researchers to track the evolution of references from the initial import to the final selection.

Citation

If you use or adapt this workflow in an academic or scientific context, please cite the associated research work or explicitly mention this repository.
