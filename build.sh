#!/bin/bash
# build.sh - Vercel deployment script

# Install Python dependencies
pip install -r requirements.txt

# Initialize Reflex (creates .web directory)
python3 -m reflex init

# Export static frontend
python3 -m reflex export --no-zip

# Create dist directory and copy static files
mkdir -p ./dist
cp -r .web/build/client/* ./dist/