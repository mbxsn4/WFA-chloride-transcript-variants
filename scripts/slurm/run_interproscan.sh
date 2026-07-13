#!/bin/bash
#SBATCH --job-name=interpro_candidates
#SBATCH --output=interpro_candidates.out
#SBATCH --error=interpro_candidates.err
#SBATCH --time=04:00:00
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G

module purge
module load interproscan-uoneasy/5.62-94.0-foss-2023a

cd /gpfs01/home/mbxsn4/RNAseq_project/WFA_chloride_project/sequence_extraction

interproscan.sh \
-i all_candidate_transcripts.unique.fa.transdecoder.pep \
-f tsv \
-o candidate_proteins_interproscan.tsv \
-goterms \
-pa \
-cpu 8
