#!/bin/bash
#SBATCH --job-name=run02
#SBATCH --output=res02.out
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1 
#SBATCH --mem=1G     
#SBATCH --time=72:00:00      

module load Anaconda3
python -u runPEA2.py