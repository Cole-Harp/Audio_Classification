import IPython
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from numpy.fft import fftfreq
from scipy.io import wavfile
from scipy.fft import fft, fftfreq


import os
def fft_process(dir_path):
    print(dir_path)
    #fft(dir_path)

    fs, data = wavfile.read(os.path.join(dir_path))  # load the data
    audio = data.T[0]  # this is a two channel soundtrack, get the first track

    # FFT_WINDOW_SIZE = int(fs * FFT_WINDOW_SECONDS)
    # AUDIO_LENGTH = len(audio) / fs
    # fs, signala = wavfile.read(dir_path)
    # signal=signala[0]

    N = len(audio)
    time = np.linspace(0., N / fs, N)

    # Fourier Transform
    y_freq = fftfreq(N, 1 / fs)[:N // 2]  # array for frequency stamps
    signal_f = fft(audio)  # Signal in frequency domain
    signal_f_onesided = 2.0 / N * np.abs(signal_f[0:N // 2])  # taking positive terms

    # Plotting signal in time and frequency domains
    fig, axes = plt.subplots(2, 2, figsize=(12, 7))
    axes[0, 0].plot(time, audio)
    axes[0, 0].set_title("Sound Wave in Time Domain (No Zoom)")
    axes[0, 0].set(xlabel='Time [sec]')
    axes[0, 1].plot(y_freq, signal_f_onesided)
    axes[0, 1].set_title("Sound Wave in Frequency Domain (No Zoom)")
    axes[0, 1].set(xlabel='Frequency [Hz]')
    axes[1, 0].plot(time[(N // 2):(N // 2 + 480)], audio[(N // 2):(N // 2 + 480)])
    axes[1, 0].set_title("Sound Wave in Time Domain (Zoomed)")
    axes[1, 0].set(xlabel='Time [sec]')
    axes[1, 1].plot(y_freq[:5000], signal_f_onesided[:5000])
    axes[1, 1].set_title("Sound Wave in Frequency Domain (Zoomed)")
    axes[1, 1].set(xlabel='Frequency [Hz]')
    fig.tight_layout()
    plt.show()

def proccess_wav(df):
    # print(df)
    # df['num_notes'] = df["notes"].apply(lambda x: len(x))
    for index, row in df.iterrows():
        # print(row["filename"])
        fft_process(row['filename'])
    print(df)




if __name__ == "__main__":
    data=pd.read_pickle('wavs/data.pickle')
    data = data.drop(["command"], axis=1)
    proccess_wav(data.iloc[1:3])
