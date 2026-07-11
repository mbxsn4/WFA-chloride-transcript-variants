#!/bin/bash
#SBATCH --job-name=stringtie_sample1_final
#SBATCH --partition=defq
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --time=12:00:00
#SBATCH --output=/gpfs01/home/mbxsn4/RNAseq_project/WFA_chloride_project/logs/stringtie_sample1_final_%j.out
#SBATCH --error=/gpfs01/home/mbxsn4/RNAseq_project/WFA_chloride_project/logs/stringtie_sample1_final_%j.err

module purge
module load stringtie-uoneasy/2.2.1-GCC-11.2.0

PROJECT=~/RNAseq_project/WFA_chloride_project

stringtie \
$PROJECT/alignment/sample1.fixed.sorted.bam \
-p 8 \
-G $PROJECT/reference/Rattus_norvegicus.Rnor_6.0.95.gtf \
-o $PROJECT/stringtie/sample1.fixed.gtf
