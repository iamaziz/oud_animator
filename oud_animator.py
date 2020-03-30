from time import sleep
from typing import List, Union, Any

from config import NOTES_MAP, MASTER_STRING_LEN, NUM_STRINGS, STRING_LEN, SPEED
from lib import clear


class OudAnimator:
    current_board: List[Union[str, Any]]

    def __init__(self, transition_speed=1):
        self.speed = transition_speed
        self.played_notes = []

    def build_master_string_with_current_note(self, notes: List[str]) -> List[str]:
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
        self.current_board = master_string
        return master_string

    @staticmethod
    def split_master_string_into_oud_strings(master_string: List[str]) -> List[str]:
        """Split the master string into Oud strings (6)"""

        strings = []
        slider = 0, STRING_LEN  # over strings
        for i in range(1, NUM_STRINGS):
            line = master_string[slider[0] : slider[1] + 1]
            slider = slider[1], slider[1] + STRING_LEN  # slide to the next string
            # trim extra dashes in the line (caused by the induced note char) to
            # enforce a unified length of lines
            string = "".join(line)[:STRING_LEN]
            strings.append(string)
        return strings

    def note_progress(func):
        def inner(self, *args):
            func(self, *args)
            print(" ".join([s for s in self.played_notes]))

        return inner

    @note_progress
    def plot_oud_grid(self, strings: List[str]) -> None:
        for i, l in enumerate(strings, 1):
            print(i, l)
        print()


def main(note_sheet, speed):
    animator = OudAnimator()  # transition_speed=speed)
    while note_sheet:
        clear()
        next_ = note_sheet.pop(0)
        current_notes = [next_] if isinstance(next_, str) else next_
        master_string = animator.build_master_string_with_current_note(current_notes)
        strings = animator.split_master_string_into_oud_strings(master_string)
        animator.plot_oud_grid(strings)

        # transition time before the next note
        sleep(speed)

        # reset the grid. For animating strings (in case the next note is the same)
        clear()
        reset = ["".join(["-" for _ in range(len(l))]) for l in strings]
        animator.plot_oud_grid(reset)
        sleep(0.2)

    clear()


if __name__ == "__main__":

    import sys
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

    from sample_music_sheets import ramsis_kasis, test_notes

    all_notes = args.note if args.note else ["FA", ["SOL", "RE"], "DO"]  # or test_notes
    all_notes = args.note if args.note else ramsis_kasis

    main(note_sheet=all_notes, speed=args.speed)
