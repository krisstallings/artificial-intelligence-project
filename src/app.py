from elevenlabs import play, save
from elevenlabs.client import ElevenLabs
import os
import platform

# Access the ElevenLabs API requires setting up an API key
client = ElevenLabs(
  api_key="",
)

# Function to provide option to create speech from text file
def speech_from_text_file(file_path):
    """
    This can be used to provide a text file for generating the speech.

    Args:
        file_path (str): Path to the text file.

    Returns:
        str: Will put the content of the file as a string.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None

# Function to create speech from the text
def create_speech(text, voice="Rachel", model="eleven_multilingual_v2", settings=None):
    """
    Generate speech audio from text.

    Args:
        text (str): The text used to generate the speech.
        voice (str): The voice used to read the text.
        model (str): Model to use for speech.
        settings (dict): Optional settings for speed, pitch, and volume.

    Returns:
        Audio data of the provided text.
    """
    return client.generate(
        text=text,
        voice=voice,
        model=model,
        stream=True 
    )

# Function to play audio from a file using system-specific options
def play_audio_from_file(file_name):
    """
    Play audio file using system-specific command options.

    Args:
        file_name (str): Name of the audio file.
    """
    try:
        system_platform = platform.system()
        if system_platform == "Darwin":
            os.system(f"afplay {file_name}")
        elif system_platform == "Linux":
            os.system(f"mpg123 {file_name}")
        elif system_platform == "Windows":
            os.system(f'start {file_name}')
        else:
            print(f"Unsupported OS: {system_platform}")
    except Exception as e:
        print(f"Error playing the audio from file: {e}")

# Main program to run text to speech AI program
def main():
    print("This program will accept text files or CLI input to return generated speech audio.")
    print("Choose an input option:")
    print("1. Enter text directly in console")
    print("2. Load text from a file")
    
    user_selection = input("Enter 1 or 2: ")
    
    if user_selection == "1":
        text_input = input("Enter the text to generate speech audio: ")
    elif user_selection == "2":
        file_path = input("Enter the path to the text file: ")
        text_input = speech_from_text_file(file_path)
        if not text_input:
            return
    else:
        print("Invalid user selection! Exiting the program.")
        return

    # Create audio for the user from generated speech
    print("Creating the speech audio for the text.")
    audio = create_speech(text_input, voice="Brian", model="eleven_multilingual_v2")
    print("Playing the created audio from text.")
    play(audio)

    # Save the audio to a local file
    file_name = "audio.mp3"
    audio = create_speech(text_input, voice="Brian", model="eleven_multilingual_v2")
    save(audio, file_name)
    print(f"Audio has been created and saved as {file_name}.")

    # Play the saved audio file
    print(f"Playing audio from the saved file {file_name}.")
    play_audio_from_file(file_name)


if __name__ == "__main__":
    main()
