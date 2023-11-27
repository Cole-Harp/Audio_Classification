from scamp import *


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


def gen_wav(file_name, chord_list, instrument, duration=1.0):
    midi_notes = []

    s = Session()

    playback_settings.recording_file_path = file_name

    violin = s.new_part(instrument)
    for notes in chord_list:
        for note in notes:
            midi_notes.append(note_to_midi(note))

        violin.play_chord(midi_notes, 1, duration)
        midi_notes = []

    s.kill()


import wave
import audioop


def split_wav(file_name, num_chords, chord_duration=1.0):
    with wave.open(file_name, 'rb') as w:
        params = w.getparams()
        framerate = w.getframerate()
        nframes = w.getnframes()
        audio = w.readframes(nframes)

    # Calculate the number of frames per chord
    frames_per_chord = int(framerate * chord_duration)

    # Split the audio into chunks and save as separate files
    for i in range(num_chords):
        start = i * frames_per_chord
        end = start + frames_per_chord
        chunk = audio[start:end]

        output_filename = f"{file_name[:-4]}_chord_{i + 1}.wav"
        with wave.open(output_filename, 'wb') as out:
            out.setparams(params)
            out.writeframes(chunk)
