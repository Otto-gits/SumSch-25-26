#!/bin/bash
#SBATCH --job-name=run09
#SBATCH --output=res09.out
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1 
#SBATCH --mem=1G     
#SBATCH --time=48:00:00      

module load Anaconda3
python -u runPEA9.py