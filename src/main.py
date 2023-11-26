"""
SCAMP Example: Hello World

Plays a C major arpeggio.
"""
# import the scamp namespace
from scamp import *
from generator import note_to_midi as NM
from generator import gen_wav as GW
def main():
    GW("test2.wav", [NM("C",2), NM('E'), NM("G")], "Piano")


if __name__ == "__main__":
    main()