data <- read.table(
  "results/tables/gene_isoform_counts.tsv",
  header = TRUE
)

gene <- data$Gene
count <- data$Count

png(
  "results/figures/chloride_gene_distribution_polished.png",
  width = 2600,
  height = 1700,
  res = 300,
  type = "cairo"
)

par(mar = c(5, 14, 4, 3))

bp <- barplot(
  rev(count),
  names.arg = rev(gene),
  horiz = TRUE,
  las = 1,
  col = "steelblue",
  border = "black",
  xlab = "Number of novel isoforms",
  main = "Novel chloride-related isoforms identified in candidate genes",
  xlim = c(0, 7)
)

text(
  x = rev(count) + 0.2,
  y = bp,
  labels = rev(count),
  cex = 0.8
)

dev.off()
