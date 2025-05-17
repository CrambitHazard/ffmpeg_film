#!/usr/bin/env python
"""
Add audio to video using FFmpeg
"""
import argparse
import os
import sys

from src.config import load_config, get_ffmpeg_path, create_config_from_template
from src.audio_processing import add_audio
from src.utils import check_requirements

def main():
    parser = argparse.ArgumentParser(description='Add audio to video using FFmpeg')
    parser.add_argument('-c', '--config', default='config.json', help='Path to configuration file')
    parser.add_argument('-i', '--input', default='temp_concat.mp4', help='Path to input video file')
    parser.add_argument('-o', '--output', default='final_output.mp4', help='Path to output file')
    args = parser.parse_args()
    
    # Check requirements
    if not check_requirements():
        print("Error: Missing required dependencies.")
        return 1
    
    # Check if input file exists
    if not os.path.exists(args.input):
        print(f"Error: Input video '{args.input}' not found.")
        print("Run concatenate_videos.py first to create the concatenated video.")
        return 1
    
    try:
        # Load configuration
        config = load_config(args.config)
        ffmpeg_path = get_ffmpeg_path(config)
        
        # Add audio to video
        output_file = add_audio(config, ffmpeg_path, args.input, args.output)
        print(f"Audio added successfully: {output_file}")
        return 0
    except Exception as e:
        print(f"Error adding audio: {e}")
        return 1

if __name__ == '__main__':
    sys.exit(main()) 