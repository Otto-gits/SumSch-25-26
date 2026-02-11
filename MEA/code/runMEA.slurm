#!/bin/bash
#SBATCH --job-name=runMEA
#SBATCH --output=resMEA.out
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1 
#SBATCH --mem=1G     
#SBATCH --time=60:00:00      

module load Anaconda3
python -u runfileMEA.py