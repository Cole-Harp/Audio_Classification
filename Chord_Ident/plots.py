import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.fft import fft


from scipy.signal import spectrogram, find_peaks


class Plotting:

    def __init__(self, df):
        self.df=df
    def plot(self, time, audio, N, freq, fft, fs):
        # Plotting signal in time domain

        fig, axes = plt.subplots(3, 2, figsize=(12, 8))

        axes[0, 0].plot(time, audio)
        axes[0, 0].set_title("Sound Wave in Time Domain (No Zoom)")
        axes[0, 0].set(xlabel='Time [sec]')

        axes[0, 1].plot(time[(N // 2):(N // 2 + 480)], audio[(N // 2):(N // 2 + 480)])
        axes[0, 1].set_title("Sound Wave in Time Domain (Zoomed)")
        axes[0, 1].set(xlabel='Time [sec]')

        # Plotting signal in freq domain

        axes[1, 0].plot(freq, fft)
        axes[1, 0].set_title("Sound Wave in Frequency Domain (No Zoom)")
        axes[1, 0].set(xlabel='Frequency [Hz]')

        axes[1, 1].plot(freq[:5000], fft[:5000])
        axes[1, 1].set_title("Sound Wave in Frequency Domain (Zoomed)")
        axes[1, 1].set(xlabel='Frequency [Hz]')

        # Plotting signal in spectogram

        f, t, Sxx = spectrogram(audio, fs, nperseg=10000, nfft=50000)

        # Plots

        axes[2, 0].pcolormesh(t, f, np.log(Sxx), cmap="jet")
        axes[2, 0].set_title("Spectogram (No Zoom)")
        axes[2, 0].set(xlabel='Time [sec]', ylabel='Frequency [Hz]')
        axes[2, 1].pcolormesh(t, f[:1500], np.log(Sxx)[:1500, :], cmap="jet")
        axes[2, 1].set_title("Spectogram (Zoomed)")
        axes[2, 1].set(xlabel='Time [sec]', ylabel='Frequency [Hz]')
        fig.tight_layout()
        plt.show()


    def plots(self, index):
        audio = self.df.at[index, 'audio']
        fft = self.df.at[index, 'fft']
        fs = self.df.at[index, 'fs']
        N = len(audio)
        freq = self.df.at[index, 'freq']
        time = np.linspace(0., N / fs, N)

        self.plot(time, audio, N, freq, fft, fs)


if __name__ == "__main__":
    df = pd.read_pickle('wavs/processed_data.pickle')
    p = Plotting(df)
    p.plots(2)
