import re
import pandas as pd
from openpyxl.utils import get_column_letter

# -----------------------------
# Paths to files
# -----------------------------
PUBMED_PATH = "Pubmed1.txt"                   # Fichier texte PubMed
SCOPUS_PATH = "ScopusList.csv"                # Fichier CSV Scopus
SCIENCE_DIRECT_PATH = "ScienceDirectListe.xlsx"  # Fichier Excel ScienceDirect
OUT_PATH = "AffichageArticlesTotal.xlsx"         # Fichier Excel de sortie

# =============================
# 1️⃣ Load PubMed text
# =============================
with open(PUBMED_PATH, encoding="utf-8", errors="ignore") as f:
    pubmed_text = f.read()

# =============================
# 2️⃣ Parse PubMed records
# =============================
def parse_pubmed_records(text):
    """
    Parse les articles depuis un fichier texte PubMed.
    Retourne une liste de dictionnaires avec : Database, Title, DOI, PMID
    """
    recs = []
    entries = re.split(r"\n(?=\d+: )", text.strip())  # Split par enregistrement
    for e in entries:
        m = re.match(r"(\d+):\s*(.*)", e, flags=re.S)
        if not m:
            continue
        body = " ".join([ln.strip() for ln in m.group(2).splitlines() if ln.strip()])
        # Extraction du titre
        parts = body.split(". ")
        title = parts[1].strip().rstrip(".") if len(parts) > 1 else parts[0].strip().rstrip(".")
        # Extraction DOI
        m_doi = re.search(r"\bdoi:\s*([^\s;]+)", body, flags=re.I)
        doi = m_doi.group(1).rstrip(".") if m_doi else ""
        # Extraction PMID
        m_pmid = re.search(r"PMID:\s*(\d+)", body)
        pmid = m_pmid.group(1) if m_pmid else ""
        recs.append({
            "Database": "PubMed",
            "Title": title,
            "DOI": doi,
            "PMID": pmid
        })
    return recs

pubmed_recs = parse_pubmed_records(pubmed_text)

# =============================
# 3️⃣ Parse Scopus records (CSV)
# =============================
def parse_scopus_records(path):
    """
    Parse les articles depuis un fichier CSV Scopus.
    """
    df = pd.read_csv(path)
    recs = []
    for _, row in df.iterrows():
        recs.append({
            "Database": "Scopus",
            "Title": str(row.get("Title", "")).strip(),
            "DOI": str(row.get("DOI", "")).strip(),
            "PMID": ""  # Souvent vide dans Scopus
        })
    return recs

scopus_recs = parse_scopus_records(SCOPUS_PATH)

# =============================
# 4️⃣ Parse ScienceDirect records (Excel)
# =============================
def parse_sciencedirect_records(path):
    """
    Parse les articles depuis un fichier Excel ScienceDirect.
    """
    df = pd.read_excel(path)  # read_excel pour .xlsx
    recs = []
    for _, row in df.iterrows():
        recs.append({
            "Database": "ScienceDirect",
            "Title": str(row.get("Title", "")).strip(),  # Vérifier que la colonne s'appelle "Title"
            "DOI": str(row.get("DOI", "")).strip(),
            "PMID": ""  # Généralement absent
        })
    return recs

sd_recs = parse_sciencedirect_records(SCIENCE_DIRECT_PATH)

# =============================
# 5️⃣ Merge all records
# =============================
all_recs = pubmed_recs + scopus_recs + sd_recs
df = pd.DataFrame(all_recs)

# =============================
# 6️⃣ Add Record ID (PRISMA)
# =============================
df.insert(0, "Record ID", [f"R{str(i+1).zfill(4)}" for i in range(len(df))])

# =============================
# 7️⃣ Add screening columns (PRISMA)
# =============================
for col in [
    "Stage (Title/Abstract/Full-text)",
    "Decision (Include/Exclude)",
    "Reason for Exclusion",
    "Notes"
]:
    df[col] = ""

# =============================
# 8️⃣ Counts summary
# =============================
counts = pd.DataFrame({
    "Database": ["PubMed","Scopus","ScienceDirect","Total"],
    "Records": [ len(pubmed_recs), len(scopus_recs), len(sd_recs), len(all_recs)]
})

print("Parsed records:")
print(f"  PubMed: {len(pubmed_recs)}")
print(f"  Scopus: {len(scopus_recs)}")
print(f"  ScienceDirect: {len(sd_recs)}")
print(f"  Total: {len(all_recs)}")

# =============================
# 9️⃣ Save Excel with auto column width
# =============================
with pd.ExcelWriter(OUT_PATH, engine="openpyxl") as writer:
    df.to_excel(writer, index=False, sheet_name="Screening")
    counts.to_excel(writer, index=False, sheet_name="Counts")

    # Auto-fit columns
    for sheet_name in writer.sheets:
        ws = writer.sheets[sheet_name]
        for col in ws.columns:
            max_length = 0
            column = col[0].column_letter
            for cell in col:
                if cell.value:
                    max_length = max(max_length, len(str(cell.value)))
            ws.column_dimensions[column].width = min(max_length + 5, 100)  # cap at 100 chars

print("✅ Saved Excel file:", OUT_PATH)