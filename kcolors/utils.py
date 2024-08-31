"""
Some utils related with the work that this library does. By now it contains two
functions

`remove_ansi_codes(str)`: it removes all the ansi codes using regex and returns
it it.

`remove_color_coldes(str)`: it removes ansi too, but just the color codes
including BOLD, END, etc..
"""

import re


def remove_ansi_codes(text: str) -> str:
    ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")
    return ansi_escape.sub("", text)


def remove_color_codes(text: str) -> str:
    ansi_escape = re.compile(r"\033\[[0-9;]*m")
    return ansi_escape.sub("", text)
