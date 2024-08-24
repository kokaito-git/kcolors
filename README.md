# kcolors
```python
pip install kcolors
```
Automátic ANSI colors for Python Scripts (static colors too)

Any import from kcolors enables VT Mode for Windows terminal.
```python
import kcolors # Not recomended, but works
import kcolors.vt # I just want vt (doesn't matter the kcolors version)
```

```python
from kcolors import Colors, SColors

# Colors values becomes "" if the output target is not a terminal
print(f"The color is {Colors.RED}red{Colors.END}.")

# Static colors (will be printed always)
print(f"The color is {SColors.RED}red{SColors.END}.")
```

Samples of auto-disable colors:
```sh
python main.py | cat # output into |, no colors
python main.py > data.txt # output into data.txt, no colors
python main.py # colors
```

# Use refs (or irefs)
They are both the same, just a set of references to Colors. SColors, but 'i' means inversed.

```python
from kcolors.refs import *  # pyright: ignore
print(f"{RED}Dynamic Color{END} - {RED_}Static Color{END}.")
```

```python
from kcolors.irefs import *  # pyright: ignore
print(f"{RED}Dynamic Color{END} - {RED_}Static Color{END}.")
```


