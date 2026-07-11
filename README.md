# Identification of Novel Chloride Channel Transcript Variants in White Fat Adipocytes

## Overview

This repository contains the computational workflow, analysis scripts, summary tables, and figures used to identify and prioritise novel chloride channel transcript variants in rat white fat adipocytes (WFA).

RNA-seq data from three WFA samples were analysed using transcriptome reconstruction and reference-guided transcript comparison.

## Analysis workflow

The main workflow consisted of:

1. RNA-seq read alignment using HISAT2
2. BAM processing using SAMtools
3. Reference-guided transcript assembly using StringTie
4. Transcript comparison and classification using GffCompare
5. Screening of chloride channel-associated transcripts
6. Candidate prioritisation using expression and transcript structure
7. Visualisation of prioritised transcript variants

Detailed workflow information is available in `docs/workflow.md`.

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
