"""

Script name: "src/app/all/main.py"\n
Goal of the script: Contains the main function that runs the program.\n
Part of project: "LiveSheetReaderBIU"\n
Description of project: Reads automatically musical sheet, and turns over pages according to the match between it and the input audio.\n
Made by: Mr. Yuval Almog and Mr. Itay Rimmler\n
Ways to contact us if something went wrong in the code: itay.rimmler@gmail.com\n
Uploaded to GitHub in the link: https://github.com/ItayRimmler?tab=repositories\n

"""

# Libraries and Imports
from src.lib.all.State import State
from src.app.pdf import pdf
from src.lib.audio.Sound import Sound

Event = State()
file_path, tempo = pdf.process()
sound = Sound()
