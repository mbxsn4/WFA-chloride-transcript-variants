# RNA-seq Analysis Workflow

## Project aim

This workflow was developed to identify and prioritise novel chloride channel transcript variants in rat white fat adipocytes (WFA).

## 0. Upstream quality control and preprocessing

The dissertation records initial read-quality assessment with FastQC 0.11.9 and adapter/quality trimming with Trimmomatic 0.39. The original preprocessing command scripts and logs were not retained in this repository.

The provided SLURM workflow begins from paired FASTQ files staged under `raw_fastq/` and reproduces the analysis from HISAT2 alignment onward.

## 1. RNA-seq alignment

Paired-end RNA-seq reads from three WFA samples were aligned to the Rattus norvegicus Rnor_6.0 reference genome using HISAT2.

SAM alignment files were converted to BAM format, sorted, and indexed using SAMtools.

## 2. Transcript assembly

Transcript structures were reconstructed independently for each sample using StringTie with the Ensembl Rnor_6.0.95 gene annotation as the reference.

## 3. Transcript comparison

Two GffCompare runs underpin the reported outputs.

The corrected summary run, `WFA_compare_final`, used:

- `sample1.fixed.gtf`
- `sample2.gtf`
- `sample3.gtf`

This run generated the global merged-assembly and transcript-classification statistics reported in the dissertation, including 87,185 consensus transcripts and 28,787 class-j transcripts.

The candidate-discovery run, `WFA_compare_all3`, used:

- `sample1.gtf`
- `sample2.gtf`
- `sample3.gtf`

The eight prioritised *Ano1* and *Ano8* candidate identifiers and their downstream analyses were derived from this candidate-discovery run. GffCompare `TCONS_` identifiers are run-specific and must be interpreted using the corresponding combined GTF.

Novel splice variants were identified using GffCompare class code `j`, representing potentially novel isoforms sharing at least one splice junction with a reference transcript.

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

Filtering the candidate-discovery run identified 64 chloride-related class-j transcripts across 22 genes.

The corrected gene-family summary, which sums to all 64 candidate isoforms, is provided in:

`results/tables/gene_family_candidate_counts.tsv`

Reproducibility was assessed using the GffCompare tracking output. Novel isoforms detected in at least two samples (`num_samples >= 2`) were retained in the broader reproducible candidate set:

`results/tables/reproducible_chloride_candidates.tsv`

Further prioritisation incorporated transcript abundance, exon structure, coding-potential prediction, conserved-domain evidence, and biological relevance. This produced the final set of eight transcript isoforms: five associated with *Ano1* and three associated with *Ano8*.

All eight final candidates retained the PF04547 anoctamin domain. Their genomic span, exon count, mean TPM, relative abundance, and domain evidence are summarised in:

`results/tables/final_prioritised_candidates.tsv`

The final eight candidates were used for expression, relative-abundance, exon-structure, protein-domain, and IGV analyses.

The representative candidate GTF models used for IGV inspection are provided in `results/igv/`. The corresponding BAM alignment files are not included because of their size.

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
- HMMER
- R

Analysis was performed on the University of Nottingham Ada HPC cluster using SLURM.
