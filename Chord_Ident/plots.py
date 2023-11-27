import numpy as np
import pandas as pd
import pickle as pl
from matplotlib import pyplot as plt
from numpy.fft import fftfreq
from scipy.io import wavfile
from scipy.fft import fft, fftfreq
import os

from scipy.signal import spectrogram, find_peaks

df = ""




def plot_freq_domain(y_freq, signal_f_onesided):
    # Plotting signal in time and frequency domains
    fig, axes = plt.subplots(1, 2, figsize=(12, 7))

    axes[0].plot(y_freq, signal_f_onesided)
    axes[0].set_title("Sound Wave in Frequency Domain (No Zoom)")
    axes[0].set(xlabel='Frequency [Hz]')

    axes[1].plot(y_freq[:5000], signal_f_onesided[:5000])
    axes[1].set_title("Sound Wave in Frequency Domain (Zoomed)")
    axes[1].set(xlabel='Frequency [Hz]')
    fig.tight_layout()
    plt.show()




def plot_time_domain(time, audio, N):
    fig, axes = plt.subplots(1, 2, figsize=(12, 7))
    axes[0].plot(time, audio)
    axes[0].set_title("Sound Wave in Time Domain (No Zoom)")
    axes[0].set(xlabel='Time [sec]')

    axes[1].plot(time[(N // 2):(N // 2 + 480)], audio[(N // 2):(N // 2 + 480)])
    axes[1].set_title("Sound Wave in Time Domain (Zoomed)")
    axes[1].set(xlabel='Time [sec]')
    fig.tight_layout()
    plt.show()


def graph_spectogram(fs, audio):
    f, t, Sxx = spectrogram(audio, fs, nperseg=10000, nfft=50000)

    # Plots
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    axes[0].pcolormesh(t, f, np.log(Sxx), cmap="jet")
    axes[0].set_title("Spectogram (No Zoom)")
    axes[0].set(xlabel='Time [sec]', ylabel='Frequency [Hz]')
    axes[1].pcolormesh(t, f[:1500], np.log(Sxx)[:1500, :], cmap="jet")
    axes[1].set_title("Spectogram (Zoomed)")
    axes[1].set(xlabel='Time [sec]', ylabel='Frequency [Hz]')
    plt.show()


def plots(index):
    audio = df.at[index, 'audio']
    fft = df.at[index, 'fft']
    fs = df.at[index, 'fs']
    N = len(audio)
    freq = df.at[index, 'freq']
    time = np.linspace(0., N / fs, N)

    plot_time_domain(time, audio, N)

    plot_freq_domain(freq, fft)

    graph_spectogram(fs, audio)






if __name__ == "__main__":
    df = pd.read_pickle('wavs/processed_data.pickle')
    print(df.dtypes)
    plots(1)
