#!/bin/bash
#SBATCH --job-name=pfam_hmmscan
#SBATCH --output=pfam_hmmscan.out
#SBATCH --error=pfam_hmmscan.err
#SBATCH --time=04:00:00
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G

module purge
module load HMMER/3.4-gompi-2023a

cd /gpfs01/home/mbxsn4/RNAseq_project/WFA_chloride_project/gffcompare

hmmscan \
  --domtblout pfam_domains.domtblout \
  pfam/Pfam-A.hmm \
  longest_orfs.clean.pep
