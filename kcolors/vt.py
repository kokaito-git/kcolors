"""Enable VT Mode for windows just by importing this"""

# Enable VT mode (for Windows)
if __import__("sys").stdout.isatty():
    if __import__("platform").system() == "Windows":
            kernel32 = __import__("ctypes").windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
            del kernel32
