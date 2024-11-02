#!/bin/bash

# Install mamba if not already installed
conda install mamba -n base -c conda-forge -y

# Create environment using mamba
mamba create -n risk-analysis python=3.9 numpy matplotlib seaborn -y

echo "To activate the environment, run: conda activate risk-analysis"