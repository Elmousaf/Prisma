import re
import os
import pandas as pd

# -----------------------------
# PATHS
# -----------------------------
IN_PATH  = "AffichageArticlesTotal.xlsx"
OUT_PATH = "duplicates_report_by_doi.xlsx"

# -----------------------------
# NORMALISATION DOI
# -----------------------------
def normalize_doi(doi):
    if not isinstance(doi, str):
        return ""
    doi = doi.strip().lower()
    doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", doi)
    doi = doi.rstrip(" .;,)")  
    return doi

# -----------------------------
# NORMALISATION TITLE
# -----------------------------
def normalize_title(title):
    if not isinstance(title, str):
        return ""
    t = title.lower()
    t = re.sub(r"[^a-z0-9]+", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_excel(IN_PATH, sheet_name="Screening")

# -----------------------------
# CHECK COLUMNS
# -----------------------------
for col in ["DOI", "PMID", "Title"]:
    if col not in df.columns:
        raise ValueError(f"Missing column: {col}")

# -----------------------------
# NORMALIZATION
# -----------------------------
df["DOI_norm"] = df["DOI"].apply(normalize_doi)

df["PMID_norm"] = df["PMID"].fillna("").astype(str).str.strip()
df["PMID_norm"] = df["PMID_norm"].replace({"0": "", "0.0": ""})

df["Title_norm"] = df["Title"].apply(normalize_title)

# -----------------------------
# DUP KEY
# -----------------------------
def build_key(row):
    if row["DOI_norm"]:
        return "DOI:" + row["DOI_norm"]
    if row["PMID_norm"]:
        return "PMID:" + row["PMID_norm"]
    return "TITLE:" + row["Title_norm"]

df["DupKey"] = df.apply(build_key, axis=1)

# -----------------------------
# COUNT DUPLICATES PER ARTICLE
# -----------------------------
dup_counts = df.groupby("DupKey").size().reset_index(name="DuplicateCount")

df = df.merge(dup_counts, on="DupKey", how="left")

# -----------------------------
# KEEP ONLY ONE VERSION PER ARTICLE
# -----------------------------
df_unique = df.drop_duplicates("DupKey", keep="first").copy()

# -----------------------------
# CLEAN DISPLAY COLUMN
# -----------------------------
df_unique["DuplicateInfo"] = df_unique["DuplicateCount"].apply(
    lambda x: "No duplicate" if x == 1 else f"Duplicated {x-1} time(s)"
)

# -----------------------------
# STATS
# -----------------------------
total = len(df)
final = len(df_unique)
duplicates_removed = total - final

print("\n===== DUPLICATE SUMMARY =====")
print(f"Total records        : {total}")
print(f"Final records        : {final}")
print(f"Duplicates removed   : {duplicates_removed}")
print("============================\n")

# -----------------------------
# SAVE
# -----------------------------
df_unique.to_excel("Deduplicated_Final.xlsx", index=False)

print("Saved: Deduplicated_Final.xlsx")