import matplotlib.pyplot as plt
import numpy as np

# ================= DATA =================
methods = [
    "Random Forest", "Support Vector Machine (SVM)", "K-Nearest Neighbors (KNN)",
    "Convolutional Neural Network (CNN)", "Logistic Regression", "Decision Tree",
    "Extreme Gradient Boosting (XGBoost)", "Long Short-Term Memory (LSTM)",
    "Naive Bayes", "Artificial Neural Network (ANN)", "Recurrent Neural Network (RNN)",
    "Multi-Layer Perceptron (MLP)", "Bidirectional LSTM (BiLSTM)",
    "Ensemble Voting", "Linear Regression", "RusBoost"
]

values = [18, 12, 11, 10, 9, 9, 7, 6, 4, 4, 3, 2, 2, 2, 1, 1]

total = sum(values)
percentages = [(v / total) * 100 for v in values]

# ================= FIGURE =================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 10))
fig.patch.set_facecolor("white")

# ================= TITLE =================
fig.suptitle(
    "Most Used Methods in Analyzed Articles",
    fontsize=22,
    fontweight='bold',
    color="#0B3C5D"  # bleu élégant
)

# ================= BAR CHART =================
y_pos = np.arange(len(methods))

bars = ax1.barh(y_pos, values, color="#4A90E2")  # bleu propre

ax1.set_yticks(y_pos)
ax1.set_yticklabels(methods, fontsize=9)
ax1.invert_yaxis()

ax1.set_title(
    "Number of Articles Using Each Method",
    fontsize=14,
    color="#0B3C5D"
)

# enlever bordures inutiles
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# valeurs
for i, v in enumerate(values):
    ax1.text(v + 0.3, i, str(v), va='center', fontsize=9)

# ================= TABLE =================
ax2.axis('off')

table_data = [
    [i + 1, methods[i], values[i], f"{percentages[i]:.2f}%"]
    for i in range(len(methods))
]

table = ax2.table(
    cellText=table_data,
    colLabels=["Rank"," Method","Articles" , "Percentage(%)"],
    cellLoc='left',
    colLoc='left',
    bbox=[0, 0, 1, 1]
)

# ================= STYLE TABLE =================
table.auto_set_font_size(False)
table.set_fontsize(10)

n_rows = len(table_data) + 1

for (row, col), cell in table.get_celld().items():
    cell.set_height(1 / n_rows)

    # HEADER
    if row == 0:
        cell.set_facecolor("#0B3C5D")
        cell.set_text_props(color="white", weight='bold')

    # LIGNES ALTERNÉES
    elif row % 2 == 0:
        cell.set_facecolor("#F4F8FB")

# ================= COLUMN WIDTH FIX =================
# élargir "Method", réduire chiffres
col_widths = [0.08, 0.55, 0.17, 0.20]

for i, width in enumerate(col_widths):
    for row in range(n_rows):
        table[(row, i)].set_width(width)

# ================= FOOTER =================
plt.figtext(
    0.5, 0.02,
    "Random Forest (18 articles) is the most used method, followed by SVM (12) and KNN (11). "
    "Average performance: Accuracy = 95.73% ; AUC = 79.62%",
    ha="center",
    fontsize=11,
    color="#333333"
)

plt.tight_layout(rect=[0, 0.05, 1, 0.95])
plt.show()