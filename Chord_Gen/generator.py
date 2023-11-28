from scamp import *


def note_to_midi(note, octave=4):
    """
    Converts a musical note and octave to its corresponding MIDI note number.

    Parameters:
    note (str): The musical note (e.g., 'C', 'D#', 'Eb', etc.).
    octave (int, optional): The octave number of the note, default is 4.

    Returns:
    int: The MIDI note number corresponding to the given note and octave.
    """

    note_values = {
        'C': 0, 'C#': 1, 'Db': 1, 'D': 2, 'D#': 3, 'Eb': 3,
        'E': 4, 'F': 5, 'F#': 6, 'Gb': 6, 'G': 7, 'G#': 8,
        'Ab': 8, 'A': 9, 'A#': 10, 'Bb': 10, 'B': 11
    }

    # Calculate the MIDI number
    midi_number = 12 * (octave + 1) + note_values[note]

    return midi_number


def note_arg(arg):
    """
    Parses a string argument to extract a musical note and optional octave,
    then converts it to a MIDI note number.

    Parameters:
    arg (str): A string representing a musical note, optionally followed by
               a comma and an octave number (e.g., 'C,4').

    Returns:
    int: The MIDI note number corresponding to the parsed note and octave.

    Raises:
    TypeError: If the input string is not in the expected format.
    """

    note = arg.split(',')
    if len(note) < 1 or len(note) > 2:
        raise TypeError(f"not a valid note: {arg}\t Length: {len(note)}")
    elif (len(note) > 1):
        return note_to_midi(note[0], int(note[1]))
    else:
        return note_to_midi(note[0], 4)


class gen_Wav:
    """
    A class for generating a WAV file with musical chords.

    Attributes:
    filename (str): The name of the output WAV file.
    s (Session): A SCAMP session for musical playback and recording.
    chordCount (int): Counter for the number of chords generated.
    duration (int): Duration of each chord in seconds.
    """
    def __init__(self, file_name):
        self.filename = file_name
        playback_settings.recording_file_path = self.filename
        self.s = Session()
        self.chordCount = 0
        self.duration = 2

    def end_session(self):
        """
        Ends the SCAMP session.
        """
        self.s.kill()

    def __del__(self):
        """
        Destructor to ensure the SCAMP session is properly ended.
        """
        self.end_session()

    def gen_chord(self, note_list, instrument, ):
        """
        Generates a chord in the WAV file.

        Parameters:
        note_list (list of int): A list of MIDI note numbers to form a chord.
        instrument (str): The name of the instrument to use for the chord.
        """
        inst = self.s.new_part(instrument)
        inst.play_chord(note_list, .9, self.duration)
        self.chordCount += 1

    def gen_multi_chords(self, chord_list, instrument):
        """
       Generates multiple chords in the WAV file.

       Parameters:
       chord_list (list of list[int]): A list of chord lists, each containing
                                         MIDI note numbers.
       instrument (str): The name of the instrument to use for the chords.
       """
        for note_list in chord_list:
            self.gen_chord(note_list, instrument)


# TODO: Build sequential chord splitter
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
