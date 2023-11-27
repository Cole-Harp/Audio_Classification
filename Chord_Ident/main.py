import numpy as np
import pandas as pd
import subprocess
from vars import instruments, chords
from concurrent.futures import ThreadPoolExecutor

class DataGen:
    def __init__(self):
        self.data = pd.DataFrame()
        self.gen_data_1()

    def gen_data_1(self):
        data_table = []
        k = 0
        for i in range(0,len(instruments)):
            for j in range(0,len(chords)):
                inst = instruments[i]
                chord = chords[j]
                name = f"wavs/{k}.wav"
                command = f"-o {name} -i {inst} -n {self.chordToCommand(chord)}"
                data_table.append([inst, chord, name, command])
                k+=1
        df = pd.DataFrame(data=data_table)
        df.set_axis(['instrument', 'notes','filename','command'], axis='columns', inplace=True)
        self.data = df
    @staticmethod
    def chordToCommand(chord):
        out = ""
        for x in chord:
            out += f"{x} "
        return out[:-1]

    def make_wav_parallel(self, max_workers=5):
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(self.run_subprocess, comd) for comd in self.data['command']]
            for future in futures:
                future.result()

    @staticmethod
    def run_subprocess(command):
        print(command)
        subprocess.run(f"Python ../Chord_Gen/main.py {command}")
def main():
    DG = DataGen()
    #print(DG.data)
    DG.make_wav_parallel()

if __name__ == "__main__":
    main()