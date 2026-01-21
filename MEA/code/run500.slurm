#!/bin/bash
#SBATCH --job-name=run500knap
#SBATCH --output=500knapres.txt
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1 
#SBATCH --mem=20G            
#SBATCH --time=24:00:00      

module load Anaconda3
python runKp1_MEA.py