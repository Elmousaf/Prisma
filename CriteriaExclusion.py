import pandas as pd
import re

# -----------------------------
# Charger le fichier Excel
# -----------------------------
df = pd.read_excel("duplicates_report_by_doi.xlsx")

# Ne garder que les non-doublons
if "IsDuplicate" in df.columns:
    df = df[df["IsDuplicate"] == False].copy()

print("Non-duplicate records:", len(df))

# -----------------------------
# Normalisation
# -----------------------------
def norm(s):
    return re.sub(r"\s+", " ", str(s).lower()).strip()

# -----------------------------
# Mots-clés
# -----------------------------
CARDIO = [
    "cardiovascular", "heart disease", "hypertension", "cardiac",
    "heart failure", "arrhythmia", "coronary artery", "cvd", "heart attack"
]

AI = [
    "machine learning", "deep learning", "deep-neural", "neural", "cnn", "rnn",
    "classification", "predictive model", "decision support", "risk prediction",
    "regression", "model", "algorithm", "svm", "random forest", "xgboost", "bayesian"
]

MONITORING = [
    "monitoring", "telemedicine", "mobile app", "web app",
    "remote follow-up", "patient monitoring", "digital health"
]

ANIMAL = ["mouse", "mice", "rat", "murine", "zebrafish", "primate model"]
HUMAN = ["human", "adult", "patient", "patients"]

# -----------------------------
# Fonctions utilitaires
# -----------------------------
def contains_any(text, kws):
    text = norm(text)
    return any(k in text for k in kws)

# -----------------------------
# Scoring robuste (TOUJOURS retourne une valeur)
# -----------------------------
def score_record(title, abstract=None):
    t = norm(title)
    a = norm(abstract) if abstract else ""
    full_text = t + " " + a

    # ⚠️ Cas vide → éviter ligne perdue
    if not full_text.strip():
        return "Exclude", "Empty record", 1

    # Exclusion animaux
    if contains_any(full_text, ANIMAL):
        return "Exclude", "Animal study", 1

    score = 0
    reasons = []

    # Cardio
    if contains_any(full_text, CARDIO):
        score += 2
        reasons.append("cardio")

    # IA
    if contains_any(full_text, AI):
        score += 2
        reasons.append("AI/ML")

    # Monitoring
    if contains_any(full_text, MONITORING):
        score += 0.5
        reasons.append("monitoring")

    # Human
    if contains_any(full_text, HUMAN):
        score += 0.5
        reasons.append("human")

    # Limiter à 5
    score = min(score, 5)

    # Décision (TOUJOURS définie)
    if score > 4:
        decision = "Include"
    elif score == 4:
        decision = "Maybe"
    else:
        decision = "Exclude"

    return decision, ", ".join(reasons) if reasons else "No keywords", score

# -----------------------------
# Appliquer scoring
# -----------------------------
out = df.copy()

if "Abstract" in df.columns:
    out[["Decision", "Reason", "Score"]] = out.apply(
        lambda x: pd.Series(score_record(x["Title"], x["Abstract"])), axis=1
    )
else:
    out[["Decision", "Reason", "Score"]] = out["Title"].apply(
        lambda x: pd.Series(score_record(x))
    )

# -----------------------------
#  FIX CRUCIAL : remplacer les NaN
# -----------------------------
out["Decision"] = out["Decision"].fillna("Exclude")

# -----------------------------
# Vérification TOTALE
# -----------------------------
total_records = len(out)

counts = out["Decision"].value_counts()

include_count = counts.get("Include", 0)
maybe_count = counts.get("Maybe", 0)
exclude_count = counts.get("Exclude", 0)

print("\n===== FINAL COUNTS =====")
print(f"Include : {include_count}")
print(f"Maybe   : {maybe_count}")
print(f"Exclude : {exclude_count}")
print("------------------------")
print(f"TOTAL   : {include_count + maybe_count + exclude_count}")
print(f"EXPECTED: {total_records}")

# Vérification automatique
if (include_count + maybe_count + exclude_count) != total_records:
    print("⚠️ ERREUR : mismatch détecté !")
else:
    print("✅ Comptage correct")

# -----------------------------
# Sauvegarde
# -----------------------------
out.to_excel("ExclusionCriteres_Final.xlsx", index=False)

print("\nSaved: ExclusionCriteres_Final.xlsx")