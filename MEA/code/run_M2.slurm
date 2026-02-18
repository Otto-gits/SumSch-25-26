#!/bin/bash
#SBATCH --job-name=runMEA2
#SBATCH --output=resMEA2.out
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1 
#SBATCH --mem=1G     
#SBATCH --time=60:00:00      

module load Anaconda3
python -u runMEA2.py