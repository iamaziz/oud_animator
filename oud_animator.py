import curses
from time import sleep
from typing import List, Union, Any

from config import NOTES_MAP, MASTER_STRING_LEN, NUM_STRINGS, STRING_LEN




class OudAnimator:

    def __init__(self, speed=1):
        # self.speed: float = speed
        self.current_board: List[str] = []  # the Oud's Zend state
        self.current_master_string: List[Union[str, Any]] = []
        self.played_notes: List[str] = []

        self.screen = curses.initscr()
        curses.curs_set(0)  # hide cursor

    def __del__(self):
        curses.endwin()

    def __repr__(self):
        s = "note progress:\n"
        for n in self.played_notes:
            s += f" {n} "
        return "\n".join([s[i: i + STRING_LEN] for i in range(0, len(s), STRING_LEN)])

    # LOGIC
    def build_master_string_with_current_note(
            self, notes: Union[List[str], str]
    ) -> List[str]:
        """build a long line 'a string' to represent all the six strings of the Oud as one segment.
        This is easier for indexing (and inserting) notes.
        ::notes: list, of the notes to be played together at a time e.g [FA, Sol] or [MI]
        """
        # create the master string

        # e.g. {'FA': 0, 'Fa': 185}
        current_notes = {NOTES_MAP.get(note, None): note for note in notes}

        master_string = []
        for i in range(MASTER_STRING_LEN):
            if i in current_notes.keys():
                note = current_notes[i]
                master_string.append(note)
                self.played_notes.append(note)
            else:
                master_string.append("-")
        self.current_master_string = master_string
        return master_string

    def split_master_string_into_oud_strings(self):
        """Update the state of Oud Zend
        Split the master string into Oud strings (6) with each newly added note
        """

        strings = []
        slider = 0, STRING_LEN  # over strings
        for i in range(1, NUM_STRINGS):
            line = self.current_master_string[slider[0]: slider[1] + 1]
            slider = slider[1], slider[1] + STRING_LEN  # slide to the next string
            # trim extra dashes in the line (caused by the induced note char) to
            # enforce a unified length of lines
            string = "".join(line)[:STRING_LEN]
            strings.append(string)
        self.current_board = strings

    # DISPLAY
    def note_progress(func):
        # wrapper to display note progress while Zend's state changes
        def inner(self, *args):
            self.screen.addstr(8, 0, self.__repr__())
            func(self, *args)

        return inner

    @note_progress
    def curses_ui(self):
        # Grab curses screen
        screen = self.screen

        screen.refresh()
        curses.napms(100)  # self.speed)

        # Display the current state of the Oud Zend
        for i, l in enumerate(self.current_board, 1):
            screen.addstr(i, 0, f"{i} {self.current_board[i - 1]}")
            # screen.addchr(i, 0, f"{i} {self.current_board[i - 1]}")

        # Changes go in to the screen buffer and only get
        # displayed after calling `refresh()` to update
        screen.refresh()

    def run(self, note_sheet: Union[List[str], List[List]], speed: float):
        while note_sheet:
            # clear()
            next_ = note_sheet.pop(0)
            next_ = [next_] if isinstance(next_, str) else next_

            self.build_master_string_with_current_note(next_)
            self.split_master_string_into_oud_strings()
            # self.plot_oud_grid()
            self.curses_ui()
            # transition time before the next note
            sleep(speed)

            # reset the grid. For animating strings (in case the next note is the same)
            # re-create an empty boar (Oud Zend)
            reset = [
                "".join(["-" for _ in range(STRING_LEN)]) for _ in range(1, NUM_STRINGS)
            ]
            self.current_board = reset
            self.curses_ui()

        # clear()


def main(note_sheet, speed):
    animator = OudAnimator()
    animator.run(note_sheet=note_sheet, speed=speed)


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("-note", help="note sheet", required=False)
    parser.add_argument(
        "-speed",
        help="transition speed between notes (i.e. sleep time in seconds)",
        type=float,
        default=1,
    )
    args = parser.parse_args()

    from sample_music_sheets import ramsis_kasis, test_notes, saaloony_elnas

    all_notes = args.note.split() if args.note else ["FA", ["SOL", "RE"], "DO"]
    all_notes = args.note.split() if args.note else test_notes.split()
    all_notes = args.note.split() if args.note else saaloony_elnas.split()
    all_notes = args.note.split() if args.note else ramsis_kasis.split()

    main(note_sheet=all_notes, speed=args.speed)
