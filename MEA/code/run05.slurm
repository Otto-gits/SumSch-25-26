#!/bin/bash
#SBATCH --job-name=run05
#SBATCH --output=res05.out
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1 
#SBATCH --mem=6G     
#SBATCH --time=48:00:00      

module load Anaconda3
python -u runfile_05.py