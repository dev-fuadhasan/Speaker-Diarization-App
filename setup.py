"""
Setup script for the Speaker Diarization application.
This script helps with initial setup and dependency installation.
"""

import os
import sys
import subprocess
import platform

def run_command(command, description):
    """Run a command and handle errors."""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 11):
        print("❌ Python 3.11 or higher is required")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible")
    return True

def check_node_version():
    """Check if Node.js is installed and compatible."""
    try:
        result = subprocess.run(["node", "--version"], capture_output=True, text=True)
        version = result.stdout.strip()
        print(f"✅ Node.js {version} is installed")
        return True
    except FileNotFoundError:
        print("❌ Node.js is not installed. Please install Node.js 18+ from https://nodejs.org/")
        return False

def setup_backend():
    """Set up the Python backend."""
    print("\n🐍 Setting up Python backend...")
    
    # Create virtual environment
    if not os.path.exists("venv"):
        if not run_command("python -m venv venv", "Creating virtual environment"):
            return False
    
    # Activate virtual environment and install dependencies
    if platform.system() == "Windows":
        activate_cmd = "venv\\Scripts\\activate"
        pip_cmd = "venv\\Scripts\\pip"
    else:
        activate_cmd = "source venv/bin/activate"
        pip_cmd = "venv/bin/pip"
    
    if not run_command(f"{pip_cmd} install --upgrade pip", "Upgrading pip"):
        return False
    
    if not run_command(f"{pip_cmd} install -r requirements.txt", "Installing Python dependencies"):
        return False
    
    return True

def setup_frontend():
    """Set up the React frontend."""
    print("\n⚛️ Setting up React frontend...")
    
    os.chdir("frontend")
    
    if not run_command("npm install", "Installing Node.js dependencies"):
        os.chdir("..")
        return False
    
    os.chdir("..")
    return True

def create_directories():
    """Create necessary directories."""
    print("\n📁 Creating directories...")
    
    directories = ["temp", "output"]
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"✅ Created directory: {directory}")
        else:
            print(f"✅ Directory already exists: {directory}")
    
    return True

def main():
    """Main setup function."""
    print("🚀 Speaker Diarization App Setup")
    print("=" * 40)
    
    # Check system requirements
    if not check_python_version():
        sys.exit(1)
    
    if not check_node_version():
        sys.exit(1)
    
    # Create directories
    if not create_directories():
        sys.exit(1)
    
    # Setup backend
    if not setup_backend():
        print("\n❌ Backend setup failed")
        sys.exit(1)
    
    # Setup frontend
    if not setup_frontend():
        print("\n❌ Frontend setup failed")
        sys.exit(1)
    
    print("\n🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Get a HuggingFace token from https://huggingface.co")
    print("2. Update backend/audio_processor.py with your token")
    print("3. Run the backend: cd backend && uvicorn main:app --reload")
    print("4. Run the frontend: cd frontend && npm run dev")
    print("5. Open http://localhost:3000 in your browser")

if __name__ == "__main__":
    main()
