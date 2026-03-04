#!/bin/bash
#SBATCH --job-name=runC1
#SBATCH --output=resC1.out
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1 
#SBATCH --mem=1G     
#SBATCH --time=100:00:00      

module load Anaconda3
python -u runfile_C1.py