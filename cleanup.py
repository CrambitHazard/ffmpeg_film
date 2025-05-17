#!/usr/bin/env python
"""
Clean up temporary files generated during video processing
"""
import argparse
import sys

from src.utils import cleanup

def main():
    parser = argparse.ArgumentParser(description='Clean up temporary files')
    parser.add_argument('files', nargs='*', default=['input.txt', 'temp_concat.mp4'], 
                        help='Temporary files to clean up')
    args = parser.parse_args()
    
    try:
        # Clean up specified files
        cleanup(args.files)
        print("Cleanup completed successfully")
        return 0
    except Exception as e:
        print(f"Error during cleanup: {e}")
        return 1

if __name__ == '__main__':
    sys.exit(main()) 