"""

Script name: "src/lib/audio/Sound.py"\n
Goal of the script: Contains the Sound class definition.\n
Goal of the class: Focus all possible actions (methods) and data pieces (data members) about our sound settings into one convenient object.\n
Part of project: "LiveSheetReaderBIU"\n
Description of project: Reads automatically musical sheet, and turns over pages according to the match between it and the input audio.\n
Made by: Mr. Yuval Almog and Mr. Itay Rimmler\n
Ways to contact us if something went wrong in the code: itay.rimmler@gmail.com\n
Uploaded to GitHub in the link: https://github.com/ItayRimmler?tab=repositories\n

"""

# Libraries and Imports
import sounddevice as sd
from sys import argv as av
import numpy as np

class Sound:
    """
    An object that saves and controls our audio.
    """

    def __init__(self, tempo=1, dur=1, sr=44100, mat=np.float64):
        """
        Initializes:\n
        1) Tempo.\n
        2) Values as None.\n
        3) Notes as None.\n
        Tempo is given by the user.\n
        Values are going to be the values of the STFT of the recorded sound.\n
        Notes are going to be the labels of notes that were recognized in the recorded sound.\n
        Dur is the duration of recording.\n
        Sr is the sample-rate of the recording.\n
        """
        self.tempo = tempo
        self.values = None
        self.notes = None
        self.dur = dur
        self.sr = sr
        self.format = mat

    def record(self):
        """
        Records IN MONO audio in an expected tempo, for a duration and in a sr.
        """
        self.values = sd.rec(int(self.dur * self.sr), self.sr, 1)
        sd.wait()

    def bin_write(self, path="../../../data/recording.bin"):
        """
        Saves values as a .bin file.
        """
        with open(path, 'wb') as file:
            self.values.astype(self.format).tofile(file)

    def bin_read(self, path="../../../data/recording.bin"):
        """
        Reads a bin file and save its values in the object.
        """
        with open(path, 'rb') as file:
            self.values = np.fromfile(file, dtype=self.format).reshape(-1,1)

    """
    
    Methods only for demonstrations and experiments:
    
    """

    def play(self):
        """
        Plays what you recorded.
        """
        if __name__ == "__main__" or av[0].endswith("area51.py"):
            sd.play(self.values, self.sr)
            sd.wait()

# Script usage demonstration
if __name__ == "__main__":
    print("SCRIPT src/lib/audio/Sound.py'S DEMONSTRATION:\n")
    ExampleSound = Sound(dur=3)
    ExampleSound.record()
    temp = ExampleSound.values.astype(ExampleSound.format)
    ExampleSound.bin_write()
    ExampleSound.bin_read()
    if np.sum(temp - ExampleSound.values) == 0:
        print("Success!")
        ExampleSound.play()
