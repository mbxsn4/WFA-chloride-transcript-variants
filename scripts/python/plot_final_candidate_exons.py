import matplotlib.pyplot as plt
from matplotlib.patches import Patch

labels = ["04856", "08054", "04858", "04857", "08053", "26007", "25093", "26006"]
exons = [19, 15, 7, 2, 2, 4, 4, 1]
colors = ["steelblue"]*5 + ["darkorange"]*3

plt.figure(figsize=(10, 5))
bars = plt.bar(labels, exons, color=colors, edgecolor="black", linewidth=0.8)

plt.ylabel("Number of exons", fontsize=13)
plt.xlabel("Candidate transcript", fontsize=13)
plt.title("Exon counts of prioritised Ano1 and Ano8 transcript isoforms", fontsize=15, weight="bold")

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 0.3, str(int(height)), ha="center", fontsize=11)

legend_elements = [
    Patch(facecolor="steelblue", edgecolor="black", label="Ano1"),
    Patch(facecolor="darkorange", edgecolor="black", label="Ano8")
]
plt.legend(handles=legend_elements, frameon=False)

plt.tight_layout()
plt.savefig("final_candidate_exon_counts_polished.png", dpi=600)
plt.savefig("final_candidate_exon_counts_polished.pdf")
plt.close()
