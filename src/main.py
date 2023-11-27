import argparse
import sys
import time

from .generator import gen_Wav,note_arg
from .feature_extraction import Data


def main(raw_args):
    parser = argparse.ArgumentParser(description='generate wav from notes.')
    parser.add_argument('-o', '--outwav', action='store', type=str, required=True)
    parser.add_argument('-n', '--notes', action="extend", type=note_arg, nargs='+', required=True)
    parser.add_argument('-i', "--instrument", action='store', type=str, default='Violin')
    args = parser.parse_args(raw_args)

    GW = gen_Wav(args.outwav)
    GW.gen_chord(args.notes, args.instrument)


if __name__ == "__main__":
    main(sys.argv)