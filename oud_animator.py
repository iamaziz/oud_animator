import curses
from time import sleep
from typing import List, Union, Any

from config import NOTES_INDEX, NUM_STRINGS, STRING_LEN, NOTES_INTERVAL


class OudAnimator:
    def __init__(self, speed=1):
        # self.speed: float = speed
        self.current_board: List[str] = []  # the Oud's Zend state
        self.current_master_string: List[Union[str, Any]] = []
        self.number_notes: int = 0
        self.played_notes: List[str] = []

        self.screen = curses.initscr()
        curses.curs_set(0)  # hide cursor

    def __del__(self):
        curses.endwin()

    def __str__(self):
        # 'i' for the string numbers
        return "\n".join(
            [
                f"{i}  " + "".join(string)
                for i, string in enumerate(self.current_board, 1)
            ]
        )

    def progress(self):
        s = f"{len(self.played_notes)}/{self.number_notes} note progress:\n"
        for n in self.played_notes:
            s += f" {n} "
        # enforce the length of the progress bar to not exceed the STRING_LEN
        return "\n".join([s[i : i + STRING_LEN] for i in range(0, len(s), STRING_LEN)])

    def build_zend(self):
        zend = []
        # Oud strings
        for i in range(NUM_STRINGS):
            oud_string = []
            for j in range(STRING_LEN):
                oud_string.append("-")
            zend.append(oud_string)
        self.current_board = zend

    def insert_notes(self, current_notes):
        for note in current_notes:
            string_no, note_position = NOTES_INDEX.get(note, [None, None])
            if (string_no and note_position) is not None:
                self.current_board[string_no][note_position] = f"{note}"
                self.played_notes.append(note)
                # trim string length
                self.current_board[string_no] = self.current_board[string_no][
                    : STRING_LEN - len(note) + 1
                ]

    # DISPLAY
    def zend_header(self):
        spaces = " " * (NOTES_INTERVAL - 6)
        header = [f"finger{i}" if i is not 0 else "open" for i in range(5)]
        header = "  " + f"{spaces}".join(header)
        return header

    def curses_ui(self):
        # Grab curses screen
        screen = self.screen

        screen.refresh()
        curses.napms(100)  # self.speed)

        # Display the current state of the Oud Zend
        screen.addstr(0, 0, self.zend_header())
        screen.addstr(2, 0, self.__str__())
        screen.addstr(10, 0, self.progress())

        # Changes go in to the screen buffer and only get
        # displayed after calling `refresh()` to update
        screen.refresh()

    def run(self, note_sheet: Union[List[str], List[List]], speed: float):
        self.number_notes = len(note_sheet)
        while note_sheet:
            next_ = note_sheet.pop(0)
            next_ = [next_] if isinstance(next_, str) else next_

            self.build_zend()
            self.insert_notes(next_)
            self.curses_ui()
            # transition time before the next note
            sleep(speed)

            # reset the grid. For animating strings (in case the next note is the same)
            # re-create an empty boar (Oud Zend)
            self.build_zend()
            self.curses_ui()


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
