#!/bin/bash
# build.sh

# Install Python dependencies
pip install -r requirements.txt

# Initialize Reflex
reflex init

# Export frontend
reflex export --no-zip

# Copy static files
cp -r .web/build/client/* ./dist/