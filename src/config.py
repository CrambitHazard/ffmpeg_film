"""
Configuration handling for the video processor
"""
import json
import os
import sys

def load_config(config_file='config.json'):
    """Load configuration from JSON file"""
    try:
        with open(config_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Config file '{config_file}' not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Config file '{config_file}' is not valid JSON.")
        sys.exit(1)

def get_ffmpeg_path(config):
    """Get FFmpeg path from config or use the system's FFmpeg"""
    if 'ffmpeg_path' in config and config['ffmpeg_path']:
        return config['ffmpeg_path']
    else:
        # Try to use system FFmpeg
        return 'ffmpeg'

def create_config_from_template():
    """Create a config.json file from the template if it doesn't exist"""
    if not os.path.exists('config.json') and os.path.exists('config.template.json'):
        try:
            with open('config.template.json', 'r') as src, open('config.json', 'w') as dst:
                dst.write(src.read())
            print("Created config.json from template.")
            print("Please edit config.json to set your FFmpeg path before running again.")
            return True
        except Exception as e:
            print(f"Error creating config from template: {e}")
    return False 