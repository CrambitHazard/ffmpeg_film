#!/usr/bin/env python
"""
Concatenate videos using FFmpeg
"""
import argparse
import os
import sys

from src.config import load_config, get_ffmpeg_path, create_config_from_template
from src.video_processing import concatenate_videos
from src.utils import check_requirements

def main():
    parser = argparse.ArgumentParser(description='Concatenate videos using FFmpeg')
    parser.add_argument('-c', '--config', default='config.json', help='Path to configuration file')
    parser.add_argument('-i', '--input', default='input.txt', help='Path to input file')
    parser.add_argument('-o', '--output', default='temp_concat.mp4', help='Path to output video file')
    args = parser.parse_args()
    
    # Check requirements
    if not check_requirements():
        print("Error: Missing required dependencies.")
        return 1
    
    # Check if input file exists
    if not os.path.exists(args.input):
        print(f"Error: Input file '{args.input}' not found.")
        print("Run generate_input.py first to create the input file.")
        return 1
    
    try:
        # Load configuration
        config = load_config(args.config)
        ffmpeg_path = get_ffmpeg_path(config)
        
        # Concatenate videos
        output_file = concatenate_videos(ffmpeg_path, args.input, args.output)
        print(f"Videos concatenated successfully: {output_file}")
        return 0
    except Exception as e:
        print(f"Error concatenating videos: {e}")
        return 1

if __name__ == '__main__':
    sys.exit(main()) 