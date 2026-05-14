import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_prisma_final():
    # Figure large et haute pour une aération maximale
    fig, ax = plt.subplots(figsize=(11, 14))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # --- CONFIGURATION DES STYLES ---
    # Style pour les étiquettes de gauche (Phases)
    phase_style = dict(boxstyle="round,pad=0.5", lw=0)
    # Style pour les boîtes de contenu (Détails)
    content_style = dict(boxstyle="round,pad=0.6", fc="white", ec="#2c3e50", lw=1.2)
    
    # --- 1. IDENTIFICATION ---
    # Phase (Gauche)
    ax.add_patch(patches.FancyBboxPatch((5, 82), 18, 10, fc="#1a237e", **phase_style))
    plt.text(14, 87, "IDENTIFICATION", color='white', weight='bold', ha='center', fontsize=9)
    
    # Contenu (Droite)
    ax.add_patch(patches.FancyBboxPatch((30, 82), 65, 10, **content_style))
    plt.text(32, 88, "Sources: PubMed (192), Scopus (749), Other (3)", weight='bold', fontsize=10)
    plt.text(32, 84, "Total records identified: n = 941", fontsize=11, color='#1a237e', weight='bold')

    # --- 2. SCREENING ---
    # Phase (Gauche)
    ax.add_patch(patches.FancyBboxPatch((5, 68), 18, 10, fc="#1565c0", **phase_style))
    plt.text(14, 73, "SCREENING", color='white', weight='bold', ha='center', fontsize=9)
    
    # Contenu (Droite)
    ax.add_patch(patches.FancyBboxPatch((30, 68), 65, 10, **content_style))
    plt.text(32, 74, "Duplicates removed automatically (Python script): n = 123", fontsize=10)
    plt.text(32, 70, "Unique records to screen: n = 818", fontsize=11, color='#1565c0', weight='bold')

    # --- 3. ELIGIBILITY ---
    # Phase (Gauche)
    ax.add_patch(patches.FancyBboxPatch((5, 38), 18, 24, fc="#ef6c00", **phase_style))
    plt.text(14, 50, "ELIGIBILITY", color='white', weight='bold', ha='center', fontsize=9)
    
    # Contenu (Droite)
    ax.add_patch(patches.FancyBboxPatch((30, 38), 65, 24, **content_style))
    plt.text(62.5, 58, "Selection Criteria Assessment", weight='bold', fontsize=11, ha='center')
    
    # Texte Exclusion simplifié (Aéré avec linespacing)
    plt.text(32, 53, "Excluded (n=730)", weight='bold', color='#c62828', fontsize=9)
    plt.text(32, 41, "• Animal/Pediatric: 69\n• Non-clinical IoT: 165\n• Reviews: 29\n• Irrelevant domains: 467", fontsize=9, linespacing=1.8)

    # Texte Inclusion simplifié
    plt.text(65, 53, "Inclusion", weight='bold', color='#2e7d32', fontsize=9)
    plt.text(65, 43, "• Cardiovascular focus\n• AI/ML methods\n• Clinical monitoring\n• Last 10 years", fontsize=9, linespacing=1.8)

    # --- 4. TRANSITION (88 ARTICLES) ---
    ax.add_patch(patches.FancyBboxPatch((30, 28), 65, 6, boxstyle="round,pad=0.3", fc="#fdfefe", ec="#7f8c8d", ls='--'))
    plt.text(62.5, 31, "Full-text articles assessed for eligibility: n = 88", weight='bold', ha='center', fontsize=10)

    # --- 5. INCLUDED ---
    # Phase (Gauche)
    ax.add_patch(patches.FancyBboxPatch((5, 10), 18, 14, fc="#4a148c", **phase_style))
    plt.text(14, 17, "INCLUDED", color='white', weight='bold', ha='center', fontsize=9)
    
    # Résultat Final (Droite)
    ax.add_patch(patches.FancyBboxPatch((30, 10), 65, 14, fc="#4a148c", boxstyle="round,pad=0.4"))
    plt.text(62.5, 19, "FINAL CORPUS FOR SYSTEMATIC REVIEW", color='white', weight='bold', ha='center', fontsize=11)
    plt.text(62.5, 13, "n = 42 (39 from databases + 3 from other sources)", color='white', weight='bold', ha='center', fontsize=14)

    # --- FLÈCHES ---
    arrow_props = dict(arrowstyle='->', color='#b0bec5', lw=2)
    plt.annotate('', xy=(62.5, 78), xytext=(62.5, 82), arrowprops=arrow_props)
    plt.annotate('', xy=(62.5, 62), xytext=(62.5, 68), arrowprops=arrow_props)
    plt.annotate('', xy=(62.5, 34), xytext=(62.5, 38), arrowprops=arrow_props)
    plt.annotate('', xy=(62.5, 24), xytext=(62.5, 28), arrowprops=arrow_props)

    plt.show()

if __name__ == "__main__":
    draw_prisma_final()