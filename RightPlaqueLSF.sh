#!/bin/bash
#BSUB -J my_job_name           # Job name
#BSUB -n 4                     # Number of CPU cores
#BSUB -R "rusage[mem=8192]"    # Memory requirement (in MB)
#BSUB -W 2:00                  # Wall-clock time (2 hours)

# Your job commands go here
python RightPlaqueCropped.py
