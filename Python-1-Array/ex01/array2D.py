import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Takes a 2D array as input, prints its shape, and returns a truncated version
    based on the provided start and end arguments using slicing method.

    Parameters:
    - family (list): A 2D array (list of lists).
    - start (int): Starting index for slicing.
    - end (int): Ending index for slicing.

    Returns:
    - list: Truncated 2D array based on the start and end indices.
    """
    if not isinstance(family, list) or not all(isinstance(row, list) and len(row) == len(family[0]) for row in family):
        raise ValueError("Input should be a 2D list with equal-sized rows")

    arr = np.array(family)
    original_shape = arr.shape
    print("My shape is:", original_shape)

    if start < 0 or end > original_shape[1]:
        raise ValueError("Start or end indices are out of bounds")

    sliced = arr[start:end, :]

    new_shape = sliced.shape
    print("My new shape is:", new_shape)
    return sliced.tolist()

# family = [[1.80, 78.4],
#     [2.15, 102.7],
#     [2.10, 98.5],
#     [1.88, 75.2]]
# print(slice_me(family, 0, 2))
# print(slice_me(family, 1, 2))