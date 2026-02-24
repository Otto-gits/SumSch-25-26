#!/bin/bash
#SBATCH --job-name=runP2
#SBATCH --output=resP2.out
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1 
#SBATCH --mem=1G     
#SBATCH --time=60:00:00      

module load Anaconda3
python -u runfile_P2.py