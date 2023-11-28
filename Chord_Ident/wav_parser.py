

# import plotly.graph_objects as go
import numpy as np
from scipy.io import wavfile  # get the api
import os
from collections import Counter



directory = ''

# Configuration
FPS = 30
FFT_WINDOW_SECONDS = 0.25  # how many seconds of audio make up an FFT window

# Note range to display
FREQ_MIN = 10
FREQ_MAX = 1000

# Notes to display
TOP_NOTES = 5

# Names of the notes
NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

# Output size. Generally use SCALE for higher res, unless you need a non-standard aspect ratio.
RESOLUTION = (1920, 1080)
SCALE = 1  # 0.5=QHD(960x540), 1=HD(1920x1080), 2=4K(3840x2160)
path = "Uke_1.wav"


def fft(path):
    """
    Function to parse many frames of a wav file
    A start to multi chord parsing
    """
    fs, data = wavfile.read(os.path.join(directory, path))  # load the data
    audio = data.T[0]  # this is a two channel soundtrack, get the first track
    FFT_WINDOW_SIZE = int(fs * FFT_WINDOW_SECONDS)
    AUDIO_LENGTH = len(audio) / fs

    def extract_sample(audio, frame_number):
        end = frame_number * FRAME_OFFSET
        begin = int(end - FFT_WINDOW_SIZE)

        if end == 0:
            # We have no audio yet, return all zeros (very beginning)
            return np.zeros((np.abs(begin)), dtype=float)
        elif begin < 0:
            # We have some audio, padd with zeros
            return np.concatenate([np.zeros((np.abs(begin)), dtype=float), audio[0:end]])
        else:
            # Usually this happens, return the next sample
            return audio[begin:end]

    def total_frequency(notes):
        total_freq = 0
        for note in notes:
            total_freq += note[0]
        if len(notes) > 0:
            return total_freq
        else:
            return 0

    def find_top_notes(fft, num):
        if np.max(fft.real) < 0.001:
            return []

        lst = [x for x in enumerate(fft.real)]
        lst = sorted(lst, key=lambda x: x[1], reverse=True)

        idx = 0
        found = []
        found_note = set()
        while (idx < len(lst)) and (len(found) < num):
            f = xf[lst[idx][0]]
            y = lst[idx][1]
            n = freq_to_number(f)
            n0 = int(round(n))
            name = note_name(n0)

            if name not in found_note:
                found_note.add(name)
                s = [f, note_name(n0), y]
                found.append(s)
            idx += 1

        return found

    # See https://newt.phys.unsw.edu.au/jw/notes.html
    def freq_to_number(f):
        return 69 + 12 * np.log2(f / 440.0)

    def number_to_freq(n):
        return 440 * 2.0 ** ((n - 69) / 12.0)

    def note_name(n):
        return NOTE_NAMES[n % 12] + str(int(n / 12 - 1))

    # Hanning window function
    window = 0.5 * (1 - np.cos(np.linspace(0, 2 * np.pi, FFT_WINDOW_SIZE, False)))

    xf = np.fft.rfftfreq(FFT_WINDOW_SIZE, 1 / fs)
    FRAME_COUNT = int(AUDIO_LENGTH * FPS)
    FRAME_OFFSET = int(len(audio) / FRAME_COUNT)

    # Pass 1, find out the maximum amplitude, so we can scale.
    mx = 0
    for frame_number in range(FRAME_COUNT):
        sample = extract_sample(audio, frame_number)

        fft = np.fft.rfft(sample * window)
        fft = np.abs(fft).real
        mx = max(np.max(fft), mx)

    print(f"Max amplitude: {mx}")

    # Pass 2, data and maybe animation
    total_notes = []
    for frame_number in (range(FRAME_COUNT)):
        sample = extract_sample(audio, frame_number)

        fft = np.fft.rfft(sample * window)
        fft = np.abs(fft) / mx

        s = find_top_notes(fft, TOP_NOTES)
        print(s)
        note = total_frequency(s)
        total_notes.append(note)

fft('wavs/5.wav')
