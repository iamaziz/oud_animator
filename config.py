"""This file contains:
1) the parameters for the Oud's neck segmentation and 
2) the mapping of the notes to indices on the Master String


# -- help

# "ß" --> bemol       (on keyboard: options + s)
# "#" --> diez        (on keyboard: shift + 3)

# for reference see:
# https://en.wikipedia.org/wiki/Key_signature_names_and_translations
"""

# -- PARAMETERS to setup the grid of the Oud neck (Zend)
MASTER_STRING_LEN = 420  # 490
NUM_STRINGS = 6
NOTES_INTERVAL = 15  # distance between two neighboring notes on the same string
STRING_LEN = int(MASTER_STRING_LEN / NUM_STRINGS)

# MAP legend
# ----------
# NOTENAME: (StringNumber) + (Number of shift on the string)

NOTES_MAP = {
    # string #1
    "FA": (STRING_LEN * 0),
    "SOL": (STRING_LEN * 0) + (NOTES_INTERVAL * 2),
    # string #2
    "LA": (STRING_LEN * 1),
    "SI": (STRING_LEN * 1) + (NOTES_INTERVAL * 1),
    "DO": (STRING_LEN * 1) + (NOTES_INTERVAL * 3),
    "REß": (STRING_LEN * 1) + (NOTES_INTERVAL * 4),
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


NOTES_INDEX = {
    # string #1
    "FA": [0, NOTES_INTERVAL * 0],
    "SOL": [0, NOTES_INTERVAL * 2],
    # string #2
    "LA": [1, NOTES_INTERVAL * 0],
    "SI": [1, NOTES_INTERVAL * 1],
    "DO": [1, NOTES_INTERVAL * 3],
    "REß": [1, NOTES_INTERVAL * 4],
    # string #3
    "RE": [2, NOTES_INTERVAL * 0],
    "MIß": [2, NOTES_INTERVAL * 1],
    "MI": [2, NOTES_INTERVAL * 2],
    "Fa": [2, NOTES_INTERVAL * 3],
    "Fa#": [2, NOTES_INTERVAL * 4],
    # string #4
    "Sol": [3, NOTES_INTERVAL * 0],
    "Laß": [3, NOTES_INTERVAL * 1],
    "La": [3, NOTES_INTERVAL * 2],
    "Siß": [3, NOTES_INTERVAL * 3],
    "Si": [3, NOTES_INTERVAL * 4],
    # string #5
    "Do": [4, NOTES_INTERVAL * 0],
    "Reß": [4, NOTES_INTERVAL * 1],
    "Re": [4, NOTES_INTERVAL * 2],
    "Mi": [4, NOTES_INTERVAL * 3],
    "Faß": [4, NOTES_INTERVAL * 4],
    # string #6
    "fa": [5, NOTES_INTERVAL * 0],
    "sol": [5, NOTES_INTERVAL * 2],
    "laß": [5, NOTES_INTERVAL * 3],
    "la": [5, NOTES_INTERVAL * 4],
}
