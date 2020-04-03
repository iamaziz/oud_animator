import curses
from time import sleep
from typing import List, Union, Any

from config import NOTES_INDEX, NUM_STRINGS, STRING_LEN, NOTES_INTERVAL


class OudAnimator:
    def __init__(self):
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

    def note_progress(self):
        s = f"{len(self.played_notes)}/{self.number_notes} note progress:\n"
        for n in self.played_notes:
            s += f" {n} "
        # enforce the same length of the STRING_LEN
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

    @staticmethod
    def zend_header():
        spaces = " " * (NOTES_INTERVAL - 6)
        header = [f"finger{i}" if i is not 0 else "open" for i in range(5)]
        header = "  " + f"{spaces}".join(header)
        return header

    def insert_notes(self, current_notes: List[str]):
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
    def curses_ui(self):
        # Grab curses screen
        screen = self.screen

        curses.napms(100)  # To flash between repeated note

        # Display the current state of the Oud Zend
        screen.addstr(0, 0, self.zend_header())
        screen.addstr(2, 0, self.__str__())
        screen.addstr(10, 0, self.note_progress())

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

            # Reset the grid.
            # For animating strings (in case the next note is the same)
            # re-create an empty boar (Oud Zend)
            self.build_zend()
            self.curses_ui()


def main(note_sheet, speed):
    animator = OudAnimator()
    animator.run(note_sheet=note_sheet, speed=speed)


if __name__ == "__main__":
    from argparse import ArgumentParser
    from note_sheets import maqam

    parser = ArgumentParser()
    notes = parser.add_mutually_exclusive_group()
    notes.add_argument(
        "-note",
        help="the note sheet as space-separated string",
        required=False,
        type=str,
    )
    notes.add_argument(
        "-maqam",
        help="choose Maqam to display its notes",
        required=False,
        choices=[m for m in dir(maqam) if not m.startswith("_")],
    )
    parser.add_argument(
        "-speed",
        help="transition speed between notes (i.e. sleep time in seconds)",
        type=float,
        default=1,
    )
    args = parser.parse_args()

    all_notes = args.note.split() if args.note else ["FA", ["SOL", "RE"], "DO"]
    if args.maqam:
        all_notes = getattr(maqam, args.maqam).split()

    elif args.note:
        all_notes = args.note.split()
    else:

        from note_sheets import ramsis_kasis

        all_notes = ramsis_kasis.lesson5.split()

    main(note_sheet=all_notes, speed=args.speed)
