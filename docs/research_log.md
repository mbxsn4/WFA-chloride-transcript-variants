# Research and Development Log

## Purpose

This log summarises the main analytical decisions, troubleshooting steps, workflow changes, and interpretation milestones during the development of the RNA-seq analysis. Detailed changes are preserved in the Git commit history.

## 11 July 2026 — Initial workflow

- Added the initial RNA-seq workflow for identifying chloride-channel transcript variants in white fat adipocytes.
- Organised the repository into scripts, metadata, results, figures, tables, and workflow documentation.
- Established a candidate-prioritisation approach based on transcript classification, structure, expression, and reproducibility.

## 12 July 2026 — Protein-domain evidence

- Added Pfam anoctamin-domain evidence to strengthen candidate prioritisation.
- Updated the workflow documentation to explain how reproducibility and conserved-domain evidence contributed to candidate selection.
- Interpreted Pfam support as complementary evidence rather than proof of transcript function.

## 13–14 July 2026 — Domain-annotation troubleshooting

- Investigated InterProScan as a possible method for candidate protein-domain annotation.
- Added an initial InterProScan workflow script, but the approach did not provide a reliable working workflow in the available environment.
- Removed the unsuccessful InterProScan script rather than retaining an unverified analysis.
- Adopted HMMER `hmmscan` with the Pfam-A database as the documented domain-screening approach.
- Recorded the relevant anoctamin-domain evidence in the workflow and README.
- Added reproducible scripts for GffCompare transcript-classification and exon-count figures.

## 15 July 2026 — Metadata and documentation

- Added Sample 1 to the metadata table.
- Improved the README overview and clarified the evidence-based candidate-prioritisation workflow.
- Reviewed the relationship between novel-isoform classification, detection across samples, transcript structure, abundance, and protein-domain evidence.

## 17 July 2026 — Input layout and exon-count correction

- Documented the expected input-data layout while keeping large raw sequencing, alignment, and reference files outside the repository.
- Restored tab-separated formatting where required.
- Corrected exon-count results and consolidated the associated plotting scripts.
- Regenerated affected outputs after correcting the underlying values.

## 18 July 2026 — Reproducible TPM figures

- Updated the TPM plotting workflow to use repository-relative input and output paths.
- Replaced manually entered splice-variant percentages with values calculated directly from mean TPM measurements in `candidate_TPM_table.tsv`.
- Added validation that raises an error when TPM measurements are missing for a prioritised transcript.
- Regenerated the splice-variant relative-abundance figure in PNG and PDF formats.
- Removed overlapping labels for very small Ano1 segments while retaining their identification in the legend.
- Added a Python requirements file and documented the command needed to reproduce the relative-abundance figure.

## Interpretation notes

- Reproducibility across samples was treated as an important criterion for prioritising novel isoforms.
- GffCompare class code `j` was used to identify potentially novel isoforms sharing at least one splice junction with a reference transcript.
- TPM abundance was interpreted as expression support and not as independent confirmation of biological function.
- Pfam-domain matches were used as supporting structural evidence.
- Transcript-structure visualisation focused primarily on prioritised Ano1 and Ano8 variants.

## Data and reproducibility notes

- Raw FASTQ files, alignments, genome references, and large intermediate files are not stored in GitHub.
- Sample layout information is provided in `metadata/samples.tsv`.
- The repository contains analysis scripts, selected summary tables, figures, software requirements, and workflow documentation.
- Ada-specific paths remain in some SLURM scripts because they record the computing environment used for the original analysis.

## Use of AI tools

Generative AI tools were used as supplementary support during the project, including for troubleshooting. All resulting work was reviewed and validated by the student.
