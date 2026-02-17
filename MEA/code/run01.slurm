#!/bin/bash
#SBATCH --job-name=run01
#SBATCH --output=res01.out
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1 
#SBATCH --mem=1G     
#SBATCH --time=48:00:00      

module load Anaconda3
python -u runPEA1.py