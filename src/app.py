from elevenlabs import play
from elevenlabs.client import ElevenLabs

# access the ElevenLabs api requires setting up an api key
client = ElevenLabs(
  api_key="",
)

# function to provide option to create speech from text file
def speech_from_text_file(file_path):
    """
    This can be used to provide text file for generating the speech.

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

# function to create speech from the text
def create_speech(text, voice="Rachel", model="eleven_multilingual_v2", settings=None):
    """
    Generate speech audio from text.

    Args:
        text (str): The text used to generate the speech.
        voice (str): The voice used to read the text.
        model (str): Model to use for speech.
        settings (dict): Optional settings for speed, pitch, and volume.

    Returns:
        Audio of the provided text.
    """
    return client.generate(
        text=text,
        voice=voice,
        model=model,
    )

# function to save speech created to file
def save_speech(speech_data, file_name):
    """
    Save speech data created to a file.

    Args:
        speech_data (bytes): Binary audio data.
        file_name (str): Name to save the audio file.
    """
    try:
        with open(file_name, "wb") as file:
            if hasattr(speech_data, "__iter__") and not isinstance(speech_data, (bytes, bytearray)):
                for chunk in speech_data:
                    file.write(chunk)
            else:
                file.write(speech_data)
        print(f"Speech audio generated has been saved to '{file_name}'.")
    except Exception as e:
        print(f"Error saving speech: {e}")

# Main Program to run text to speech AI program
def main():
    print("This program will accept text files or cli input to return generated speech audio. ")
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

    # create the audio for the user from generated speech
    print("Creating the speech audio for the text.")
    audio = create_speech(text_input, voice="Brian", model="eleven_multilingual_v2")

    # play the audio for the user
    play(audio)

    # output the audio to a local file as an mp3
    save_speech(audio, file_name="audio.mp3")
    print("Audio has been created, played, and saved as 'audio.mp3'.")


if __name__ == "__main__":
    main()
