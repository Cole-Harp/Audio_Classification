import sys

from IPython.display import display
import numpy as np
import pandas as pd
import pickle as pl
from matplotlib import pyplot as plt
from numpy.fft import fftfreq
from scipy.io import wavfile
from scipy.fft import fft, fftfreq
from scipy.signal import spectrogram, find_peaks
import os

df = ""
def fft_process(index):
    try:
        path = df.at[index,'filename']
        #print(path)

        fs, data = wavfile.read(os.path.join(path))  # load the data
        audio = data.T[0]  # this is a two channel soundtrack, get the first track

        N = len(audio)
        time = np.linspace(0., N / fs, N)

        # Fourier Transform
        y_freq = fftfreq(N, 1 / fs)[:N // 2]  # array for frequency stamps
        signal_f = fft(audio)  # Signal in frequency domain
        signal_f_onesided = 2.0 / N * np.abs(signal_f[0:N // 2])  # taking positive terms

        return (signal_f_onesided, y_freq, audio)
    except:
        print(f"error at: {index}")
        return (None, None, None)

def harmonic_process(index):
    print(df.at[index, 'fft'])
    signal_f_onesided = df.at[index, 'fft']
    y_freq = df.at[index, 'freq']
    h = signal_f_onesided.max() * 5 / 100
    peaks, _ = find_peaks(signal_f_onesided, distance=10, height=h)

    freq_50_index = np.abs(y_freq - 50).argmin()  # finding index for 50 Hz
    peaks = peaks[peaks > freq_50_index]  # filtering peaks less than 50 Hz
    harmonics = y_freq[peaks]

    return peaks

def harmonic_full():
    df['peaks'] = ""
    for index in range(len(df)):
        df.at[index, 'peaks'] = harmonic_process(index)
def fft_full():
    df['audio'] = ""
    df['fft'] = ""
    df['freq'] = ""
    for index in range(len(df)):
        temp = fft_process(index)
        df.at[index, 'fft'] = temp[0]
        df.at[index, 'freq'] = temp[1]
        df.at[index, 'audio'] = temp[2]

def df_print():
    display(df)
    print(df.dtypes)
def proccess_wav():
    # print(df)
    df['num_notes'] = df["notes"].apply(lambda x: len(x))
    fft_full()
    df.dropna(inplace=True)
    harmonic_full()
    df_print()
    df.to_pickle('wavs/processed_data.pickle')


if __name__ == "__main__":
    df=pd.read_pickle('wavs/data.pickle')
    df = df[0:12]
    df = df.drop(["command"], axis=1)
    proccess_wav()
