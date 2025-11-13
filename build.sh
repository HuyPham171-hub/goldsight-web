#!/bin/bash
# build.sh - Vercel deployment script

# Install Python dependencies
pip install -r requirements.txt

# Set environment variable to disable WebSocket in static export
export REFLEX_DISABLE_WEBSOCKET=1

# Initialize Reflex (creates .web directory)
python3 -m reflex init

# Export static frontend (without WebSocket client code)
python3 -m reflex export --no-zip

# Create dist directory and copy static files
mkdir -p ./dist
cp -r .web/build/client/* ./dist/

# CRITICAL: Copy chart JSON data to assets for HTTP access
mkdir -p ./dist/assets/charts_cache
cp -r goldsight/data/cache/*.json ./dist/assets/charts_cache/ 2>/dev/null || true

# Also copy to goldsight path for Python-style loading
mkdir -p ./dist/goldsight/data/cache
cp -r goldsight/data/cache/*.json ./dist/goldsight/data/cache/ 2>/dev/null || true

echo "✅ Build complete! Chart data copied, WebSocket disabled for static deployment"