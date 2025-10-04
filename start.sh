#!/bin/bash

echo "Starting Hotel Agreement Form Generator..."
echo

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Error: Virtual environment not found!"
    echo "Please run 'python3 setup.py' first to set up the environment."
    exit 1
fi

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed or not in PATH"
    echo "Please install Python 3.7 or higher"
    exit 1
fi

# Start the application using virtual environment
venv/bin/python app.py 