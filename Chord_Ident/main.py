import numpy as np
import pandas as pd
import subprocess
from vars import instruments, chords
from concurrent.futures import ThreadPoolExecutor


class DataGen:
    """
    Class for generating audio data

    Attributes:
    data (DataFrame): A Pandas DataFrame holding the generated data including instrument names,
                      chords, filenames, and commands used for audio generation.

    Methods:
    gen_data_1(): Generates the initial data table with combinations of instruments and chords.
    make_wav_parallel(max_workers=5): Generates WAV files in parallel based on the commands
    """
    def __init__(self):
        self.data = pd.DataFrame()
        self.gen_data_1()

    def gen_data_1(self):
        """
        Generates the initial data table with combinations of instruments and chords.
        """
        data_table = []
        k = 0
        for i in range(0, len(instruments)):
            for j in range(0, len(chords)):
                inst = instruments[i]
                chord = chords[j]
                name = f"wavs/{k}.wav"
                command = f"-o {name} -i {inst} -n {self.chord_to_command(chord)}"
                data_table.append([inst, chord, name, command])
                k += 1
        df = pd.DataFrame(data=data_table)
        df.set_axis(['instrument', 'notes', 'filename', 'command'], axis='columns', inplace=True)
        self.data = df

    @staticmethod
    def chord_to_command(chord):
        """
        Converts a chord (list of MIDI note numbers) to a command string.

        Parameters:
        chord (list[int]): A list of MIDI note numbers representing a chord.

        Returns:
        str: A command string that can be used to generate audio for the chord.
        """
        out = ""
        for x in chord:
            out += f"{x} "
        return out[:-1]

    def make_wav_parallel(self, max_workers=5):
        """
        Generates WAV files in parallel based on the commands in the 'data' DataFrame.

        Parameters:
        max_workers (int): The maximum number of parallel workers for generating WAV files.
        """
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(self.run_subprocess, comd) for comd in self.data['command']]
            for future in futures:
                future.result()

    @staticmethod
    def run_subprocess(command):
        """
        Executes a subprocess to generate a WAV file based on the provided command.

        It was done this way because Sessions from scamp had to be compartmentalized.
        There is probably a better way to do this.
        """
        print(command)
        subprocess.run(f"Python ../Chord_Gen/main.py {command}")


def main():
    DG = DataGen()
    # print(DG.data)
    DG.data.to_pickle('wavs/data.pickle')
    DG.make_wav_parallel()


if __name__ == "__main__":
    main()
