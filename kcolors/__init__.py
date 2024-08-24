"""
https://github.com/kokaito-git/kcolors

Automátic ANSI colors for Python Scripts (static colors too)

Classes:
- **Colors**: Provides dynamic color codes and text formatting that adapt based on whether the output is to a terminal.
  - `python program.py > file.txt` (no colors)
  - `python program.py | cat` (no colors)
  - `python program.py` (colors, if executed from a terminal)

- **StaticColors**: Provides the same colors, but they will always be printed.

Attributes (both `Colors` and `StaticColors`):
- Regular colors: `BLACK`, `RED`, `GREEN`, `YELLOW`, `BLUE`, `PURPLE`, `CYAN`, `GRAY`
- Bold (bright) colors: `BBLACK`, `BRED`, `BGREEN`, `BYELLOW`, `BBLUE`, `BPURPLE`, `BCYAN`, `BGRAY`
- Text formatting options: `BOLD`, `FAINT`, `ITALIC`, `UNDERLINE`, `BLINK`, `NEGATIVE`, `CROSSED`
- `END`: Resets all formatting and colors.

Usage:
- To use the classes, import them directly and access their attributes. For example:
    ```python
    from kcolors import Colors, StaticColors
    print(Colors.RED + "This text is red." + Colors.END)
    print(StaticColors.RED + "This text is red." + StaticColors.END)
    ```

# Direct Access To Members

You can create your own color references. For example:
  - [Sample Code](https://github.com/kokaito-git/kcolors/blob/main/kcolors/samples/colors.py)

Or you can use the `references` module:

**Preferred Methods:**
```python
from kcolors import SColor, Color
from kcolors import BLACK, RED, GREEN, YELLOW, BLUE, PURPLE, CYAN, GRAY, BBLACK, BRED, BGREEN, BYELLOW, BBLUE, BPURPLE, BCYAN, BGRAY, END
from kcolors import BLACK_, RED_, GREEN_, YELLOW_, BLUE_, PURPLE_, CYAN_, GRAY_, BBLACK_, BRED_, BGREEN_, BYELLOW_, BBLUE_, BPURPLE_, BCYAN_, BGRAY_, END_

**Not recomended (but simple):**
from kcolors import * # pyright: ignore
"""

from .src.colors import SColors, Colors
from .src.references import *
