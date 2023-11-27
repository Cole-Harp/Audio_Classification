import argparse
import time

from feature_extraction import Data
from generator import gen_Wav, note_arg, split_wav_from_gen


def main2():

    #fft('test2_chord_1.wav')
    d = Data('test_chord_1.wav')
    d2 = Data('test_chord_2.wav')
    d.plot()
    d2.plot()
    d.gen_fft()
    d2.gen_fft()
    d.plot_fft()
    d2.plot_fft()



def main(raw_args):
    parser = argparse.ArgumentParser(description='generate wav from notes.')
    parser.add_argument('-o','--outwav',action='store',type=str, default="output.wav", required=True)
    parser.add_argument('-n','--notes',action="extend", type=note_arg, nargs='+', required=False)
    args = parser.parse_args(raw_args)

    GW = gen_Wav(args.outwav)
    notes = [["C", 'E', 'G', 'F'], ['A', 'C', 'G']]
    notes_midi =[]
    for i in range(0, len(notes)):
        notes_midi.append([])
        for j in range(0,len(notes[i])):
            notes_midi[i].append(note_arg(notes[i][j]))

    GW.gen_multi_chords(notes_midi, "Piano")
    GW.gen_multi_chords(notes_midi, "Violin")
    GW.gen_multi_chords(notes_midi, "Organ")
    time.sleep(10)
    d = Data('test.wav')
    d.plot()
    split_wav_from_gen(GW)




if __name__ == "__main__":
    main(["-o","test.wav"])