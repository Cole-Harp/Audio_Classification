import numpy as np
import pandas as pd
import subprocess
from vars import instruments, chords

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
                name = f"{k}.wav"
                command = f"-o {name} -n {self.chordToCommand(chord)} -i {inst}"
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
        return out

    def make_wav(self):
        for comd in self.data['command']:
            print(comd)
            subprocess.run(f"")
def main():
    DG = DataGen()
    #print(DG.data)
    DG.make_wav()

if __name__ == "__main__":
    main()