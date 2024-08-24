"""
Automátic ANSI colors for Python Scripts (static colors too)

Classes:
- Colors: Provides dynamic color codes and text formatting that adapt based on
  whether the output is to a terminal. Includes attributes for regular colors,
  bold colors, and text formatting styles.
- StaticColors: Provides static color codes and text formatting that always output
  as defined, regardless of terminal status.

Attributes (both `Colors` and `StaticColors`):
- Regular colors: BLACK, RED, GREEN, YELLOW, BLUE, PURPLE, CYAN, GRAY
- Bold (bright) colors: BBLACK, BRED, BGREEN, BYELLOW, BBLUE, BPURPLE, BCYAN, BGRAY
- Text formatting options: BOLD, FAINT, ITALIC, UNDERLINE, BLINK, NEGATIVE, CROSSED
- END: Resets all formatting and colors.


Usage:
- To use the classes, import them directly and access their attributes. For example:
    from kcolors import Colors, StaticColors
    print(Colors.RED + "This text is red." + Colors.END)
    print(StaticColors.RED + "This text is red." + StaticColors.END)

# References
wget https://raw.githubusercontent.com/kokaito-git/kcolors/main/kcolors/samples/colors.py
"""

from kcolors.src.colors import Colors
from kcolors.src.static_colors import StaticColors

