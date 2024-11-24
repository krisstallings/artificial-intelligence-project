# Setup Instructions

## Prerequisites
- Python installed
- Check if Python is already installed on MacOS:
   ```bash
   python3 --version
- Check if Python is already installed on Windows
    ```cmd
    python --version
---

## Setup python environment
- install dependencies for elevenlabs on MacOS
   ```bash
   brew install ffmpeg
- install dependencies for elevenlabs on Windows
https://www.wikihow.com/Install-FFmpeg-on-Windows

- setup virtual env for MacOS
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
- setup virtual env for Windows
    ```cmd
    python -m venv .venv
    .venv\Scripts\activate
- install dependencies 
   ```bash
   pip install -r requirements.txt
---
# Create api key in elevenlabs
- need to access [elevenlabs](https://elevenlabs.io/app/settings/api-keys) to generate api key
- add api key in `src/app.py` for variable `api_key`
---
# Run program

- run program on MacOS
   ```bash
   python3 src/app.py
- run program on Windows
   ```bash
   python src/app.py

- Input selection for entering text or file to generate speech

# Feature work
- supports text input for speech output
- supports file input for speech output
- saves speech files
- supports multiple languages
- supports mulitple speaking styles and accents

