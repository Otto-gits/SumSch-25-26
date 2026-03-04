#!/bin/bash
#SBATCH --job-name=runC5
#SBATCH --output=resC5.out
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1 
#SBATCH --mem=1G     
#SBATCH --time=200:00:00      

module load Anaconda3
python -u runfile_C5.py