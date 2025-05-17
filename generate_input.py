#!/usr/bin/env python
"""
Generate input file for FFmpeg concatenation
"""
import argparse
import sys

from src.config import load_config, get_ffmpeg_path, create_config_from_template
from src.video_processing import generate_input_file
from src.utils import check_requirements

def main():
    parser = argparse.ArgumentParser(description='Generate input file for FFmpeg concatenation')
    parser.add_argument('-c', '--config', default='config.json', help='Path to configuration file')
    parser.add_argument('-o', '--output', default='input.txt', help='Path to output input file')
    args = parser.parse_args()
    
    # Check requirements
    if not check_requirements():
        print("Error: Missing required dependencies.")
        return 1
    
    # Check if config exists, create from template if not
    if not os.path.exists(args.config) and args.config == 'config.json':
        if create_config_from_template():
            print("Please edit the config file and run again.")
            return 1
    
    try:
        # Load configuration
        config = load_config(args.config)
        ffmpeg_path = get_ffmpeg_path(config)
        
        # Generate input file
        input_file = generate_input_file(config, ffmpeg_path, args.output)
        print(f"Input file generated successfully: {input_file}")
        return 0
    except Exception as e:
        print(f"Error generating input file: {e}")
        return 1

if __name__ == '__main__':
    import os
    sys.exit(main()) 