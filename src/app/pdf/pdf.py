"""

Script name: "src/app/pdf/pdf.py"\n
Goal of the script: Contains the main function that processes pdf files.\n
Part of project: "LiveSheetReaderBIU"\n
Description of project: Reads automatically musical sheet, and turns over pages according to the match between it and the input audio.\n
Made by: Mr. Yuval Almog and Mr. Itay Rimmler\n
Ways to contact us if something went wrong in the code: itay.rimmler@gmail.com\n
Uploaded to GitHub in the link: https://github.com/ItayRimmler?tab=repositories\n

"""

# Libraries and Imports
import src.lib.pdf.pdf as pdf

def process():
    file, tempo = pdf.list_of_pdfs()
    return file, tempo

# Script usage demonstration
if __name__ == "__main__":
    print("SCRIPT src/app/pdf/pdf.py'S DEMONSTRATION:\n")
    process()