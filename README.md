# Identification of Novel Chloride Channel Transcript Variants in White Fat Adipocytes

- **Author:** Sahar Naeemi
- **Programme:** Bioinformatics MSc
- **Institution:** University of Nottingham
- **Submission date:** July 2026

## Overview

This repository contains the computational workflow, analysis scripts, metadata, summary tables, and figures used to identify and prioritise novel chloride-channel transcript variants in rat white fat adipocytes (WFA).

RNA sequencing (RNA-seq) data from three independent WFA samples were analysed using reference-guided transcriptome reconstruction with StringTie followed by transcript comparison using GffCompare. Novel chloride-channel-associated transcript variants were subsequently prioritised by integrating transcript classification, transcript structure, expression evidence, reproducibility across samples, and protein-domain annotation.

The principal output of the workflow is the high-confidence candidate table:

`results/tables/final_prioritised_candidates.tsv`

which summarises the eight prioritised *Ano1* and *Ano8* transcript isoforms together with their genomic span, exon count, mean TPM, relative abundance, and PF04547 anoctamin-domain evidence.

The broader reproducible chloride-related candidate set retained before final *Ano1*/*Ano8* prioritisation is provided in:

`results/tables/reproducible_chloride_candidates.tsv`


## Analysis workflow

The main workflow consisted of:

1. RNA-seq read alignment using HISAT2
2. BAM processing using SAMtools
3. Reference-guided transcript assembly using StringTie
4. Transcript comparison and classification using GffCompare
5. Screening of chloride channel-associated transcripts
6. Candidate prioritisation using GffCompare classification, transcript structure, transcript abundance, reproducibility across WFA samples, and protein-domain annotation
7. Visualisation of prioritised transcript variants

Detailed workflow information is available in `docs/workflow.md`.

### Analysis provenance

Global merged-assembly and transcript-classification statistics, including 87,185 consensus transcripts and 28,787 class-j transcripts, were obtained from the corrected `WFA_compare_final` run using `sample1.fixed.gtf`, `sample2.gtf`, and `sample3.gtf`.

The eight prioritised *Ano1* and *Ano8* candidate identifiers and their downstream structural, expression, domain, and IGV analyses were derived from the earlier `WFA_compare_all3` candidate-discovery run using `sample1.gtf`, `sample2.gtf`, and `sample3.gtf`. GffCompare `TCONS_` identifiers are run-specific and should be interpreted using the corresponding source GTF.

## Input data

Raw FASTQ files, alignment files, and reference files are not included in this repository because of their size. The paths in `metadata/samples.tsv` describe a standardised `raw_fastq/` staging layout for the three WFA samples. The SLURM scripts retain the original Ada HPC paths used during the analysis, including the separate source directories used for Samples 2 and 3.

FastQC and Trimmomatic preprocessing are documented in the dissertation, but the original preprocessing commands and logs were not retained. The scripts in this repository reproduce the workflow from HISAT2 alignment onward.O

## Repository structure

```text
WFA-chloride-transcript-variants/
|-- metadata/
|   `-- samples.tsv
|-- scripts/
|   |-- slurm/
|   |-- python/
|   `-- R/
|-- results/
|   |-- tables/
|   `-- figures/
|-- docs/
|   `-- workflow.md
|-- requirements.txt
|-- .gitignore
`-- README.md
```

## Software requirements

The analysis used the following principal software:

- Python 3.11.3
- Matplotlib 3.7.2
- FastQC 0.11.9
- Trimmomatic 0.39
- HISAT2 2.2.1
- SAMtools 1.22.1
- StringTie 2.2.1
- HMMER 3.4
- GffCompare 0.12.10
- GffRead 0.12.7
- TransDecoder 5.7.1
- IGV 2.16.0
- R 4.4.2


Install the Python plotting dependency with:

```bash
python -m pip install -r requirements.txt
```

On the Ada HPC cluster, the R plotting scripts can be run after loading R with:

```bash
module load R-uoneasy/4.4.2-gfbf-2024a
```

## Reproducing figures

From the repository root, the relative-abundance figure can be regenerated with:

```bash
python scripts/python/plot_splice_variant_relative_abundance.py
```

This reads `results/tables/candidate_TPM_table.tsv` and generates:

- `results/figures/splice_variant_relative_abundance_stacked.png`
- `results/figures/splice_variant_relative_abundance_stacked.pdf`

The R-based summary figures can be regenerated with:

```bash
Rscript scripts/R/plot_chloride_gene_distribution.R
Rscript scripts/R/plot_gffcompare_classification.R
```

These scripts write:

- `results/figures/chloride_gene_distribution_polished.png`
- `results/figures/gffcompare_transcript_classification.png`

The relative abundance of each prioritised transcript is calculated from its mean transcripts per million (TPM) across the available samples within its gene.

## Further documentation

See `docs/workflow.md` for the full analysis outline, `docs/research_log.md` for the project development and troubleshooting record, and `metadata/samples.tsv` for sample metadata.

## External GEO Validation

External validation of candidate genes (*Ano1* and *Ano8*) was performed using a publicly available adipose tissue dataset from the Gene Expression Omnibus (GEO):

- **Accession:** GSE20950
- **Platform:** GPL570 (Affymetrix Human Genome U133 Plus 2.0 Array)
- **Samples:** 39
- **Conditions:** Insulin-sensitive vs insulin-resistant human adipose tissue

The dataset was downloaded using the `GEOquery` package in R.

A minimal reproducible script is provided in:

`scripts/R/geo_validation.R`

Statistical analysis was performed using Welch's t-test, and visualisation was carried out using `ggplot2`.
