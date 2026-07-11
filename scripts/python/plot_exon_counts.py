import matplotlib.pyplot as plt
from matplotlib.patches import Patch

genes = ["Ano1","Ano1","Ano1","Ano1","Ano1","Ano8","Ano8","Ano8"]
transcripts = [
    "00004856","00004857","00004858","00008054","00008053",
    "00026007","00025093","00026006"
]
exons = [26,27,28,27,26,17,16,15]

colors = ["steelblue" if g == "Ano1" else "orange" for g in genes]

plt.figure(figsize=(8,4.5))
bars = plt.bar(transcripts, exons, color=colors)

plt.title("Exon counts of prioritised Ano1 and Ano8 transcript isoforms")
plt.xlabel("Candidate transcript")
plt.ylabel("Number of exons")

for bar, value in zip(bars, exons):
    plt.text(
        bar.get_x() + bar.get_width()/2,
        value + 0.3,
        str(value),
        ha="center",
        va="bottom",
        fontsize=9
    )

legend_elements = [
    Patch(facecolor="steelblue", label="Ano1"),
    Patch(facecolor="orange", label="Ano8")
]
plt.legend(handles=legend_elements, frameon=False)

plt.tight_layout()
plt.savefig("results/figures/exon_counts_prioritised_Ano1_Ano8.png", dpi=300)
plt.savefig("results/figures/exon_counts_prioritised_Ano1_Ano8.pdf")
print("Saved:")
print("results/figures/exon_counts_prioritised_Ano1_Ano8.png")
print("results/figures/exon_counts_prioritised_Ano1_Ano8.pdf")
