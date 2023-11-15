
from typing import Iterator


def ft_filter(function, iterable) -> Iterator:
    """
    Construct an iterator from elements of iterable for which function returns true.

    Equivalent to:

    result = []
    for item in iterable:
        if function(item):
            result.append(item)
    return iter(result)
    """
    return iter([item for item in iterable if function(item)])
