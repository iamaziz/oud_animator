from time import sleep
from typing import List, Union

from config import NOTES_MAP, MASTER_STRING_LEN, NUM_STRINGS, NOTES_INTERVAL, STRING_LEN
from lib import clear


def build_master_string_with_current_note(notes: List[str]) -> List[str]:
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
        else:
            master_string.append("-")
    return master_string


def split_master_string_into_oud_strings(master_string: List[str]) -> List[str]:
    """Split the master string into Oud strings (6)"""

    strings = []
    slider = 0, STRING_LEN  # over strings
    for i in range(1, NUM_STRINGS):
        line = master_string[slider[0]:slider[1] + 1]
        slider = slider[1], slider[1] + STRING_LEN  # slide to the next string
        # trim extra dashes in the line (caused by the induced note char) to
        # enforce a unified length of lines
        string = "".join(line)[:STRING_LEN]
        strings.append(string)
    return strings


def plot_oud_grid(strings: List[str]) -> None:
    for i, l in enumerate(strings, 1):
        print(i, l)
    print()


def main(note_sheet):

    while note_sheet:
        clear()
        next_ = note_sheet.pop(0)
        current_notes = [next_] if isinstance(next_, str) else next_
        master_string = build_master_string_with_current_note(current_notes)
        strings = split_master_string_into_oud_strings(master_string)
        plot_oud_grid(strings)
        sleep(1)

    clear()


if __name__ == "__main__":

    import sys

    try:
        all_notes = sys.argv[1].split()
    except IndexError:
        all_notes = ['FA', 'SOL', 'LA', 'SI', 'DO', 'RE', 'MIß', 'MI', 'Fa', 'Fa#',
                     'Sol', 'Laß', 'La', 'Si', 'Si#', 'Do', 'Reß', 'Re', 'fa', 'sol', 'laß']
        from sample_music_sheets import ramsis_kasis
        all_notes = ramsis_kasis

    # TODO: assert all_notes is a clean
    # TODO: also output info e.g. now playing ... bla bla or your note sheet is invalid!
    print(all_notes)
    
    main(note_sheet=all_notes)



