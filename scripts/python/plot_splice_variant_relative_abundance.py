import csv
from collections import defaultdict
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

repo_root = Path(__file__).resolve().parents[2]
table_path = repo_root / "results" / "tables" / "candidate_TPM_table.tsv"
figure_path = repo_root / "results" / "figures" / "splice_variant_relative_abundance_stacked.png"

# Calculate relative abundance from mean TPM values.
display_order = {
    "Ano1": [
        "TCONS_00004856",
        "TCONS_00004858",
        "TCONS_00008054",
        "TCONS_00004857",
        "TCONS_00008053",
    ],
    "Ano8": [
        "TCONS_00026006",
        "TCONS_00026007",
        "TCONS_00025093",
    ],
}

transcript_genes = {
    transcript: gene
    for gene, transcripts in display_order.items()
    for transcript in transcripts
}

tpm_values = defaultdict(list)
with table_path.open() as handle:
    reader = csv.DictReader(handle, delimiter="\t")
    for row in reader:
        transcript = row["Transcript"]
        if transcript in transcript_genes:
            tpm_values[transcript].append(float(row["TPM"]))

missing = [
    transcript
    for transcript in transcript_genes
    if transcript not in tpm_values
]
if missing:
    raise ValueError("No TPM values found for: " + ", ".join(sorted(missing)))

mean_tpm = {
    transcript: sum(values) / len(values)
    for transcript, values in tpm_values.items()
}

data = {}
for gene, transcripts in display_order.items():
    total = sum(mean_tpm[transcript] for transcript in transcripts)
    data[gene] = [
        (
            transcript.replace("TCONS_000", ""),
            100 * mean_tpm[transcript] / total,
        )
        for transcript in transcripts
    ]


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

        # Label segments that are wide enough to remain readable.
        if value >= 5:
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
plt.savefig(figure_path, dpi=600)
plt.savefig(figure_path.with_suffix(".pdf"))
plt.close()
