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


def find_harmonics(path, print_peaks=False):
    fs, X = wavfile.read(path)
    N = len(X)
    X_F = fft(X)
    X_F_onesided = 2.0 / N * np.abs(X_F[0:N // 2])
    freqs = fftfreq(N, 1 / fs)[:N // 2]
    freqs_50_index = np.abs(freqs - 50).argmin()

    h = X_F_onesided.max() * 5 / 100
    peaks, _ = find_peaks(X_F_onesided, distance=10, height=h)
    peaks = peaks[peaks > freqs_50_index]
    harmonics = np.round(freqs[peaks], 2)

    if print_peaks:
        i = peaks.max() + 100
        plt.plot(freqs[:i], X_F_onesided[:i])
        plt.plot(freqs[peaks], X_F_onesided[peaks], "x")
        plt.xlabel('Frequency [Hz]')
        plt.show()
    return harmonics


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
    signal = df.at[index, 'true_signal']
    audio = df.at[index, 'audio']
    fft = df.at[index, 'fft']
    fs = df.at[index, 'fs']
    N = df.at[index, 'length']
    y_freq = df.at[index, 'y_freq']
    time = np.linspace(0., N / fs, N)

    # Fourier Transform
     # y_freq = fftfreq(N, 1 / fs)[:N // 2]  # array for frequency stamps
    fft_onesided = 2.0 / N * np.abs(fft[0:N // 2])  # taking positive terms

    plot_time_domain(time, signal, N)

    plot_freq_domain(y_freq, fft_onesided)

    graph_spectogram(fs, audio)






if __name__ == "__main__":
    df = pd.read_pickle('wavs/final_data.pickle')
    print(df.dtypes)
    plots(1)
