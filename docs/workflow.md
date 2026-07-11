# RNA-seq Analysis Workflow

## Project aim

This workflow was developed to identify and prioritise novel chloride channel transcript variants in rat white fat adipocytes (WFA).

## 1. RNA-seq alignment

Paired-end RNA-seq reads from three WFA samples were aligned to the Rattus norvegicus Rnor_6.0 reference genome using HISAT2.

SAM alignment files were converted to BAM format, sorted, and indexed using SAMtools.

## 2. Transcript assembly

Transcript structures were reconstructed independently for each sample using StringTie with the Ensembl Rnor_6.0.95 gene annotation as the reference.

## 3. Transcript comparison

The three StringTie transcript assemblies were compared with the reference annotation using GffCompare.

The final comparison used:

- sample1.fixed.gtf
- sample2.gtf
- sample3.gtf

Novel splice variants were identified primarily using GffCompare class code `j`, representing potentially novel isoforms sharing at least one splice junction with a reference transcript.

## 4. Chloride channel candidate screening

Reconstructed transcripts associated with chloride channel-related genes were screened and prioritised.

Candidate assessment included:

- GffCompare transcript classification
- transcript abundance (TPM)
- exon structure
- splice-variant complexity
- relative isoform abundance
- candidate gene distribution

## 5. Candidate prioritisation

High-confidence candidates were prioritised based on transcript structure and expression evidence.

The final prioritised candidates were associated primarily with Ano1 and Ano8.

## 6. Visualisation

Python and R scripts were used to generate figures describing:

- chloride channel gene distribution
- GffCompare transcript classification
- candidate transcript TPM expression
- exon counts
- relative splice-variant abundance

## Software

The main software used in the workflow included:

- HISAT2
- SAMtools
- StringTie
- GffCompare
- Python
- R

Analysis was performed on the University of Nottingham Ada HPC cluster using SLURM.
