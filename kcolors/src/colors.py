class SColors:
    """
    Static version of Colors.
    """
    # Regular colors
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    YELLOW = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    GRAY = "\033[0;37m"

    # Bold colors (bright versions)
    BBLACK = "\033[1;30m"
    BRED = "\033[1;31m"
    BGREEN = "\033[1;32m"
    BYELLOW = "\033[1;33m"
    BBLUE = "\033[1;34m"
    BPURPLE = "\033[1;35m"
    BCYAN = "\033[1;36m"
    BGRAY = "\033[1;37m"

    # Text formatting
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"  # Reset all formatting


class Colors:
    """
    A class for automatic color codes and text formatting for terminal output.

    Provides attributes for:
    - Regular colors and bold colors (bright versions of the regular colors)
    - Text formatting styles

    Attributes:
    - Regular colors: BLACK, RED, GREEN, YELLOW, BLUE, PURPLE, CYAN, GRAY
    - Bold (bright) colors: BBLACK, BRED, BGREEN, BYELLOW, BBLUE, BPURPLE, BCYAN, BGRAY
    - Text formatting options: BOLD, FAINT, ITALIC, UNDERLINE, BLINK, NEGATIVE, CROSSED
    - END: Resets all formatting and colors.

    Behavior:
    - If the output is not to a terminal (i.e., `sys.stdout.isatty()` is False), color codes are disabled to avoid unwanted characters in non-terminal environments.

    - If you want to avoid automatic disabling of colors when output is not to a terminal, use the `SColors` class instead.
    """

    # Regular colors
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    YELLOW = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    GRAY = "\033[0;37m"

    # Bold colors (bright versions)
    BBLACK = "\033[1;30m"
    BRED = "\033[1;31m"
    BGREEN = "\033[1;32m"
    BYELLOW = "\033[1;33m"
    BBLUE = "\033[1;34m"
    BPURPLE = "\033[1;35m"
    BCYAN = "\033[1;36m"
    BGRAY = "\033[1;37m"

    # Text formatting
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"  # Reset all formatting

    # Convert color codes in "" if program output is not a terminal
    if not __import__("sys").stdout.isatty():
        for _ in dir():
            if isinstance(_, str) and _[0] != "_":
                locals()[_] = ""
