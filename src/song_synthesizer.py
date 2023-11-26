import numpy as np
import wave
import librosa

# params
sample_rate = 44100.0 #frames
duration = 1.0  # seconds

#List of notes
notes = ['A4', 'B4', 'C5', 'D5', 'E5']

#Initialize audio signal
audio = np.array([], dtype=np.int16)

#generate the audio signal for each note
for note in notes:
    frequency = librosa.note_to_hz(note)

    #generate the time values for one cycle of the wave
    t = np.arange(int(sample_rate * duration))

    #generate the audio signal for the note
    y = 0.5 * np.sin(2 * np.pi * frequency * t / sample_rate)

    #normalize to keep within 16 but range so audio is not clipped
    y = y * 32767 / np.max(np.abs(y))

    #convert to 16-bit data
    y = y.astype(np.int16)

    #concatenate the note to the end of audio signal
    audio = np.concatenate((audio, y))

with wave.open('../output1.wav', 'w') as wav_file:
    wav_file.setparams((1, 2, int(sample_rate), len(audio), 'NONE', 'noncompressed'))
    wav_file.writeframes(audio.tobytes())

    import librosa

    frequency = librosa.note_to_hz(note)