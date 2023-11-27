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

def note_arg(arg):
    note = arg.split(',')
    if (len(note)<1 or len(note)>2):
        raise TypeError(f"not a valid note: {arg}\t Length: {len(note)}")
    elif (len(note)>1):
        return note_to_midi(note[0],int(note[1]))
    else:
        return note_to_midi(note[0], 4)
class gen_Wav:
    def __init__(self, file_name):
        self.filename = file_name
        playback_settings.recording_file_path = self.filename
        self.s = Session()
        self.chordCount = 0
        self.duration = 2
    def end_session(self):
        self.s.kill()
    def __del__(self):
        self.end_session()
    def gen_chord(self, note_list, instrument,):
        inst = self.s.new_part(instrument)
        inst.play_chord(note_list, .9, self.duration)
        self.chordCount += 1
    def gen_multi_chords(self, chord_list, instrument):
        for note_list in chord_list:
            self.gen_chord(note_list, instrument)


# import wave
# import audioop
#
#
# def split_wav_from_gen(gen_wav):
#     #gen_wav.duration
#     split_wav(gen_wav.filename,gen_wav.chordCount,gen_wav.duration)
# def split_wav(file_name, num_chords, chord_duration):
#     with wave.open(file_name, 'rb') as w:
#         params = w.getparams()
#         framerate = w.getframerate()
#         nframes = w.getnframes()
#         audio = w.readframes(nframes)
#
#     # Calculate the number of frames per chord
#     frameStart = int(framerate*1)
#     frames_per_chord = int(framerate * chord_duration)
#
#     # Split the audio into chunks and save as separate files
#     for i in range(num_chords):
#         start = frameStart+(i * frames_per_chord)
#         end = start + frames_per_chord
#         chunk = audio[start:end]
#
#         output_filename = f"{file_name[:-4]}_chord_{i + 1}.wav"
#         with wave.open(output_filename, 'wb') as out:
#             out.setparams(params)
#             out.writeframes(chunk)
