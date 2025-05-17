"""
Utility functions for the video processor
"""
import os

def cleanup(temp_files):
    """Remove temporary files"""
    for file in temp_files:
        if os.path.exists(file):
            os.remove(file)
            print(f"Removed temporary file: {file}")
    
def check_requirements():
    """Check if all the required tools and libraries are installed"""
    try:
        import subprocess
        import json
        import sys
        
        # All required modules are available
        return True
    except ImportError as e:
        print(f"Missing required Python module: {e}")
        return False 