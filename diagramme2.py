import matplotlib.pyplot as plt
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import requests
from PIL import Image
from io import BytesIO

# -----------------------------
# DATA
# -----------------------------
data = {
    "Other (Private / Not Mentioned)": 14,
    "Cleveland (UCI)": 14,
    "Kaggle": 6,
    "MIT-BIH": 5,
    "Framingham": 4,
    "PhysioNet": 2,
    "SHHS": 1,
    "PPG-BP": 1,
    "MIMIC-III": 1,
    "NHANES": 1,
    "UK Biobank": 1
}

# -----------------------------
# LOGO URLs (you can change)
# -----------------------------
logos = {
    "Kaggle": "https://upload.wikimedia.org/wikipedia/commons/7/7c/Kaggle_logo.png",
    "PhysioNet": "https://physionet.org/static/pn-logo.png",
    "MIT-BIH": "https://upload.wikimedia.org/wikipedia/commons/0/0c/MIT_logo.svg",
    "UCI": "https://upload.wikimedia.org/wikipedia/commons/6/6e/University_of_California%2C_Irvine_seal.svg",
    "UK Biobank": "https://upload.wikimedia.org/wikipedia/en/1/1e/UK_Biobank_logo.png"
}

# -----------------------------
# SORT DATA
# -----------------------------
data = dict(sorted(data.items(), key=lambda x: x[1], reverse=True))
names = list(data.keys())
values = list(data.values())

# -----------------------------
# FUNCTION: LOAD IMAGE FROM URL
# -----------------------------
def load_image(url):
    try:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        return img
    except:
        return None

# -----------------------------
# FIGURE
# -----------------------------
fig, ax = plt.subplots(figsize=(16, 9))
ax.set_facecolor('#f5f7fb')

# Colors
colors = plt.cm.plasma(np.linspace(0.2, 0.9, len(names)))

# Bars
bars = ax.barh(names, values, color=colors)
ax.invert_yaxis()

# -----------------------------
# ADD VALUES
# -----------------------------
for bar in bars:
    width = bar.get_width()
    ax.text(width + 0.2,
            bar.get_y() + bar.get_height()/2,
            f'{int(width)}',
            va='center',
            fontsize=12,
            fontweight='bold')

# -----------------------------
# ADD LOGOS
# -----------------------------
for i, name in enumerate(names):
    for key in logos:
        if key.lower() in name.lower():
            img = load_image(logos[key])
            if img:
                imagebox = OffsetImage(img, zoom=0.05)
                ab = AnnotationBbox(
                    imagebox,
                    (0, i),
                    xybox=(-40, 0),
                    frameon=False,
                    xycoords='data',
                    boxcoords="offset points",
                    pad=0
                )
                ax.add_artist(ab)

# -----------------------------
# STYLE
# -----------------------------
ax.set_title("Most Used Databases in Reviewed Articles",
             fontsize=22, weight='bold')

ax.set_xlabel("Number of Articles", fontsize=14)

for spine in ['top', 'right', 'left']:
    ax.spines[spine].set_visible(False)

ax.xaxis.grid(True, linestyle='--', alpha=0.3)

# -----------------------------
# SAVE
# -----------------------------
plt.tight_layout()
plt.savefig("databases_with_logos.png", dpi=300, bbox_inches='tight')
plt.show()