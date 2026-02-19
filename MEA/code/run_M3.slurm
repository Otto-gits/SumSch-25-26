#!/bin/bash
#SBATCH --job-name=runMEA3
#SBATCH --output=resMEA3.out
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1 
#SBATCH --mem=1G     
#SBATCH --time=60:00:00      

module load Anaconda3
python -u runMEA3.py