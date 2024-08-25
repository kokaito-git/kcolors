# kcolors

## Install

Automatic ANSI colors for Python scripts (static colors too).

```python
pip install kcolors
```

Examples of auto-disable colors:

```sh
python main.py | cat # output into |, no colors
python main.py > data.txt # output into data.txt, no colors
python main.py # colors
```

## Enable VT

Any import from kcolors enables VT Mode for the Windows terminal.

```python
import kcolors # Not recomended, but works
import kcolors.vt # I just want vt (doesn't matter the kcolors version)
```

## Use the classes

```python
from kcolors import Colors, SColors

# Color values become "" if the output target is not a terminal
print(f"The color is {Colors.RED}red{Colors.END}.")

# Static colors (will be printed always)
print(f"The color is {SColors.RED}red{SColors.END}.")
```

## Use refs (or irefs)

They are both the same, just a set of references to Colors and SColors, but 'i' means inverted.

#### Normal

```python
from kcolors.refs import *  # pyright: ignore
print(f"{RED}Dynamic Color{END} - {RED_}Static Color{END}.")
```

#### Reversed

```python
from kcolors.irefs import *  # pyright: ignore
print(f"{RED}Static Color{END} - {RED_}Dynamic Color{END}.")
```
