from pydub import AudioSegment
from pydub.generators import Sine
import numpy as np

def sonify_data(csv_file, sound_file, mode="brightness", max_pixels=10000):
    """
    Generate sound from a CSV file with a specified sonification mode.
    
    Args:
        csv_file (str): Path to the CSV file.
        sound_file (str): Path to save the generated sound file.
        mode (str): Sonification mode ("brightness" or "color").
        max_pixels (int): Maximum number of pixels to process for sound.
    """
    data = np.loadtxt(csv_file, delimiter=',')
    data = data[:max_pixels]  # Limit the number of pixels processed

    audio = AudioSegment.silent(duration=0)  # Start with silence

    for value in data:
        if mode == "brightness":
            frequency = 100 + (value / 255) * 900  # Map brightness to frequency
        else:
            frequency = 440  # Default frequency for color mode

        # Generate a sine wave
        sine_wave = Sine(frequency).to_audio_segment(duration=50)  # Shorter duration
        audio += sine_wave

    audio.export(sound_file, format="wav")
    print(f"Sound file saved at: {sound_file}")
