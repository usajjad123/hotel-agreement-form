#!/usr/bin/env python3
"""
Hotel Agreement Form Generator - Startup Script
This script checks dependencies and starts the Flask server
"""

import os
import sys
import subprocess
import importlib.util
from config import SAMPLE_AGREEMENT_FILE, FONT_FILE

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 7):
        print("❌ Error: Python 3.7 or higher is required")
        print(f"Current version: {sys.version}")
        sys.exit(1)
    print(f"✅ Python version: {sys.version.split()[0]}")

def check_required_files():
    """Check if required files exist"""
    required_files = [
        SAMPLE_AGREEMENT_FILE,
        FONT_FILE
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
        else:
            print(f"✅ Found: {file}")
    
    if missing_files:
        print("❌ Missing required files:")
        for file in missing_files:
            print(f"   - {file}")
        print("\nPlease ensure all required files are in the project directory.")
        sys.exit(1)

def install_requirements():
    """Install required Python packages"""
    print("\n📦 Installing Python dependencies...")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("✅ Dependencies installed successfully")
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        print("Please run: pip install -r requirements.txt")
        sys.exit(1)

def check_dependencies():
    """Check if required packages are installed"""
    required_packages = ['flask', 'flask_cors', 'PIL']
    
    missing_packages = []
    for package in required_packages:
        if package == 'PIL':
            spec = importlib.util.find_spec('PIL')
        else:
            spec = importlib.util.find_spec(package)
        
        if spec is None:
            missing_packages.append(package)
        else:
            print(f"✅ {package} is installed")
    
    if missing_packages:
        print(f"\n❌ Missing packages: {', '.join(missing_packages)}")
        install_requirements()

def create_directories():
    """Create necessary directories"""
    directories = ['static', 'ALL_AGREEMENTS']
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✅ Directory ready: {directory}")

def move_static_files():
    """Move static files to static directory"""
    static_files = ['index.html', 'styles.css', 'script.js']
    
    for file in static_files:
        if os.path.exists(file) and not os.path.exists(f'static/{file}'):
            try:
                os.rename(file, f'static/{file}')
                print(f"✅ Moved: {file} to static/")
            except Exception as e:
                print(f"⚠️  Could not move {file}: {e}")

def main():
    """Main startup function"""
    print("🏨 Hotel Agreement Form Generator")
    print("=" * 40)
    
    # Check if virtual environment exists
    venv_path = "venv"
    if not os.path.exists(venv_path):
        print("❌ Virtual environment not found!")
        print("Please run 'python setup.py' first to set up the environment.")
        sys.exit(1)
    
    # Check Python version
    check_python_version()
    
    # Check required files
    print("\n📁 Checking required files...")
    check_required_files()
    
    # Create directories
    print("\n📂 Setting up directories...")
    create_directories()
    
    # Move static files
    print("\n📄 Organizing files...")
    move_static_files()
    
    print("\n🚀 Starting server...")
    print("=" * 40)
    print("✅ Server is ready!")
    print("🌐 Open your browser and go to: http://localhost:5000")
    print("⏹️  Press Ctrl+C to stop the server")
    print("=" * 40)
    
    # Start the Flask app using virtual environment Python
    try:
        if os.name == 'nt':  # Windows
            python_executable = "venv\\Scripts\\python.exe"
        else:  # macOS/Linux
            python_executable = "venv/bin/python"
        
        subprocess.run([python_executable, "app.py"])
    except KeyboardInterrupt:
        print("\n👋 Server stopped. Goodbye!")
    except Exception as e:
        print(f"\n❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main() 