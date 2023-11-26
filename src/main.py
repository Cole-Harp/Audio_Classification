import sys
import argparse
from generator import note_to_midi as NM
from generator import gen_wav as GW

def main():
    parser = argparse.ArgumentParser(description='generate wav from notes.')
    parser.add_argument('-n')




    GW([NM("F",2), NM('E'), NM("G")], "Piano")



if __name__ == "__main__":
    main()