import sys
from ft_filter import ft_filter

def filter_string(s, n):
    """
    Filter words from string s with length greater than n.
    """
    assert isinstance(s, str) and isinstance(n, int), "AssertionError: the arguments are bad"
    return list(ft_filter(lambda word: len(word) > n, s.split()))


if __name__ == "__main__":
    try:
        assert len(sys.argv) == 3, "AssertionError: the arguments are bad"
        s = sys.argv[1]
        try:
            n = int(sys.argv[2])
            result = filter_string(s, n)
            print(result)
        except ValueError:
            print('AssertionError: the arguments are bad')
    except AssertionError and ValueError as e:
        print(e)
