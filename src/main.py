import sys
import argparse
from generator import charInt_to_midi as CIM
from generator import gen_wav as GW
from generator import *

def main(args):
    parser = argparse.ArgumentParser(description='generate wav from notes.')
    parser.add_argument('-o','--output',type=str, default="output.wav", required=False)
    parser.add_argument('-n','--notes',action="extend", type=note, nargs='+', required=True)
    temp = parser.parse_args(args)
    print(temp)
    #GW([CIM("F",2), CIM('E'), CIM("G")], "Piano")

if __name__ == "__main__":
    main(sys.argv)