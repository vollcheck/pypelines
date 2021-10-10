# pypelines - hack on Python stack enabling unix-like pipeline - `|`

`pypelines` allows you to use `|` like in the Unix shell.

Look at that (really dumb) example:

```python
from pypelines import pypeline

def mul_two(x):
    return x * 2


@pypeline
def hard_computations(x):
    return x | mul_two


print(hard_computations(210))   # => 420
```
