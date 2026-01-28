#!/bin/bash
#SBATCH --job-name=run04
#SBATCH --output=res04.out
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1 
#SBATCH --mem=6G     
#SBATCH --time=48:00:00      

module load Anaconda3
python -u runfile_04.py