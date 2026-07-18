import csv
import math
from pathlib import Path
from collections import defaultdict
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
repo_root = Path(__file__).resolve().parents[2]
table_path = repo_root / "results" / "tables" / "candidate_TPM_table.tsv"
figure_path = repo_root / "results" / "figures" / "final_candidate_TPM_expression_log.png"

data = defaultdict(list)

with table_path.open() as f:
    reader = csv.DictReader(f, delimiter="\t")
    for row in reader:
        transcript = row["Transcript"]
        tpm = float(row["TPM"])
        data[transcript].append(tpm)

# Keep grouped by gene, consistent with exon figure
order = [
    "TCONS_00004856",
    "TCONS_00004858",
    "TCONS_00008054",
    "TCONS_00004857",
    "TCONS_00008053",
    "TCONS_00026006",
    "TCONS_00026007",
    "TCONS_00025093",
]

genes = {
    "TCONS_00004856": "Ano1",
    "TCONS_00004857": "Ano1",
    "TCONS_00004858": "Ano1",
    "TCONS_00008053": "Ano1",
    "TCONS_00008054": "Ano1",
    "TCONS_00025093": "Ano8",
    "TCONS_00026006": "Ano8",
    "TCONS_00026007": "Ano8",
}

labels = [t.replace("TCONS_000", "") for t in order]

mean_tpm = []
log_values = []

for t in order:
    values = data[t]
    mean = sum(values) / len(values)
    mean_tpm.append(mean)
    log_values.append(math.log10(mean + 1))

colors = ["steelblue" if genes[t] == "Ano1" else "darkorange" for t in order]

plt.figure(figsize=(9, 5))

bars = plt.bar(
    labels,
    log_values,
    color=colors,
    edgecolor="black",
    linewidth=0.8
)

plt.ylabel("log10(mean TPM + 1)", fontsize=13)
plt.xlabel("Transcript ID", fontsize=13)
plt.title(
    r"Expression levels of prioritised $\it{Ano1}$ and $\it{Ano8}$ transcript isoforms",
    fontsize=14,
    fontweight="bold",
    pad=15
)


plt.xticks(fontsize=11)
plt.yticks(fontsize=11)

# Label bars with original mean TPM values
for bar, mean in zip(bars, mean_tpm):
    h = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        h + 0.05,
        f"{mean:.1f}",
        ha="center",
        va="bottom",
        fontsize=10
    )

legend = [
    Patch(facecolor="steelblue", edgecolor="black", label=r"$\it{Ano1}$"),
    Patch(facecolor="darkorange", edgecolor="black", label=r"$\it{Ano8}$")
]

plt.legend(handles=legend, frameon=False, fontsize=12, loc="upper right")

ax = plt.gca()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.savefig(figure_path, dpi=600)
plt.close()
