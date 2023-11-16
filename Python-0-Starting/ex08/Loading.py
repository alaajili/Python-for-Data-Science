def ft_tqdm(lst: range) -> None:
    """
    A simplified tqdm-like progress bar implemented as a generator function.

    Args:
    - lst (range): The range over which to iterate.

    Yields:
    - str: Progress bar representation for each iteration.
    """
    total = len(lst)
    bar = ""
    for i in range(total + 1):
        progress = i / total
        percentage = int(progress * 100)

        bar = f"{percentage}%|{'=' * int(progress * 50)}>{' ' * (50 - int(progress * 50))}| {i}/{total}"
        print(f"\r{bar}", end='', flush=True)
        yield
        # sleep(0.05)

from time import sleep
from tqdm import tqdm 
for elem in ft_tqdm(range(333)):
    sleep(0.005)
    # print(elem, end='\r')
print()
for elem in tqdm(range(333)):
    sleep(0.005)
print()