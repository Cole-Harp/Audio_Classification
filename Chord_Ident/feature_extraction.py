
import numpy as np
import os
from scipy.io import wavfile
import matplotlib.pyplot as plt
class Data:
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