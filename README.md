# Horror Movie Video Processor

A modular Python-based tool for processing and combining horror movie clips with audio tracks using FFmpeg.

## Features

- Concatenate multiple video clips in a specific order
- Add multiple audio tracks to the concatenated video
- Configurable via JSON file
- Automatic cleanup of temporary files
- Support for custom FFmpeg path
- Modular architecture for easy maintenance
- Individual scripts for each processing step

## Requirements

- Python 3.6+
- FFmpeg (either installed on system PATH or specified in config)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/horror-movie-processor.git
   cd horror-movie-processor
   ```

2. Make sure FFmpeg is installed or available on your system

3. Create your configuration file by copying the template:
   ```
   cp config.template.json config.json
   ```

4. Update the FFmpeg path in `config.json` to match your system

## Usage

### All-in-one Processing

Run the full processing pipeline in one go:

```
python processor.py
```

On Windows, you can also use the batch file:
```
run_processor.bat all
```

### Individual Processing Steps

You can run each step of the processing pipeline separately:

1. Generate the input file:
   ```
   python generate_input.py
   ```
   or `run_processor.bat generate`

2. Concatenate the videos:
   ```
   python concatenate_videos.py
   ```
   or `run_processor.bat concatenate`

3. Add audio to the concatenated video:
   ```
   python add_audio.py
   ```
   or `run_processor.bat audio`

4. Clean up temporary files:
   ```
   python cleanup.py
   ```
   or `run_processor.bat cleanup`

### Command Line Options

Each script supports various command line options:

- **generate_input.py**:
  - `-c, --config`: Path to configuration file (default: config.json)
  - `-o, --output`: Path to output input file (default: input.txt)

- **concatenate_videos.py**:
  - `-c, --config`: Path to configuration file (default: config.json)
  - `-i, --input`: Path to input file (default: input.txt)
  - `-o, --output`: Path to output video file (default: temp_concat.mp4)

- **add_audio.py**:
  - `-c, --config`: Path to configuration file (default: config.json)
  - `-i, --input`: Path to input video file (default: temp_concat.mp4)
  - `-o, --output`: Path to output file (default: final_output.mp4)

- **processor.py**:
  - `-c, --config`: Path to configuration file (default: config.json)
  - `--keep-temp`: Keep temporary files after processing

## Configuration Options

The `config.json` file contains the following options:

| Option            | Description                                | Default        |
|-------------------|--------------------------------------------|----------------|
| ffmpeg_path       | Path to FFmpeg executable                  | "ffmpeg"       |
| videos_dir        | Directory containing video files           | "Videos"       |
| music_dir         | Directory containing audio files           | "Music"        |
| output_file       | Name of the final output file              | "final_output.mp4" |
| cleanup_temp_files| Whether to remove temporary files          | true           |
| video_files       | List of video files to concatenate         | []             |
| audio_files       | List of audio files to add                 | []             |
| audio_durations   | Duration to use from each audio file       | []             |

If `video_files` is empty, all MP4 files in the `videos_dir` will be used in alphabetical order.

## Project Structure

```
horror-movie-processor/
├── processor.py           # Main entry point for full processing
├── generate_input.py      # Script to generate input file only
├── concatenate_videos.py  # Script to concatenate videos only
├── add_audio.py           # Script to add audio only
├── cleanup.py             # Script to clean up temporary files
├── src/                   # Source code modules
│   ├── __init__.py        # Package initialization
│   ├── config.py          # Configuration handling
│   ├── video_processing.py# Video processing functions
│   ├── audio_processing.py# Audio processing functions
│   └── utils.py           # Utility functions
├── config.template.json   # Template configuration file
├── README.md              # This file
├── run_processor.bat      # Windows batch file with options
├── Videos/                # Directory for video clips
│   └── Shot1.mp4, Shot2.mp4, etc.
└── Music/                 # Directory for audio files
    └── audio1.mp3, audio2.mp3, etc.
```

## License

MIT License

## Credits

Created by [Your Name] 