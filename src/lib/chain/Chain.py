"""

Script name: "src/lib/chain/Chain.py"\n
Goal of the script: Contains the Chain class definition.\n
Purpose of the class: The purpose of chains should be explained somewhere obvious (like the Readme). If it isn't contact us immediately.\n
Part of project: "LiveSheetReaderBIU"\n
Description of project: Reads automatically musical sheet, and turns over pages according to the match between it and the input audio.\n
Made by: Mr. Yuval Almog and Mr. Itay Rimmler\n
Ways to contact us if something went wrong in the code: itay.rimmler@gmail.com\n
Uploaded to GitHub in the link: https://github.com/ItayRimmler?tab=repositories\n

"""
from itertools import accumulate

# Libraries and Imports
from src.lib.all.Note import get_names
class Chain:
    """
    An object that saves data regarding the chain of notes.
    """

    def __init__(self, id="?", content=None):
        """
        Initializes:\n
        1) Id as "0a".\n
        2) Content as an empty list.\n
        3) Score as 1.\n
        Id is the... ID of the chain, starting with page number, then alphabetically ordered with the other chains in the page.\n
        NOTES: Id shall be "?" if its unknown what page are we in, and "X?" if the page number is known (and is X) and we don't know the position of the chain within the page.\n
        Content is the... content of the chain, a list with Note objects.\n
        Score is how many "points" the chain is worth, which is a measurement of how similar is the sound to the image.\n
        """
        self.id = id
        self.content = content
        if self.content is None:
            self.content = []
        self.score = 1

    def match(self, other):
        """
        Matches other* with the calling object, updates score accordingly.\n
        It's too difficult to explain the algorithm, I've worked a lot on it. It's even hard with examples. Try it out with some examples or understand the code by yourself if you're the future me or if you're a curious individual.\n
        :param other: *another Chain
        """
        b = self.content
        a = other.content
        matches = []
        continuity = []
        while len(a) and len(b):
            for j in range(len(b)):
                if b[j] in a:
                    that = b[j]
                    if a.index(that) > 0:
                        matches.append("-")
                        continuity.append(0)
                    matches.append(that)
                    continuity.append(1)
                    del b[j]
                    del a[0:a.index(that) + 1]
                    break
                else:
                    matches.append("-")
                    continuity.append(0)
                    if j == len(b) - 1:
                        del a[0]
        new_continuity = [continuity[0]]
        while continuity[-1] == 0:
            del continuity[-1]
        for i in continuity:
            if not bool(i) != bool(new_continuity[-1]):
                new_continuity[-1] += i
            else:
                new_continuity.append(i)
        if new_continuity[0] > 0:
            new_continuity[0] -= 1
        self.score = formula(new_continuity, len(other.content), len(self.content))

    def set_content(self, content):
        """
        Sets self.content to be the names of content*.
        :param content: *a list of Notes.
        :return: content, but with id's set correctly.
        """
        self.content = get_names(content)
        for c in content:
            c.chain = self.id
        return content

def formula(l, n, m):
    """
    Credit to ChatGPT for creating the first version of the formula. The initial formula's parameters or the formula itself may be altered multiple times.\n
    """
    # Initialize score
    score = 0
    zero_penalty = -1  # Penalty for each internal "0"
    continuity_bonus = 1  # Multiplier for rewarding continuity

    for elem in l:
        if elem == 0:
            score += zero_penalty  # Penalize interruptions
        else:
            score += (elem ** 2) * continuity_bonus  # Reward continuous subsequences

    return (1 - abs(m - n)/max(m, n))*score/(n**2)


