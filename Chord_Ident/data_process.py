import sys

import IPython
import numpy as np
import pandas as pd
import pickle as pl
from matplotlib import pyplot as plt
from numpy.fft import fftfreq
from scipy.io import wavfile
from scipy.fft import fft, fftfreq
import os

df = ""
def fft_process(index):
    try:
        path = df.at[index,'filename']
        print(path)

        fs, data = wavfile.read(os.path.join(path))  # load the data
        audio = data.T[0]  # this is a two channel soundtrack, get the first track

        N = len(audio)
        time = np.linspace(0., N / fs, N)

        # Fourier Transform
        y_freq = fftfreq(N, 1 / fs)[:N // 2]  # array for frequency stamps
        signal_f = fft(audio)  # Signal in frequency domain
        signal_f_onesided = 2.0 / N * np.abs(signal_f[0:N // 2])  # taking positive terms

        # Plotting signal in time and frequency domains
        # fig, axes = plt.subplots(2, 2, figsize=(12, 7))
        # axes[0, 0].plot(time, audio)
        # axes[0, 0].set_title("Sound Wave in Time Domain (No Zoom)")
        # axes[0, 0].set(xlabel='Time [sec]')
        # axes[0, 1].plot(y_freq, signal_f_onesided)
        # axes[0, 1].set_title("Sound Wave in Frequency Domain (No Zoom)")
        # axes[0, 1].set(xlabel='Frequency [Hz]')
        # axes[1, 0].plot(time[(N // 2):(N // 2 + 480)], audio[(N // 2):(N // 2 + 480)])
        # axes[1, 0].set_title("Sound Wave in Time Domain (Zoomed)")
        # axes[1, 0].set(xlabel='Time [sec]')
        # axes[1, 1].plot(y_freq[:5000], signal_f_onesided[:5000])
        # axes[1, 1].set_title("Sound Wave in Frequency Domain (Zoomed)")
        # axes[1, 1].set(xlabel='Frequency [Hz]')
        # fig.tight_layout()
        # plt.show()

        return (signal_f, signal_f_onesided, audio, fs, N, y_freq)
    except:
        return (None, None, None, None, None, None)

# def harmonic_process(index)

def fft_full():
    df['audio'] = ""
    df['true_signal'] = ""
    df['fft'] = ""
    df['fs'] = ""
    df['length'] = ""
    df['y_freq'] = ""
    for index in range(len(df)):
        # print(row["filename"])
        temp = fft_process(index)
        df.at[index, 'true_signal'] = temp[0]
        df.at[index, 'fft'] = temp[1]
        df.at[index, 'audio'] = temp[2]
        df.at[index, 'fs'] = temp[3]
        df.at[index, 'length'] = temp[4]
        df.at[index, 'y_freq'] = temp[5]


def df_print():
    print(df)
    print(df.dtypes)
def proccess():
    # print(df)
    df['num_notes'] = df["notes"].apply(lambda x: len(x))
    fft_full()
    df.dropna()
    df_print()

    df.to_pickle("wavs/final_data.pickle")




if __name__ == "__main__":
    df =pd.read_pickle('wavs/data.pickle')
    df = df.drop(["command"], axis=1)
    proccess()
