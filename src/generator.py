import scamp.simple
from scamp import Session

def note_to_midi(note, octave=4):
    # Define the note values
    note_values = {
        'C': 0, 'C#': 1, 'Db': 1, 'D': 2, 'D#': 3, 'Eb': 3,
        'E': 4, 'F': 5, 'F#': 6, 'Gb': 6, 'G': 7, 'G#': 8,
        'Ab': 8, 'A': 9, 'A#': 10, 'Bb': 10, 'B': 11
    }

    # Calculate the MIDI number
    midi_number = 12 * (octave + 1) + note_values[note]

    return midi_number

def gen_wav( notes, instrument, duration = 2.0):

    s = Session()
    inst = s.new_part(instrument)
    inst.play_chord(notes, .9,duration)
    s.kill()

