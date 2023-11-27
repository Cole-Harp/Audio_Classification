from unittest import TestCase
import src


class Test(TestCase):
    def test_main(self):
        args = "-o output.wav -n C,4 E,4 G,4 "
        src.main(args)
