import csv
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Patch


repo_root = Path(__file__).resolve().parents[2]
table_path = repo_root / "results" / "tables" / "exon_counts_final.tsv"
figure_dir = repo_root / "results" / "figures"

with table_path.open() as handle:
    reader = csv.DictReader(handle, delimiter="\t")
    data = [
        {
            "Gene": row["Gene"],
            "Transcript": row["Transcript"],
            "Exons": int(row["Exons"]),
        }
        for row in reader
    ]

gene_order = {"Ano1": 0, "Ano8": 1}
data.sort(key=lambda row: (gene_order[row["Gene"]], -row["Exons"]))

labels = [row["Transcript"].replace("TCONS_000", "") for row in data]
exons = [row["Exons"] for row in data]
colors = [
    "steelblue" if row["Gene"] == "Ano1" else "darkorange"
    for row in data
]

plt.figure(figsize=(10, 5))
bars = plt.bar(
    labels,
    exons,
    color=colors,
    edgecolor="black",
    linewidth=0.8,
)

plt.ylabel("Number of exons", fontsize=13)
plt.xlabel("Candidate transcript", fontsize=13)
plt.title(
    "Exon counts of prioritised Ano1 and Ano8 transcript isoforms",
    fontsize=15,
    weight="bold",
)

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height + 0.3,
        str(int(height)),
        ha="center",
        fontsize=11,
    )

legend_elements = [
    Patch(facecolor="steelblue", edgecolor="black", label="Ano1"),
    Patch(facecolor="darkorange", edgecolor="black", label="Ano8"),
]
plt.legend(handles=legend_elements, frameon=False)

plt.tight_layout()
plt.savefig(
    figure_dir / "final_candidate_exon_counts_polished.png",
    dpi=600,
)

plt.close()
