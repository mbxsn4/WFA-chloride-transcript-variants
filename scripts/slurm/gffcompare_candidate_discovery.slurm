#!/bin/bash
#SBATCH --job-name=gffcompare_all3
#SBATCH --output=/gpfs01/home/mbxsn4/RNAseq_project/WFA_chloride_project/logs/gffcompare_all3_%j.out
#SBATCH --error=/gpfs01/home/mbxsn4/RNAseq_project/WFA_chloride_project/logs/gffcompare_all3_%j.err
#SBATCH --time=08:00:00
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G

module purge
source ~/miniconda3/bin/activate
conda activate base

cd ~/RNAseq_project/WFA_chloride_project/gffcompare

echo "Starting GffCompare all 3 samples"
date

gffcompare \
-r ~/RNAseq_project/WFA_chloride_project/reference/Rattus_norvegicus.Rnor_6.0.95.gtf \
-o WFA_compare_all3 \
~/RNAseq_project/WFA_chloride_project/stringtie/sample1.gtf \
~/RNAseq_project/WFA_chloride_project/stringtie/sample2.gtf \
~/RNAseq_project/WFA_chloride_project/stringtie/sample3.gtf

echo "GffCompare all 3 samples finished"
date
