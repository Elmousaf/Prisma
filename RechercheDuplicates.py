import re
import os
import pandas as pd

# -----------------------------
# Paths
# -----------------------------
IN_PATH  = "AffichageArticlesTotal.xlsx"   
OUT_PATH = "duplicates_report_by_doi.xlsx"

# -----------------------------
# Helpers
# -----------------------------
def normalize_doi(doi):
    """
    Normalize DOI strings:
    - lowercase
    - strip whitespace
    - remove https://doi.org/
    - remove trailing punctuation
    """
    if not isinstance(doi, str):
        return ""
    doi = doi.strip().lower()
    doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", doi)
    doi = doi.rstrip(" .;,)")
    return doi


def normalize_title(title):
    """
    Normalize title (fallback)
    """
    if not isinstance(title, str):
        return ""
    t = title.lower()
    t = re.sub(r"[^a-z0-9]+", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t


# -----------------------------
# Load Excel
# -----------------------------
try:
    df = pd.read_excel(IN_PATH, sheet_name="Screening")
except Exception as e:
    print(f"❌ Error loading file: {e}")
    exit()

# -----------------------------
# Validate columns
# -----------------------------
required_cols = ["DOI", "PMID", "Title"]
for col in required_cols:
    if col not in df.columns:
        raise ValueError(f"❌ Missing column: {col}")

# -----------------------------
# Normalize data
# -----------------------------
df["DOI_norm"] = df["DOI"].apply(normalize_doi)

# Convert PMID to string and replace NaN with empty string
df["PMID_norm"] = df["PMID"].fillna("").astype(str).str.strip()

# Convert "0" or "0.0" to empty string (optionnel)
df["PMID_norm"] = df["PMID_norm"].replace({"0": "", "0.0": ""})

df["Title_norm"] = df["Title"].apply(normalize_title)

# -----------------------------
# Build duplicate key
# -----------------------------
def build_dup_key(row):
    """
    Crée une clé unique pour détecter les doublons
    """
    if row["DOI_norm"]:
        return "DOI:" + row["DOI_norm"]
    if row["PMID_norm"]:
        return "PMID:" + str(row["PMID_norm"])
    return "TITLE:" + row["Title_norm"]

df["DupKey"] = df.apply(build_dup_key, axis=1)

# -----------------------------
# Detect duplicates
# -----------------------------
df["IsDuplicate"] = df.duplicated("DupKey", keep=False)

dup_groups = df[df["IsDuplicate"]].copy()

# Assign group IDs
dup_groups["DuplicateGroupID"] = (
    dup_groups.groupby("DupKey").ngroup().apply(lambda x: f"D{str(x+1).zfill(4)}")
)

# Count duplicates
dup_counts = (
    dup_groups.groupby("DupKey")
    .size()
    .reset_index(name="Count")
    .sort_values("Count", ascending=False)
)

# Merge counts
dup_groups = dup_groups.merge(dup_counts, on="DupKey", how="left")

# Sort
dup_groups = dup_groups.sort_values(
    ["Count", "DupKey", "Database", "Record ID"],
    ascending=[False, True, True, True]
)

# -----------------------------
# Save Excel (safe write)
# -----------------------------
if os.path.exists(OUT_PATH):
    try:
        os.remove(OUT_PATH)
    except PermissionError:
        print("⚠️ Ferme le fichier Excel avant de relancer.")
        exit()

with pd.ExcelWriter(OUT_PATH, engine="openpyxl", mode="w") as writer:
    df.to_excel(writer, index=False, sheet_name="AllRecords_WithFlags")
    dup_groups.to_excel(writer, index=False, sheet_name="Duplicates_Grouped")
    dup_counts.to_excel(writer, index=False, sheet_name="DuplicateKey_Summary")

print("✅ Saved duplicate report to:", OUT_PATH)