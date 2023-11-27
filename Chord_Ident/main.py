import numpy as np
import pandas as pd

from vars import instruments, chords

# [Instrument , Chords(A,G,F),
def gen_data():

    data_table = []
    for i in range(0,len(instruments)):
        for j in range(0,len(chords)):
            data_table.append([instruments[i],chords[j]])
    df = pd.DataFrame(data=data_table)
    return df

print(gen_data())