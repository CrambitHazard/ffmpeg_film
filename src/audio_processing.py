"""
Audio processing operations
"""
import os
import subprocess

def add_audio(config, ffmpeg_path, video_file, output_file='final_output.mp4'):
    """Add audio tracks to the concatenated video"""
    music_dir = config.get('music_dir', 'Music')
    audio_files = config.get('audio_files', [])
    audio_durations = config.get('audio_durations', [])
    
    # Ensure we have durations for each audio file
    if len(audio_durations) < len(audio_files):
        audio_durations.extend([20] * (len(audio_files) - len(audio_durations)))
    
    # Build the ffmpeg command
    cmd = [ffmpeg_path, '-i', video_file]
    
    # Add input files
    for audio_file in audio_files:
        audio_path = os.path.join(music_dir, audio_file)
        cmd.extend(['-i', audio_path])
    
    # Create filter complex for audio
    filter_parts = []
    labels = []
    
    for i, duration in enumerate(audio_durations[:len(audio_files)]):
        label = f'a{i+1}'
        filter_parts.append(f"[{i+1}:a]atrim=0:{duration},asetpts=PTS-STARTPTS[{label}]")
        labels.append(f"[{label}]")
    
    filter_parts.append(f"{''.join(labels)}concat=n={len(labels)}:v=0:a=1[aout]")
    filter_complex = ';'.join(filter_parts)
    
    cmd.extend([
        '-filter_complex', filter_complex,
        '-map', '0:v',
        '-map', '[aout]',
        '-c:v', 'copy',
        output_file
    ])
    
    print("Adding audio tracks...")
    subprocess.run(cmd, check=True, capture_output=True, text=True)
    return output_file 