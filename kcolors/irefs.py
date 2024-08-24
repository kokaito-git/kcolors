"""
Este modulo contiene referencias directas a las clases Colors y SColors.
    Los colores dinámicos son BLACK_, BRED_, END_, etc mientras que los estáticos son BLACK, BRED, END, etc.
  (Nota: estas referencias son las inversas de refs)
"""
from .src.colors import Colors, SColors

if "kcolors.refs" in __import__("sys").modules:
    raise ImportError(
        "kcolors: Not allowed to import both 'kcolors.refs' and 'kcolors.irefs' at the same time."
    )

# Dynamic Colors
BLACK = SColors.BLACK
RED = SColors.RED
GREEN = SColors.GREEN
YELLOW = SColors.YELLOW
BLUE = SColors.BLUE
PURPLE = SColors.PURPLE
CYAN = SColors.CYAN
GRAY = SColors.GRAY

BBLACK = SColors.BBLACK
BRED = SColors.BRED
BGREEN = SColors.BGREEN
BYELLOW = SColors.BYELLOW
BBLUE = SColors.BBLUE
BPURPLE = SColors.BPURPLE
BCYAN = SColors.BCYAN
BGRAY = SColors.BGRAY

BOLD = SColors.BOLD
FAINT = SColors.FAINT
ITALIC = SColors.ITALIC
UNDERLINE = SColors.UNDERLINE
BLINK = SColors.BLINK
NEGATIVE = SColors.NEGATIVE
CROSSED = SColors.CROSSED
END = SColors.END

# Static Colors
BLACK_ = Colors.BLACK
RED_ = Colors.RED
GREEN_ = Colors.GREEN
YELLOW_ = Colors.YELLOW
BLUE_ = Colors.BLUE
PURPLE_ = Colors.PURPLE
CYAN_ = Colors.CYAN
GRAY_ = Colors.GRAY

BBLACK_ = Colors.BBLACK
BRED_ = Colors.BRED
BGREEN_ = Colors.BGREEN
BYELLOW_ = Colors.BYELLOW
BBLUE_ = Colors.BBLUE
BPURPLE_ = Colors.BPURPLE
BCYAN_ = Colors.BCYAN
BGRAY_ = Colors.BGRAY

BOLD_ = Colors.BOLD
FAINT_ = Colors.FAINT
ITALIC_ = Colors.ITALIC
UNDERLINE_ = Colors.UNDERLINE
BLINK_ = Colors.BLINK
NEGATIVE_ = Colors.NEGATIVE
CROSSED_ = Colors.CROSSED
END_ = Colors.END
