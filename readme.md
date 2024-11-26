# Project Overview

This is a group project for Fall 2024 Artificial Intelligence (CPSC-4370-48F) course creating an AI Text Reader with the following group members. 

- Brittany Cooper - L20284115

- Jaylon Pham - L20572785

- Kristy Stallings - L20494128

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
## Create api key in elevenlabs
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
   ```bash
      Choose an input option:
      1. Enter text directly in console
      2. Load text from a file

- Input selection for voice options
   ```bash
      Please select a voice to use for generating the speech:
      1. Chris - Conversational, American, Casual, Male
      2. Callum - Transatlantic, Intense, Characters, Male
      3. Matilda - Narration, American, Friendly, Female
      4. Alice - British, Confident, News, Female
      5. Aria - American, Expressive, Social Media, Female
      6. George - Narration, British, Warm, Male

# Current Features
- supports text input for speech output
- supports file input for speech output
- supports multiple languages
- supports mulitple speaking voices
- plays generated audio
- saves generated speech files
- plays generated speech file for testing
