import librosa
import numpy as np

# Function to analyze the audio mixing level
def evaluate_mixing(audio_file):
    try:
        # Load the audio file using Librosa
        y, sr = librosa.load(audio_file)

        # Calculate the Root Mean Square (RMS) for loudness
        rms = librosa.feature.rms(y=y)[0]
        avg_loudness = np.mean(rms)

        # Calculate Spectral Centroid (brightness of the audio)
        spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
        avg_brightness = np.mean(spectral_centroid)

        # Display results and suggest improvements
        if avg_loudness < 0.01 or avg_brightness < 2000:
            return "Mixing Level: Poor. Suggest increasing loudness and adding more treble (high frequencies)."
        else:
            return "Mixing Level: Good. No immediate corrections needed."
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function with an audio file
audio_file = r'C:\Users\yonij\Desktop\KOTET\SILO\01.mp3'  # Use a raw string for file path
result = evaluate_mixing(audio_file)
print(result)
