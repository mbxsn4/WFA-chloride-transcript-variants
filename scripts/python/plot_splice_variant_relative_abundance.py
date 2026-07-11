import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# Relative abundance values calculated from mean TPM
data = {
    "Ano1": [
        ("04856", 55.63),
        ("04858", 41.74),
        ("08054", 1.72),
        ("04857", 0.56),
        ("08053", 0.36),
    ],
    "Ano8": [
        ("26006", 52.92),
        ("26007", 36.31),
        ("25093", 10.77),
    ],
}

colors = {
    "04856": "#1f4e79",
    "04858": "#5b9bd5",
    "08054": "#9dc3e6",
    "04857": "#bdd7ee",
    "08053": "#d9eaf7",
    "26006": "#c55a11",
    "26007": "#ed7d31",
    "25093": "#f4b183",
}

fig, ax = plt.subplots(figsize=(9, 3.8))

y_positions = [1, 0]
genes = ["Ano1", "Ano8"]

for y, gene in zip(y_positions, genes):
    left = 0
    for transcript, value in data[gene]:
        ax.barh(
            y,
            value,
            left=left,
            height=0.42,
            color=colors[transcript],
            edgecolor="white",
            linewidth=1.2,
        )

        # Label large segments inside the bar
        if value >= 8:
            ax.text(
                left + value / 2,
                y,
                f"{transcript}\n{value:.1f}%",
                ha="center",
                va="center",
                fontsize=10,
                color="black",
                fontweight="bold",
            )
        else:
            # Label small segments just above the bar
            ax.text(
                left + value / 2,
                y + 0.33,
                f"{transcript}\n{value:.1f}%",
                ha="center",
                va="bottom",
                fontsize=8,
                color="black",
            )

        left += value

ax.set_xlim(0, 100)
ax.set_yticks(y_positions)
ax.set_yticklabels([r"$\it{Ano1}$", r"$\it{Ano8}$"], fontsize=13)
ax.set_xlabel("Relative abundance of prioritised splice variants (%)", fontsize=12)
ax.set_title(
    "Relative abundance of prioritised splice variants",
    fontsize=14,
    fontweight="bold",
    pad=15,
)

ax.set_xticks([0, 25, 50, 75, 100])
ax.tick_params(axis="x", labelsize=11)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.tick_params(axis="y", length=0)

# Add a clean legend
legend_elements = []
for gene in genes:
    for transcript, value in data[gene]:
        legend_elements.append(
            Patch(facecolor=colors[transcript], edgecolor="white", label=transcript)
        )

ax.legend(
    handles=legend_elements,
    title="Transcript ID",
    bbox_to_anchor=(1.02, 1),
    loc="upper left",
    frameon=False,
    fontsize=9,
    title_fontsize=10,
)

plt.tight_layout()
plt.savefig("splice_variant_relative_abundance_stacked.png", dpi=600)
plt.savefig("splice_variant_relative_abundance_stacked.pdf")
plt.close()
