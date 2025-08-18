
"""
Run the Summer Project Website with Dark Theme
==============================================

This script runs your Streamlit website with the new professional dark theme.
"""

import subprocess
import sys
import os

def main():
    """Run the Streamlit website."""
    
    print("🌟 Starting MY SUMMER PROJECT Website...")
    print("🎨 Dark Theme: Professional & Animated")
    print("=" * 50)
    
    
    try:
        import streamlit
        print("✅ Streamlit is installed")
    except ImportError:
        print("❌ Streamlit not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "streamlit"])
    
    
    required_packages = [
        "streamlit",
        "pillow",
        "pyttsx3"
    ]
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package} is installed")
        except ImportError:
            print(f"❌ {package} not found. Installing...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    
    print("\n🚀 Launching website...")
    print("📱 Open your browser and go to: http://localhost:8501")
    print("🔄 Press Ctrl+C to stop the server")
    print("=" * 50)
    
   
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "main.py",
            "--server.port", "8501",
            "--server.address", "localhost",
            "--browser.gatherUsageStats", "false"
        ])
    except KeyboardInterrupt:
        print("\n👋 Website stopped. Goodbye!")
    except Exception as e:
        print(f"❌ Error running website: {e}")

if __name__ == "__main__":
    main() 