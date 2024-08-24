"""
This module provides color codes and text formatting for terminal output.

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

Direct References:
- The direct references to the attributes are named the same as the attributes of their class, with static references ending in an underscore. For example:
  - For `Colors`: BLACK, RED, GREEN, etc.
  - For `StaticColors`: BLACK_, RED_, GREEN_, etc.

Usage:
- To use the classes, import them directly and access their attributes. For example:
    from your_module import Colors, StaticColors
    print(Colors.RED + "This text is red." + Colors.END)
    print(StaticColors.RED_ + "This text is red." + StaticColors.END_)

- Alternatively, you can import the attributes directly if you prefer not to reference the classes. For example:
    from your_module import RED, RED_
    print(RED + "This text is red." + END)
    print(RED_ + "This text is red." + END_)
"""

from .src.colors import *
from .src.static_colors import *

__all__ = [
    "Colors",
    "StaticColors",
    "BLACK",
    "RED",
    "GREEN",
    "YELLOW",
    "BLUE",
    "PURPLE",
    "CYAN",
    "GRAY",
    "BBLACK",
    "BRED",
    "BGREEN",
    "BYELLOW",
    "BBLUE",
    "BPURPLE",
    "BCYAN",
    "BGRAY",
    "BOLD",
    "FAINT",
    "ITALIC",
    "UNDERLINE",
    "BLINK",
    "NEGATIVE",
    "CROSSED",
    "END",
    "BLACK_",
    "RED_",
    "GREEN_",
    "YELLOW_",
    "BLUE_",
    "PURPLE_",
    "CYAN_",
    "GRAY_",
    "BBLACK_",
    "BRED_",
    "BGREEN_",
    "BYELLOW_",
    "BBLUE_",
    "BPURPLE_",
    "BCYAN_",
    "BGRAY_",
    "BOLD_",
    "FAINT_",
    "ITALIC_",
    "UNDERLINE_",
    "BLINK_",
    "NEGATIVE_",
    "CROSSED_",
    "END_",
]
