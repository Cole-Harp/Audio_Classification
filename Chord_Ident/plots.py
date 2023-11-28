import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.signal import spectrogram, find_peaks


class Plotting:
    """
    Class for plotting various representations of audio data.

    Attributes:
    df (DataFrame): Pandas DataFrame containing audio data and related information.
    """

    def __init__(self, df):
        self.df = df

    @staticmethod
    def plot(self, index, time, audio, N, freq, fft, fs, peaks):
        # TODO: Make not static so it can be prepared for more graphs

        fig = plt.figure(figsize=(12, 8))
        fig.suptitle(f"Notes: {df.at[index, 'notes']} - Instrument: {df.at[index,'instrument']}\nIndex: {index} - Wav File: {df.at[index, 'filename']}")
        # Manually add subplots
        ax1 = fig.add_subplot(4, 2, 1)  # Top-left
        ax2 = fig.add_subplot(4, 2, 2)  # Top-right
        ax3 = fig.add_subplot(4, 2, 3)  # Middle-left
        ax4 = fig.add_subplot(4, 2, 4)  # Middle-right
        ax5 = fig.add_subplot(4, 2, 5)  # Bottom-left
        ax6 = fig.add_subplot(4, 2, 6)  # Bottom-right
        ax7 = fig.add_subplot(4,2, (7,8))  # This can span the entire bottom row

        # Plotting as before
        ax1.plot(time, audio)
        ax1.set_title("Sound Wave in Time Domain (No Zoom)")
        ax1.set(xlabel='Time [sec]')

        ax2.plot(time[(N // 2):(N // 2 + 480)], audio[(N // 2):(N // 2 + 480)])
        ax2.set_title("Sound Wave in Time Domain (Zoomed)")
        ax2.set(xlabel='Time [sec]')

        ax3.plot(freq, fft)
        ax3.set_title("Sound Wave in Frequency Domain (No Zoom)")
        ax3.set(xlabel='Frequency [Hz]')

        ax4.plot(freq[:5000], fft[:5000])
        ax4.set_title("Sound Wave in Frequency Domain (Zoomed)")
        ax4.set(xlabel='Frequency [Hz]')

        # Peaks plot
        i = peaks.max() + 100
        ax7.plot(freq[:i], fft[:i])
        ax7.plot(freq[peaks], fft[peaks], "x")
        ax7.set_title("Peaks in Frequency Domain")
        ax7.set(xlabel='Frequency [Hz]')

        # Spectrogram plots
        f, t, Sxx = spectrogram(audio, fs, nperseg=10000, nfft=50000)
        ax5.pcolormesh(t, f, np.log(Sxx), cmap="jet")
        ax5.set_title("Spectogram (No Zoom)")
        ax5.set(xlabel='Time [sec]', ylabel='Frequency [Hz]')

        ax6.pcolormesh(t, f[:1500], np.log(Sxx)[:1500, :], cmap="jet")
        ax6.set_title("Spectogram (Zoomed)")
        ax6.set(xlabel='Time [sec]', ylabel='Frequency [Hz]')

        plt.tight_layout()
        plt.show()

    def plots(self, index):
        audio = self.df.at[index, 'audio']
        fft = self.df.at[index, 'fft']
        fs = self.df.at[index, 'fs']
        N = len(audio)
        freq = self.df.at[index, 'freq']
        time = np.linspace(0., N / fs, N)
        peaks = self.df.at[index, 'peaks']

        self.plot(index, time, audio, N, freq, fft, fs, peaks)


if __name__ == "__main__":
    df = pd.read_pickle('wavs/processed_data.pickle')
    p = Plotting(df)
    p.plots(2)
