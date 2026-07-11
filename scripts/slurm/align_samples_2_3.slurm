#!/bin/bash
#SBATCH --job-name=rat_align23
#SBATCH --partition=defq
#SBATCH --nodes=1
#SBATCH --ntasks=8
#SBATCH --mem=64G
#SBATCH --time=24:00:00
#SBATCH --output=../logs/align23_%j.out
#SBATCH --error=../logs/align23_%j.err

module load python-uoneasy/3.10.4-GCCcore-11.3.0
module load hisat2-uoneasy/2.2.1-gompi-2023a
module load samtools-uoneasy/1.22.1-GCC-14.2.0

PROJECT=~/RNAseq_project/WFA_chloride_project

INDEX=$PROJECT/reference/hisat2_index/Rnor6

ALIGN=$PROJECT/alignment

########################################
# RNAsample2
########################################

hisat2 \
-p 8 \
-x $INDEX \
-1 ~/RNAseq_project/RNAsample2/Sample2_R1.fq.gz \
-2 ~/RNAseq_project/RNAsample2/Sample2_R2.fq.gz \
-S $ALIGN/sample2.sam

samtools view -@ 8 -bS \
$ALIGN/sample2.sam \
> $ALIGN/sample2.bam

samtools sort -@ 8 \
-o $ALIGN/sample2.sorted.bam \
$ALIGN/sample2.bam

samtools index \
$ALIGN/sample2.sorted.bam

rm $ALIGN/sample2.sam
rm $ALIGN/sample2.bam

########################################
# RNAsample3
########################################

hisat2 \
-p 8 \
-x $INDEX \
-1 ~/RNAseq_project/RNAsample3/Sample3_R1.fq.gz \
-2 ~/RNAseq_project/RNAsample3/Sample3_R2.fq.gz \
-S $ALIGN/sample3.sam

samtools view -@ 8 -bS \
$ALIGN/sample3.sam \
> $ALIGN/sample3.bam

samtools sort -@ 8 \
-o $ALIGN/sample3.sorted.bam \
$ALIGN/sample3.bam

samtools index \
$ALIGN/sample3.sorted.bam

rm $ALIGN/sample3.sam
rm $ALIGN/sample3.bam

echo "ALL ALIGNMENTS COMPLETED"
