#!/bin/bash
#SBATCH --job-name=stringtie
#SBATCH --output=/gpfs01/home/mbxsn4/RNAseq_project/WFA_chloride_project/logs/stringtie_%j.out
#SBATCH --error=/gpfs01/home/mbxsn4/RNAseq_project/WFA_chloride_project/logs/stringtie_%j.err
#SBATCH --time=12:00:00
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G

module purge

module load stringtie-uoneasy/2.2.1-GCC-11.2.0

cd ~/RNAseq_project/WFA_chloride_project/stringtie

echo "Starting StringTie assembly"
date

stringtie \
~/RNAseq_project/WFA_chloride_project/alignment/sample2.sorted.bam \
-p 8 \
-G ~/RNAseq_project/WFA_chloride_project/reference/Rattus_norvegicus.Rnor_6.0.95.gtf \
-o sample2.gtf

echo "Sample2 assembly finished"
date

stringtie \
~/RNAseq_project/WFA_chloride_project/alignment/sample3.sorted.bam \
-p 8 \
-G ~/RNAseq_project/WFA_chloride_project/reference/Rattus_norvegicus.Rnor_6.0.95.gtf \
-o sample3.gtf

echo "Sample3 assembly finished"
date

echo "StringTie completed"
date
