# GEO validation analysis for Ano1 and Ano8
# Dataset: GSE20950

library(GEOquery)
library(hgu133plus2.db)
library(AnnotationDbi)

# Download GEO dataset
gset <- getGEO("GSE20950", GSEMatrix = TRUE, getGPL = FALSE)

# Extract expression matrix
expr <- exprs(gset[[1]])

# Get probe annotation
anno <- AnnotationDbi::select(
    hgu133plus2.db,
    keys = rownames(expr),
    columns = c("SYMBOL")
)

# Example: extract ANO1 and ANO8 probes
ano1_probes <- anno$SYMBOL == "ANO1"
ano8_probes <- anno$SYMBOL == "ANO8"

# NOTE:
# Further processing and statistical analysis performed as described in thesis.
