"""This file contains:
1) the parameters for the Oud's neck (Zend) segmentation and
2) the mapping of the notes to indices on the Oud's strings


# -- help

# "ß" --> bemol       (on keyboard: options + s)
# "#" --> diez        (on keyboard: shift + 3)

# for reference see:
# https://en.wikipedia.org/wiki/Key_signature_names_and_translations
"""

# -- PARAMETERS to setup the grid of the Oud neck (Zend)
STRING_LEN = 100
NUM_STRINGS = 6
NOTES_INTERVAL = 15  # distance between two neighboring notes on the same string

# MAP legend
# ----------
# NOTENAME: [StringNumber, FingerNumber "or number of interval shifts on the string"]

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
    "Miß": [4, NOTES_INTERVAL * 3],
    "Mi": [4, NOTES_INTERVAL * 4],
    # string #6
    "fa": [5, NOTES_INTERVAL * 0],
    "sol": [5, NOTES_INTERVAL * 2],
    "laß": [5, NOTES_INTERVAL * 3],
    "la": [5, NOTES_INTERVAL * 4],
}
