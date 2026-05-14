import pandas as pd

# -----------------------------
# Fichiers
# -----------------------------
INPUT_FILE = "Filtered_Final_PRISMA_Strict.xlsx"
OUTPUT_FILE = "Articles_Retenus.xlsx"

# -----------------------------
# Chargement
# -----------------------------
df = pd.read_excel(INPUT_FILE)

print("📊 Total articles:", len(df))

# -----------------------------
# Vérification colonne Database
# -----------------------------
if "Database" not in df.columns:
    print("⚠️ ATTENTION: colonne 'Database' absente !")
    df["Database"] = "Unknown"

# -----------------------------
# Vérification colonne Decision
# -----------------------------
if "Decision" not in df.columns:
    raise ValueError("❌ Colonne 'Decision' introuvable")

# -----------------------------
# Nettoyage Decision (CRUCIAL)
# -----------------------------
df["Decision"] = (
    df["Decision"]
    .fillna("")
    .astype(str)
    .str.strip()
    .str.lower()
)

# -----------------------------
# DEBUG distribution
# -----------------------------
print("\n📊 Répartition des décisions :")
print(df["Decision"].value_counts())

# -----------------------------
# Filtrage Include + Maybe
# -----------------------------
retained = df[df["Decision"].isin(["include", "maybe"])].copy()

print("\n✅ Articles retenus:", len(retained))

# -----------------------------
# DEBUG — trouver l'article manquant
# -----------------------------
print("\n🔎 Articles EXCLUS avec decision suspecte :")
suspects = df[
    (df["Decision"] != "include") &
    (df["Decision"] != "maybe") &
    (df["Decision"].str.contains("include|maybe", na=False))
]

print(suspects[["Title", "Decision"]])

# -----------------------------
# Colonnes à garder
# -----------------------------
columns = []

if "Record ID" in retained.columns:
    columns.append("Record ID")

columns.append("Database")

if "Title" in retained.columns:
    columns.append("Title")

if "Abstract" in retained.columns:
    columns.append("Abstract")

if "DOI" in retained.columns:
    columns.append("DOI")

if "PMID" in retained.columns:
    columns.append("PMID")

# colonnes optionnelles
for col in ["Decision", "Reason", "Score"]:
    if col in retained.columns:
        columns.append(col)

retained = retained[columns]

# -----------------------------
# Sauvegarde
# -----------------------------
retained.to_excel(OUTPUT_FILE, index=False)

print("\n✅ Fichier créé :", OUTPUT_FILE)