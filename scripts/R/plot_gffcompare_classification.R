classification <- c(
  "Class j\nnovel isoforms",
  "Exact matches\n(=)",
  "Intergenic\n(u)",
  "Contained\n(c)",
  "Reference containment\n(k)",
  "Intronic\n(i)",
  "Opposite strand\n(x)"
)

count <- c(20686, 17071, 13038, 4269, 3480, 2616, 1623)

png("results/figures/gffcompare_transcript_classification.png",
    width = 2400, height = 1500, res = 300, type = "cairo")

par(mar = c(5, 10, 4, 2))

barplot(
  rev(count),
  names.arg = rev(classification),
  horiz = TRUE,
  las = 1,
  xlab = "Transcript count",
  main = "GffCompare transcript classification distribution"
)

dev.off()
