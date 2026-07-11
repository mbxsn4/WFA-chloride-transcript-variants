#!/bin/bash
#SBATCH --job-name=gffcompare_final
#SBATCH --partition=defq
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=08:00:00
#SBATCH --output=/gpfs01/home/mbxsn4/RNAseq_project/WFA_chloride_project/logs/gffcompare_final_%j.out
#SBATCH --error=/gpfs01/home/mbxsn4/RNAseq_project/WFA_chloride_project/logs/gffcompare_final_%j.err

module purge
source ~/miniconda3/bin/activate
conda activate base

PROJECT=~/RNAseq_project/WFA_chloride_project

cd $PROJECT/gffcompare

gffcompare \
-r $PROJECT/reference/Rattus_norvegicus.Rnor_6.0.95.gtf \
-o WFA_compare_final \
$PROJECT/stringtie/sample1.fixed.gtf \
$PROJECT/stringtie/sample2.gtf \
$PROJECT/stringtie/sample3.gtf
