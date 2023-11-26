"""
SCAMP Example: Hello World

Plays a C major arpeggio.
"""
# import the scamp namespace
from scamp import *
def main():
    s = Session()
    playback_settings.recording_file_path = "test.wav"
    violin = s.new_part("Violin")
    violin.play_chord([60, 64, 67, 72], 1, 1.0)


if __name__ == "__main__":
    main()