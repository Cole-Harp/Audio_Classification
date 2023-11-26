from scamp import *

s = Session()
s.tempo = 120

piano = s.new_part("piano")

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

def gen_wav(file_name, notes, instrument, duration = 2.0):
    s = Session()
    playback_settings.recording_file_path = file_name
    violin = s.new_part(instrument)
    violin.play_chord(notes, 1, duration)
    s.kill()
