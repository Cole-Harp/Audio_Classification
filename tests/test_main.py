from unittest import TestCase
from Chord_Gen import main


class Test(TestCase):
    def test_main(self):
        args = ["-o","test1.wav",'-n', "C,3", "E,4", "G,5", "F,2" , "-i", "Oboe"]
        main(args)
