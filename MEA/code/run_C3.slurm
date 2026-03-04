#!/bin/bash
#SBATCH --job-name=runC3
#SBATCH --output=resC3.out
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1 
#SBATCH --mem=1G     
#SBATCH --time=100:00:00      

module load Anaconda3
python -u runfile_C3.py