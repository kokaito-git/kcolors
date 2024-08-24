"""
Este modulo contiene referencias directas a las clases Colors y SColors.
Los colores dinámicos serían BLACK, BRED, END, etc. Los estáticos BLACK_, BRED_, END_, etc.
  (Nota: puedes obtener las referencias inversas desde irefs)
"""
from .src.colors import Colors, SColors

if "kcolors.irefs" in __import__("sys").modules:
    raise ImportError(
        "kcolors: Not allowed to import both 'kcolors.refs' and 'kcolors.irefs' at the same time."
    )


# Dynamic Colors
BLACK = Colors.BLACK
RED = Colors.RED
GREEN = Colors.GREEN
YELLOW = Colors.YELLOW
BLUE = Colors.BLUE
PURPLE = Colors.PURPLE
CYAN = Colors.CYAN
GRAY = Colors.GRAY

BBLACK = Colors.BBLACK
BRED = Colors.BRED
BGREEN = Colors.BGREEN
BYELLOW = Colors.BYELLOW
BBLUE = Colors.BBLUE
BPURPLE = Colors.BPURPLE
BCYAN = Colors.BCYAN
BGRAY = Colors.BGRAY

BOLD = Colors.BOLD
FAINT = Colors.FAINT
ITALIC = Colors.ITALIC
UNDERLINE = Colors.UNDERLINE
BLINK = Colors.BLINK
NEGATIVE = Colors.NEGATIVE
CROSSED = Colors.CROSSED
END = Colors.END

# Static Colors
BLACK_ = SColors.BLACK
RED_ = SColors.RED
GREEN_ = SColors.GREEN
YELLOW_ = SColors.YELLOW
BLUE_ = SColors.BLUE
PURPLE_ = SColors.PURPLE
CYAN_ = SColors.CYAN
GRAY_ = SColors.GRAY

BBLACK_ = SColors.BBLACK
BRED_ = SColors.BRED
BGREEN_ = SColors.BGREEN
BYELLOW_ = SColors.BYELLOW
BBLUE_ = SColors.BBLUE
BPURPLE_ = SColors.BPURPLE
BCYAN_ = SColors.BCYAN
BGRAY_ = SColors.BGRAY

BOLD_ = SColors.BOLD
FAINT_ = SColors.FAINT
ITALIC_ = SColors.ITALIC
UNDERLINE_ = SColors.UNDERLINE
BLINK_ = SColors.BLINK
NEGATIVE_ = SColors.NEGATIVE
CROSSED_ = SColors.CROSSED
END_ = SColors.END
