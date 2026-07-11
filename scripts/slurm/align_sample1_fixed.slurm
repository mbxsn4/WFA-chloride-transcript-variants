#!/bin/bash
#SBATCH --job-name=sample1_align_fixed
#SBATCH --partition=defq
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=96G
#SBATCH --time=24:00:00
#SBATCH --output=/gpfs01/home/mbxsn4/RNAseq_project/WFA_chloride_project/logs/sample1_align_fixed_%j.out
#SBATCH --error=/gpfs01/home/mbxsn4/RNAseq_project/WFA_chloride_project/logs/sample1_align_fixed_%j.err

module load python-uoneasy/3.10.4-GCCcore-11.3.0
module load hisat2-uoneasy/2.2.1-gompi-2023a
module load samtools-uoneasy/1.22.1-GCC-14.2.0

PROJECT=~/RNAseq_project/WFA_chloride_project
INDEX=$PROJECT/reference/hisat2_index/Rnor6
ALIGN=$PROJECT/alignment

echo "Starting Sample1 corrected alignment"
date

hisat2 -p 8 \
-x $INDEX \
-1 $PROJECT/raw_fastq/sample1_R1.fq.gz \
-2 $PROJECT/raw_fastq/sample1_R2.fq.gz \
-S $ALIGN/sample1.fixed.sam

echo "HISAT2 finished"
date

samtools view -@ 8 -bS $ALIGN/sample1.fixed.sam > $ALIGN/sample1.fixed.bam

echo "BAM conversion finished"
date

samtools sort -@ 8 -o $ALIGN/sample1.fixed.sorted.bam $ALIGN/sample1.fixed.bam

echo "BAM sorting finished"
date

samtools index $ALIGN/sample1.fixed.sorted.bam

echo "BAM indexing finished"
date

rm -f $ALIGN/sample1.fixed.sam
rm -f $ALIGN/sample1.fixed.bam

echo "Sample1 corrected alignment pipeline completed"
date
