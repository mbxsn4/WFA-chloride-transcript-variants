# Identification of Novel Chloride Channel Transcript Variants in White Fat Adipocytes

## Overview

This repository contains the computational workflow, analysis scripts, metadata, summary tables, and figures used to identify and prioritise novel chloride-channel transcript variants in rat white fat adipocytes (WFA).

RNA-seq data from three independent WFA samples were analysed using reference-guided transcriptome reconstruction with StringTie followed by transcript comparison using GffCompare. Novel chloride-channel-associated transcript variants were subsequently prioritised by integrating transcript classification, transcript structure, expression evidence, reproducibility across samples, and protein-domain annotation.

The principal output of the workflow is the high-confidence candidate table:

`results/tables/final_high_confidence_candidates.tsv`

which summarises the prioritised novel transcript variants together with supporting evidence, including reproducibility status and biological-family annotation.

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
## Input data

Raw FASTQ files, alignment files, and reference files are not included in this repository because of their size. The paths in `metadata/samples.tsv` describe a standardised `raw_fastq/` staging layout for the three WFA samples. The SLURM scripts retain the original Ada HPC paths used during the analysis, including the separate source directories used for Samples 2 and 3.

## Repository structure

```text
WFA_chloride_GitHub/
├── metadata/
│   └── samples.tsv
├── scripts/
│   ├── slurm/
│   ├── python/
│   └── R/
├── results/
│   ├── tables/
│   └── figures/
├── docs/
│   └── workflow.md
├── .gitignore
└── README.md
