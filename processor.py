#!/usr/bin/env python
"""
Main module for Horror Movie Video Processor
Brings together all components to process videos
"""
import os
import sys
import argparse
import subprocess

from src.config import load_config, get_ffmpeg_path, create_config_from_template
from src.utils import check_requirements

def run_step(script, args=None):
    """Run a step of the processing pipeline"""
    cmd = [sys.executable, script]
    if args:
        cmd.extend(args)
    
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd)
    return result.returncode == 0

def process_videos(config_file='config.json', keep_temp=False):
    """Run the full video processing workflow"""
    # Check if requirements are met
    if not check_requirements():
        print("Error: Missing required dependencies.")
        return False
        
    # Check if config exists, create from template if not
    if not os.path.exists(config_file) and config_file == 'config.json':
        if create_config_from_template():
            print("Please edit the config file and run again.")
            return False
    
    try:
        # Load config to get output file name
        config = load_config(config_file)
        output_file = config.get('output_file', 'final_output.mp4')
        
        # Step 1: Generate input file
        if not run_step('generate_input.py', ['-c', config_file]):
            print("Error generating input file.")
            return False
        
        # Step 2: Concatenate videos
        temp_concat = 'temp_concat.mp4'
        if not run_step('concatenate_videos.py', ['-c', config_file, '-o', temp_concat]):
            print("Error concatenating videos.")
            return False
        
        # Step 3: Add audio
        if not run_step('add_audio.py', ['-c', config_file, '-i', temp_concat, '-o', output_file]):
            print("Error adding audio.")
            return False
        
        # Step 4: Clean up (optional)
        if not keep_temp:
            if not run_step('cleanup.py', ['input.txt', temp_concat]):
                print("Warning: Failed to clean up temporary files.")
        
        print(f"Video processing complete. Output saved to {output_file}")
        return True
        
    except Exception as e:
        print(f"Error during processing: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description='Process video files with FFmpeg')
    parser.add_argument('-c', '--config', default='config.json', help='Path to configuration file')
    parser.add_argument('--keep-temp', action='store_true', help='Keep temporary files')
    args = parser.parse_args()
    
    success = process_videos(args.config, args.keep_temp)
    
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main() 