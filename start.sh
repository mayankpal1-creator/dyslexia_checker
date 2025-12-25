#!/bin/bash
# DyslexiaCheck - Startup Script for macOS/Linux

echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║                     DYSLEXIACHECK                            ║"
echo "║         Early Detection & Support Platform                   ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo ""
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo ""

# Install requirements
echo "Installing/checking dependencies..."
pip install -q -r requirements.txt
echo ""

# Start the application
echo "Starting DyslexiaCheck application..."
echo "The application will be available at: http://localhost:5000"
echo ""
python run.py
