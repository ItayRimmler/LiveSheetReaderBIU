"""

Script name: "src/lib/all/Note.py"\n
Goal of the script: Contains the Note class definition.\n
Purpose of the class: We detect each note separately, and therefore we could use a dedicated class for each note.\n
Part of project: "LiveSheetReaderBIU"\n
Description of project: Reads automatically musical sheet, and turns over pages according to the match between it and the input audio.\n
Made by: Mr. Yuval Almog and Mr. Itay Rimmler\n
Ways to contact us if something went wrong in the code: itay.rimmler@gmail.com\n
Uploaded to GitHub in the link: https://github.com/ItayRimmler?tab=repositories\n

"""

class Note:
    """
    An object that saves data regarding the note that was detected, either by sound or by image.
    """

    def __init__(self, name="Do", chain="?"):
        """
        Initializes:\n
        1) Name as "Do".\n
        2) Chain as "?".\n
        Name is going to be which type of note is it (Do\C, Re\D, etc.).\n
        Chain is going to be which chain index it is a part of.\n
        """
        self.name = name
        self.chain = chain

def get_names(l):
    """
    Returns the list of every name in l.
    :param l: *a list of Note objects
    :return: A list of strings.
    """
    temp = []
    for item in l:
        temp.append(item.name)
    return temp