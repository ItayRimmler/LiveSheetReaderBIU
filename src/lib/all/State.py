"""

Script name: "src/lib/all/State.py"\n
Goal of the script: Contains the State class definition.\n
Goal of the class: Our program is essentially one big state machine, this is a convenient way to follow the state and previous states.\n
Part of project: "LiveSheetReaderBIU"\n
Description of project: Reads automatically musical sheet, and turns over pages according to the match between it and the input audio.\n
Made by: Mr. Yuval Almog and Mr. Itay Rimmler\n
Ways to contact us if something went wrong in the code: itay.rimmler@gmail.com\n
Uploaded to GitHub in the link: https://github.com/ItayRimmler?tab=repositories\n

"""

# Libraries and Imports


class State:
    """
    An object that saves our states of our state machine.
    """

    def __init__(self):
        """
        Initializes:\n
        1) Current state as "start".\n
        2) State's log as an empty list.\n
        3) A special number we will work with as 0.\n
        """
        self.current = "Start"
        self.log = []
        self.num = 0

    def read(self, state=True, num=False):
        """
        :return: The current state, or the current number, depends on the argument.
        """
        if state and num:
            return self.current, self.num
        elif num:
            return self.num
        return self.current

    def get_log(self):
        """
        :return: The State's log.
        """
        return self.log

    def write(self, other):
        """
        Adds other* to the State's log and setting it as the current.\n
        :param other: *a new state for our State object.
        """
        self.log.append(self.current)
        self.current = other

    def show(self):
        """
        Prints the current state and the number.
        """
        print(f"Current state: {self.current}, Current num: {self.num}\n")

    def advance(self):
        """
        Adds 1 to the number.
        """
        self.num += 1

# Script usage demonstration
if __name__ == "__main__":
    print("SCRIPT src/lib/all/State.py'S DEMONSTRATION:\n")
    ExampleState = State()
    ExampleState.show()
    what_i_wanna_read = True
    current_state, current_num = ExampleState.read(what_i_wanna_read, what_i_wanna_read)
    ExampleState.write("Finish")
    ExampleState.show()
    ExampleState.advance()
    ExampleState.show()
