"""
Video processing operations
"""
import os
import subprocess

def generate_input_file(config, ffmpeg_path, output_file='input.txt'):
    """Generate the input file for FFmpeg's concat demuxer
    
    Args:
        config: Configuration dictionary
        ffmpeg_path: Path to FFmpeg executable
        output_file: Path to output input file
        
    Returns:
        Path to the generated input file
    """
    videos_dir = config.get('videos_dir', 'Videos')
    video_files = config.get('video_files', [])
    
    # If no specific files are configured, use all mp4 files in the videos directory
    if not video_files:
        if os.path.exists(videos_dir):
            video_files = [f for f in sorted(os.listdir(videos_dir)) if f.lower().endswith('.mp4')]
    
    # Write to input file
    with open(output_file, 'w') as f:
        for video in video_files:
            video_path = os.path.join(videos_dir, video).replace('\\', '/')
            f.write(f"file '{video_path}'\n")
    
    print(f"Generated input file with {len(video_files)} video entries")
    return output_file

def concatenate_videos(ffmpeg_path, input_file, output_file='temp_concat.mp4'):
    """Concatenate videos using FFmpeg's concat demuxer
    
    Args:
        ffmpeg_path: Path to FFmpeg executable
        input_file: Path to input file for concat demuxer
        output_file: Path to output concatenated video
        
    Returns:
        Path to the concatenated video file
    """
    cmd = [
        ffmpeg_path,
        '-f', 'concat',
        '-safe', '0',
        '-i', input_file,
        '-c', 'copy',
        output_file
    ]
    
    print("Concatenating videos...")
    result = subprocess.run(cmd, check=True, capture_output=True, text=True)
    return output_file 