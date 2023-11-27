"""
SCAMP Example: Hello World

Plays a C major arpeggio.
"""
# import the scamp namespace
from feature_extraction import Data
from src.wav_parser import fft
from generator import gen_wav as GW, split_wav as SW
def main():
    notes = [["C", 'E', 'G', 'F'],['A', 'C', 'G']]
    #GW("test2.wav", notes, "Piano", duration=2)
    #SW('test2.wav', len(notes), 8)
    #fft('test2_chord_1.wav')
    d = Data('test2_chord_1.wav')
    d2 = Data('test2_chord_2.wav')
    d.plot()
    d2.plot()
    d.gen_fft()
    d2.gen_fft()
    d.plot_fft()
    d2.plot_fft()

def main(args):
    parser = argparse.ArgumentParser(description='generate wav from notes.')
    parser.add_argument('-o','--output',type=str, default="output.wav", required=False)
    parser.add_argument('-n','--notes',action="extend", type=note, nargs='+', required=True)
    temp = parser.parse_args(args)
    print(temp)
    #GW([CIM("F",2), CIM('E'), CIM("G")], "Piano")

if __name__ == "__main__":
    main()