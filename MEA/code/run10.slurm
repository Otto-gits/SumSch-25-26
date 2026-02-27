#!/bin/bash
#SBATCH --job-name=run10
#SBATCH --output=res10.out
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1 
#SBATCH --mem=1G     
#SBATCH --time=48:00:00      

module load Anaconda3
python -u runPEA10.py