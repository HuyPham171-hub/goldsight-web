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

# Copy chart images to dist assets
mkdir -p ./dist/assets/charts
cp -r assets/charts/*.png ./dist/assets/charts/ 2>/dev/null || true

# Copy navbar.js to dist assets
cp assets/navbar.js ./dist/assets/navbar.js 2>/dev/null || true

echo "Build complete! Static files and chart images copied to dist/"