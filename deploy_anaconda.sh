#!/bin/bash
# This script uses the ANACONDA_TOKEN env var.
# To create a token use the commands below or directly in your conda account.
# >>> anaconda login
# >>> anaconda auth -c -n travis --max-age 307584000 --url https://anaconda.org/USERNAME/PACKAGENAME --scopes "api:write api:read"
#
# The token is stored as env var in your travis account (for security reasons, not here).
set -e

echo "Converting conda package..."
conda convert --platform all $HOME/miniconda3/conda-bld/linux-64/${PACKAGENAME}-*.tar.bz2 --output-dir conda-bld/

echo "Deploying to Anaconda.org..."
anaconda -t $ANACONDA_TOKEN upload conda-bld/**/${PACKAGENAME}-*.tar.bz2

echo "Successfully deployed to Anaconda.org."
exit 0
