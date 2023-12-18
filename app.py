import streamlit as st
from time import sleep
from typing import List, Union, Any

from note_sheets import maqam, songs
from config import NOTES_INDEX, NUM_STRINGS, STRING_LEN, NOTES_INTERVAL


class OudAnimator:
    def __init__(self):
        self.current_board: List[str] = []  # the Oud's Zend state
        self.current_master_string: List[Union[str, Any]] = []
        self.number_notes: int = 0
        self.played_notes: List[str] = []

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
        self.current_board = [["-"] * STRING_LEN for _ in range(NUM_STRINGS)]

    @staticmethod
    def zend_header():
        spaces = " " * (NOTES_INTERVAL - 6)
        header = [f"finger{i}" if i is not 0 else "open" for i in range(5)]
        return "  " + f"{spaces}".join(header)

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
    def display_ui(self):
        # Build and display the current state of the Oud Zend using Streamlit
        st.write(self.note_progress())
        st.text(self.zend_header())
        st.text(self.__str__())

    def run(self, note_sheet: Union[List[str], List[List]], speed: float):
        self.number_notes = len(note_sheet)
        with st.expander("Note list"):
            st.markdown(f"`{note_sheet}`", unsafe_allow_html=True)
        while note_sheet:
            next_ = note_sheet.pop(0)
            next_ = [next_] if isinstance(next_, str) else next_
        
            self.build_zend()
            self.insert_notes(next_)
            self.display_ui()
            sleep(speed)



def main(note_sheet, speed):
    animator = OudAnimator()
    animator.run(note_sheet=note_sheet, speed=speed)

    
if __name__ == "__main__":
    
    # Add a title
    st.title("Oud note position animator")

    
    # add header
    st.markdown(
        """
        <p align="center">
            <a href="https://github.com/iamaziz/oud_animator">
            <img src="https://raw.githubusercontent.com/iamaziz/oud_animator/master/assets/README-5a98cab3.png" alt="GitHub" width="%100" height="390">
            </a>
        </p>
        """,
        unsafe_allow_html=True,
    )

    # Streamlit widgets
    st1, st2 = st.columns(2)
    with st1:
        selected_maqam = st.selectbox("Select Maqam", [""] + [m for m in dir(maqam) if not m.startswith("_")], index=0, help="Choose Maqam to display its notes")
    with st2:
        selected_song = st.selectbox("Select Song", [""] + [s for s in dir(songs) if not s.startswith("_")], index=0, help="Or, choose a song from the available sample songs to display its notes")
    help_available_notes = list(NOTES_INDEX.keys())
    notes_input = st.text_input("Enter notes (space-separated)", placeholder="enter the notes to show. As space-separated string (e.g. -note 'DO RE MI Fa Sol La Si Do')", help=f"Available notes (**Case-sensitive**) `{' '.join(help_available_notes)}`")
    speed = st.slider("Transition speed between notes (seconds)", 0.01, 5.0, 1.0)

    # run the animation
    st1, st2 = st.columns(2)
    if st1.toggle("Animate Notes"):
        if selected_maqam:
            notes2show = getattr(maqam, selected_maqam).split()
        elif selected_song:
            notes2show = getattr(songs, selected_song).split()
        elif notes_input:
            notes2show = notes_input.split()
        else:
            st.warning("No notes selected. Showing all notes")
            notes2show = list(NOTES_INDEX.keys())

        main(note_sheet=notes2show, speed=speed)

    # show notes mapping
    if st2.toggle("Show Notes Mapping Logic"):
        # mapping logic
        st.markdown("> ## <sup>Note Mapping Logic</sup>", unsafe_allow_html=True)
        st.code(open("config.py").read())

    # add footer
    st.markdown(
        """
        <hr>
        <p align="center">
        By Aziz Alto, Dec. 17 2023
        </p>
        <p align="center">
            Source code
            <a href="https://github.com/iamaziz/oud_animator">
            available on GitHub
            </a>
        </p>
        """,
        unsafe_allow_html=True,
    )
