#!/usr/bin/env python3
"""
Hotel Agreement Form Generator - Setup Script
This script creates a virtual environment and installs all dependencies
"""

import os
import sys
import subprocess
import venv
from pathlib import Path
from config import SAMPLE_AGREEMENT_FILE, FONT_FILE

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 7):
        print("❌ Error: Python 3.7 or higher is required")
        print(f"Current version: {sys.version}")
        sys.exit(1)
    print(f"✅ Python version: {sys.version.split()[0]}")

def create_virtual_environment():
    """Create a virtual environment"""
    venv_path = Path("venv")
    
    if venv_path.exists():
        print("✅ Virtual environment already exists")
        return venv_path
    
    print("📦 Creating virtual environment...")
    try:
        venv.create("venv", with_pip=True)
        print("✅ Virtual environment created successfully")
        return venv_path
    except Exception as e:
        print(f"❌ Failed to create virtual environment: {e}")
        sys.exit(1)

def get_python_executable():
    """Get the Python executable path for the virtual environment"""
    if os.name == 'nt':  # Windows
        return "venv\\Scripts\\python.exe"
    else:  # macOS/Linux
        return "venv/bin/python"

def get_pip_executable():
    """Get the pip executable path for the virtual environment"""
    if os.name == 'nt':  # Windows
        return "venv\\Scripts\\pip.exe"
    else:  # macOS/Linux
        return "venv/bin/pip"

def install_dependencies():
    """Install required packages in the virtual environment"""
    pip_executable = get_pip_executable()
    
    print("📦 Installing dependencies...")
    try:
        # Upgrade pip first
        subprocess.check_call([pip_executable, "install", "--upgrade", "pip"])
        
        # Install requirements
        subprocess.check_call([pip_executable, "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        sys.exit(1)

def create_activation_scripts():
    """Create activation scripts for different platforms"""
    
    # Windows activation script
    with open("activate.bat", "w") as f:
        f.write("@echo off\n")
        f.write("echo Activating virtual environment...\n")
        f.write("call venv\\Scripts\\activate.bat\n")
        f.write("echo Virtual environment activated!\n")
        f.write("echo Run 'python app.py' to start the server\n")
        f.write("cmd /k\n")
    
    # macOS/Linux activation script
    with open("activate.sh", "w") as f:
        f.write("#!/bin/bash\n")
        f.write("echo 'Activating virtual environment...'\n")
        f.write("source venv/bin/activate\n")
        f.write("echo 'Virtual environment activated!'\n")
        f.write("echo 'Run \"python app.py\" to start the server'\n")
        f.write("bash\n")
    
    # Make the shell script executable
    if os.name != 'nt':  # Not Windows
        os.chmod("activate.sh", 0o755)
    
    print("✅ Activation scripts created")

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
        return False
    return True

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
    """Main setup function"""
    print("🏨 Hotel Agreement Form Generator - Setup")
    print("=" * 50)
    
    # Check Python version
    check_python_version()
    
    # Check required files
    print("\n📁 Checking required files...")
    if not check_required_files():
        sys.exit(1)
    
    # Create virtual environment
    print("\n🐍 Setting up virtual environment...")
    create_virtual_environment()
    
    # Install dependencies
    print("\n📦 Installing dependencies...")
    install_dependencies()
    
    # Create directories
    print("\n📂 Setting up directories...")
    create_directories()
    
    # Move static files
    print("\n📄 Organizing files...")
    move_static_files()
    
    # Create activation scripts
    print("\n🔧 Creating activation scripts...")
    create_activation_scripts()
    
    print("\n" + "=" * 50)
    print("✅ Setup completed successfully!")
    print("\n🚀 To start the application:")
    print("   Windows:  Double-click 'start.bat' or run 'activate.bat' then 'python app.py'")
    print("   macOS/Linux:  Run './start.sh' or 'source activate.sh' then 'python app.py'")
    print("\n🌐 Once started, open your browser and go to: http://localhost:5000")
    print("=" * 50)

if __name__ == '__main__':
    main() 