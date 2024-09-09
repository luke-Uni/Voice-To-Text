# Audio Segmentation Script

This Python script processes an audio file, converts it to `.wav` format, splits it into four equal segments, and exports these segments as separate `.wav` files.

## Features

- Converts an audio file to `.wav` format.
- Splits the audio into four equal parts.
- Exports each segment as an individual `.wav` file.

## Installation

1. Clone the repository or download the script.
2. Install the required Python packages using pip:

    ```bash
    pip install pydub
    ```

3. Install ffmpeg (required by `pydub` for handling audio formats). You can find installation instructions [here](https://ffmpeg.org/download.html).

## Usage

1. Set the path to your original audio file:

    ```python
    original_audio_path = "Path to your original audio file"
    ```

2. Run the script:

    ```bash
    python audio_segmentation.py
    ```

3. The script will generate four audio segments, which will be saved as `.wav` files in the specified directory.
