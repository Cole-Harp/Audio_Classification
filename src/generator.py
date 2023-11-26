from scamp import *

s = Session()
s.tempo = 120

piano = s.new_part("piano")


def note_to_midi(note, octave):
    # Define the note values
    note_values = {
        'C': 0, 'C#': 1, 'Db': 1, 'D': 2, 'D#': 3, 'Eb': 3,
        'E': 4, 'F': 5, 'F#': 6, 'Gb': 6, 'G': 7, 'G#': 8,
        'Ab': 8, 'A': 9, 'A#': 10, 'Bb': 10, 'B': 11
    }

    # Calculate the MIDI number
    midi_number = 12 * (octave + 1) + note_values[note]

    return midi_number


print(note_to_midi("D", 9))

# pitch_list = [60,64,66,69,67,64,60,57,54,54,54,55]
# durs_list = [1.5,1.0,1.0,0.5,1.5,1.0,1.0,.5,.5,.5]
#
# for pitch,duration in zip(pitch_list, durs_list):
#     piano.play_note(pitch,.8,duration)
#

# Pitch -> note
#
