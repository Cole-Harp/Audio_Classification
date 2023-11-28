import numpy as np
import os
from scipy.io import wavfile
import matplotlib.pyplot as plt


class Data:
    """
    Class for processing and visualizing audio data from a WAV file.

    Attributes:
    fft (ndarray): The Fast Fourier Transform of the audio data.
    fs (int): Sampling frequency of the audio file.
    data (ndarray): Raw audio data read from the WAV file.
    audio (ndarray): Mono audio data (first channel if stereo).
    length (float): Duration of the audio in seconds.

    Methods:
    plot(): Plots the audio waveform over time.
    gen_fft(): Generates the FFT of the audio data.
    plot_fft(): Plots the real part of the FFT.
    """

    def __init__(self, wav_file):
        self.fft = None
        self.fs, self.data = wavfile.read(wav_file)
        self.audio = self.data.T[0]
        self.length = self.data.shape[0] / self.fs

    def plot(self):
        time = np.linspace(0., self.length, self.data.shape[0])
        plt.plot(time, self.audio, label="Sound")
        plt.legend()
        plt.xlabel("Time [s]")
        plt.ylabel("Amplitude")
        plt.show()

    def gen_fft(self):
        self.fft = np.fft.rfft(self.audio)

    def plot_fft(self):
        plt.plot(self.fft.real)
        plt.show()
