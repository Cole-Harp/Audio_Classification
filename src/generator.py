import argparse

from scamp import Session

def note(arg):
    p = arg.split(',')
    if(len(p<1) or len(p)>2):
        raise argparse.ArgumentError(f"not a valid note: {arg}\n\tLength: {len(p)}")
    return (p[0], int(p[1]))
def note_to_mide(note):
    if(len(note)==1):
        return charInt_to_midi(note[0])
    elif(len(note) == 2):
        return charInt_to_midi(note[0], note[1])
    else:
        raise Exception("note list wrong")
def charInt_to_midi(note, octave=4):
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

