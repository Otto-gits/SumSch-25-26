#!/bin/bash
#SBATCH --job-name=run06
#SBATCH --output=res06.out
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1 
#SBATCH --mem=1G     
#SBATCH --time=48:00:00      

module load Anaconda3
python -u runfile_06.py