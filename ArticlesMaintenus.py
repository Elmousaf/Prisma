import pandas as pd

# -----------------------------
# Charger le fichier Excel
# -----------------------------
INPUT_FILE = "ExclusionCriteres_Final.xlsx"
OUTPUT_FILE = "Articles_Maintenus.xlsx"

df = pd.read_excel(INPUT_FILE)

print("Total initial:", len(df))

# -----------------------------
# Vérifier colonne Score
# -----------------------------
if "Score" not in df.columns:
    raise ValueError("❌ La colonne 'Score' est introuvable")

# -----------------------------
# Ajouter colonne Approved
# -----------------------------
def approval(score):
    if score >= 3:
        return "Oui"
    else:
        return "Non"

df["Approved"] = df["Score"].apply(approval)

# -----------------------------
# Filtrer uniquement Score >= 3
# -----------------------------
filtered_df = df[df["Score"] >= 3].copy()

print("Après filtrage (Score >= 3):", len(filtered_df))

# -----------------------------
# Statistiques
# -----------------------------
print("\n===== STATS =====")
print(filtered_df["Approved"].value_counts())

# -----------------------------
# Vérification cohérence
# -----------------------------
print("\nTOTAL FINAL:", len(filtered_df))

# -----------------------------
# Sauvegarde
# -----------------------------
filtered_df.to_excel(OUTPUT_FILE, index=False)

print("\n✅ Fichier sauvegardé:", OUTPUT_FILE)