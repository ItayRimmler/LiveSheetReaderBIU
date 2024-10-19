"""

Script name: "src/lib/pdf/pdf.py"\n
Goal of the script: Contains the functions that process pdf files.\n
Part of project: "LiveSheetReaderBIU"\n
Description of project: Reads automatically musical sheet, and turns over pages according to the match between it and the input audio.\n
Made by: Mr. Yuval Almog and Mr. Itay Rimmler\n
Ways to contact us if something went wrong in the code: itay.rimmler@gmail.com\n
Uploaded to GitHub in the link: https://github.com/ItayRimmler?tab=repositories\n

"""

# Libraries and Imports
import os

ends_with_pdf = lambda f: f[:-4] if f[-4:] == ".pdf" else None

def list_of_pdfs():
    """
    Gives a list of pdf files inside assets:\n
    1) Creates and
    :return:
    """
    path_of_assets = os.listdir("../../../assets")
    file_index = {}
    current_index = 0
    print("Choose a file (by its number, not by its name):\n")
    for file in path_of_assets:
        if ends_with_pdf(file):
            current_index += 1
            file_index[str(current_index)] = file
    for i in range(1, 1 + current_index):
        print(f"{str(i)}. {file_index[str(i)]}\n")
    choice = input()
    tempo = input("\nWhat tempo are you going to play?\n")
    return file_index[str(choice)], 60/int(tempo)

# Script usage demonstration
if __name__ == "__main__":
    print("SCRIPT src/lib/pdf/pdf.py'S DEMONSTRATION:\n")
    list_of_pdfs()