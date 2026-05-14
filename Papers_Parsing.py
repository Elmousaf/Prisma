import re
import pandas as pd
from openpyxl.utils import get_column_letter

# -----------------------------
# Paths
# -----------------------------
PUBMED_PATH = "Pubmed1.txt"
SCOPUS_PATH = "Scopus.csv"
OUT_PATH = "AffichageArticlesTotal.xlsx"

# =============================
# 1️⃣ Load PubMed text
# =============================
with open(PUBMED_PATH, encoding="utf-8", errors="ignore") as f:
    pubmed_text = f.read()

# =============================
# 2️⃣ FIXED PubMed parser
# =============================
def parse_pubmed_records(text):
    recs = []
    seen_pmids = set()

    entries = re.split(r"\n\s*\d+\s*:\s*", text.strip())
    entries = [e.strip() for e in entries if e.strip()]

    print(f"🔎 Raw entries detected: {len(entries)}")

    for e in entries:
        body = " ".join(e.splitlines())

        # PMID (clé principale)
        pmid_match = re.search(r"PMID\s*[:\-]?\s*(\d+)", body, re.I)
        if not pmid_match:
            continue  # ❌ ignore faux bloc

        pmid = pmid_match.group(1)

        # ❌ éviter doublons
        if pmid in seen_pmids:
            continue
        seen_pmids.add(pmid)

        # TITLE
        title_match = re.search(r"Title\s*[:\-]\s*(.*?)(?:\.|$)", body, re.I)
        if title_match:
            title = title_match.group(1).strip()
        else:
            title = body.split(".")[0].strip()

        # DOI
        doi_match = re.search(r"\bdoi\s*[:\-]?\s*([^\s;]+)", body, re.I)
        doi = doi_match.group(1).rstrip(".") if doi_match else ""

        recs.append({
            "Database": "PubMed",
            "Title": title,
            "DOI": doi,
            "PMID": pmid
        })

    print(f"✅ Valid PubMed records: {len(recs)}")
    return recs

pubmed_recs = parse_pubmed_records(pubmed_text)

# =============================
# 3️⃣ Scopus CSV parser
# =============================
def parse_scopus_records(path):
    df = pd.read_csv(path)
    recs = []

    for _, row in df.iterrows():
        recs.append({
            "Database": "Scopus",
            "Title": str(row.get("Title", "")).strip(),
            "DOI": str(row.get("DOI", "")).strip(),
            "PMID": ""
        })

    return recs

scopus_recs = parse_scopus_records(SCOPUS_PATH)

# =============================
# 4️⃣ Merge
# =============================
all_recs = pubmed_recs + scopus_recs
df = pd.DataFrame(all_recs)

# =============================
# 5️⃣ PRISMA ID
# =============================
df.insert(0, "Record ID", [f"R{i+1:04d}" for i in range(len(df))])

# =============================
# 6️⃣ Screening fields
# =============================
for col in [
    "Stage (Title/Abstract/Full-text)",
    "Decision (Include/Exclude)",
    "Reason for Exclusion",
    "Notes"
]:
    df[col] = ""

# =============================
# 7️⃣ Summary
# =============================
counts = pd.DataFrame({
    "Database": ["PubMed", "Scopus", "Total"],
    "Records": [len(pubmed_recs), len(scopus_recs), len(all_recs)]
})

print("\n📊 FINAL COUNTS:")
print(f"  PubMed: {len(pubmed_recs)}")
print(f"  Scopus: {len(scopus_recs)}")
print(f"  Total: {len(all_recs)}")

# =============================
# 8️⃣ Export Excel
# =============================
with pd.ExcelWriter(OUT_PATH, engine="openpyxl") as writer:
    df.to_excel(writer, index=False, sheet_name="Screening")
    counts.to_excel(writer, index=False, sheet_name="Counts")

    for sheet_name in writer.sheets:
        ws = writer.sheets[sheet_name]
        for col in ws.columns:
            max_length = 0
            column = col[0].column_letter
            for cell in col:
                if cell.value:
                    max_length = max(max_length, len(str(cell.value)))
            ws.column_dimensions[column].width = min(max_length + 5, 100)

print("\n✅ Saved Excel file:", OUT_PATH)