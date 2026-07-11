data <- read.table("results/exon_counts_final.tsv", header=TRUE, sep="\t")

data$Short_ID <- sub("TCONS_000", "", data$Transcript)
cols <- ifelse(data$Gene == "Ano1", "steelblue", "orange")

png("results/figures/exon_counts_prioritised_Ano1_Ano8.png",
    width=1800, height=1100, res=300)

bp <- barplot(data$Exons,
              names.arg=data$Short_ID,
              col=cols,
              ylim=c(0, 32),
              main="Exon counts of prioritised Ano1 and Ano8 transcript isoforms",
              xlab="Candidate transcript",
              ylab="Number of exons")

text(bp, data$Exons + 1, labels=data$Exons, cex=0.8)

legend("topright",
       legend=c("Ano1", "Ano8"),
       fill=c("steelblue", "orange"),
       bty="n")

dev.off()
