#!/bin/bash
#SBATCH --job-name=run500knap
#SBATCH --output=res.out
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1 
#SBATCH --mem=20G            
#SBATCH --time=48:00:00      

module load Anaconda3
python -u runKp1_MEA.py