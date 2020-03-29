from time import sleep
from typing import List, Union

from lib import clear

# -- PARAMETERS to setup the grid of the OUD neck (Zend)
# NOTE: the params below are carefully chosen!!
MASTER_STRING_LEN = 490
NUM_STRINGS = 7
NOTES_INTERVAL = 15     # distance between two notes on a line
# a correct string length is 70
STRING_LEN = int(MASTER_STRING_LEN / NUM_STRINGS)


NOTES_MAP = {
    # ß --> bemol       (on keyboard: options + s)
    # --> diez        (on keyboard: shift + 3)

    # for reference see:
    # https://en.wikipedia.org/wiki/Key_signature_names_and_translations

    # MAP legend
    # ----------
    # NOTENAME: (StringNumber) + (Number of shift on the string)
    # ###########################################################

    # string #1
    "FA": (STRING_LEN * 0),
    "SOL": (STRING_LEN * 0) + (NOTES_INTERVAL * 2),
    # string #2
    "LA": (STRING_LEN * 1),
    "SI": (STRING_LEN * 1) + (NOTES_INTERVAL * 1),
    "DO": (STRING_LEN * 1) + (NOTES_INTERVAL * 3),
    # string #3
    "RE": (STRING_LEN * 2),
    "MIß": (STRING_LEN * 2) + (NOTES_INTERVAL * 1),
    "MI": (STRING_LEN * 2) + (NOTES_INTERVAL * 2),
    "Fa": (STRING_LEN * 2) + (NOTES_INTERVAL * 3),
    "Fa#": (STRING_LEN * 2) + (NOTES_INTERVAL * 4),
    # string #4
    "Sol": (STRING_LEN * 3),
    "Laß": (STRING_LEN * 3) + (NOTES_INTERVAL * 1),
    "La": (STRING_LEN * 3) + (NOTES_INTERVAL * 2),
    "Si": (STRING_LEN * 3) + (NOTES_INTERVAL * 3),
    "Si#": (STRING_LEN * 3) + (NOTES_INTERVAL * 4),
    # string #5
    "Do": (STRING_LEN * 4),
    "Reß": (STRING_LEN * 4) + (NOTES_INTERVAL * 1),
    "Re": (STRING_LEN * 4) + (NOTES_INTERVAL * 2),
    "Mi": (STRING_LEN * 4) + (NOTES_INTERVAL * 3),
    "Faß": (STRING_LEN * 4) + (NOTES_INTERVAL * 4),
    # string #6
    "fa": (STRING_LEN * 5),
    "sol": (STRING_LEN * 5) + (NOTES_INTERVAL * 2),
    "laß": (STRING_LEN * 5) + (NOTES_INTERVAL * 3),
    "la": (STRING_LEN * 5) + (NOTES_INTERVAL * 4),
}


def build_master_string_with_current_note(notes: List[str]) -> List[str]:
    """build a long line 'a string' to represent all the six strings of the Oud as one segment.
    This is easier for indexing (and inserting) notes.
    ::notes: list, of the same-time notes to play together e.g [FA, Sol]
    """
    # create the master string

    # e.g. {'FA': 0, 'Fa': 185}
    current_notes = {NOTES_MAP[note]: note for note in notes}

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

    main(note_sheet=all_notes)
