# pypelines

`pypelines` allows you to use `|` like in the Unix shell.

Look at that (really dumb) example:
```python
from pypelines import pypeline

def mul_two(x):
    return x * 2


@pypeline()
def hard_computations(x):
    return x | mul_two


hard_computations(210)   # => 420
```

It's also possible to call anonymous functions:
```python
from pypelines import pypeline


@pypeline()
def hard_computations(x):
    return x | (lambda x: x * 2)

```

In case you want to make interesting, _functional_ stuff, `partial` is on your command:
```python
from functools import partial

from pypelines import pypeline


@pypeline()
def even_more_interesting_computations(x: int) -> list:
    return x | range | partial(map, lambda x: x * 2) | list



even_more_interesting_computations(10)  # => [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

```

Also there is more interesting examples in [usage](usage.py) file.

### Inspiration

This bytecode play is heavily inspired by the: [borzunov's plusplus](https://github.com/borzunov/plusplus) package.
