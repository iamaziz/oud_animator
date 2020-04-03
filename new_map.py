


# import os
# os.chdir("/Users/aaltowayan/Desktop/oud_note_animator")
from config import NOTES_INDEX


# NOTE: the params below are carefully chosen!!
MASTER_STRING_LEN = 490
NUM_STRINGS = 7
NOTES_INTERVAL = 15  # distance between two notes on a line
# a correct string length is 70
STRING_LEN = int(MASTER_STRING_LEN / NUM_STRINGS)

# -- build zend
zend = []
for i in range (NUM_STRINGS):
    oud_string = []
    for j in range (STRING_LEN+1):
        oud_string.append("-")
    zend.append(oud_string)

# -- insert notes
current_notes = ["RE", "FA", "ME"]

for note in current_notes:
    string_no, note_position = NOTES_INDEX.get(note, [None, None])
    if (string_no and note_position) is not None:
        zend[string_no][note_position] = f"{note}"
        # trim string
        zend[string_no] = zend[string_no][:STRING_LEN]
    
    
print("\n".join(["".join(string) for string in zend]))