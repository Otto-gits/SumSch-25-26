#!/bin/bash
#SBATCH --job-name=runP3
#SBATCH --output=resP3.out
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1 
#SBATCH --mem=1G     
#SBATCH --time=120:00:00      

module load Anaconda3
python -u runfile_P3.py