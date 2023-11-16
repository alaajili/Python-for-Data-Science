import sys

NESTED_MORSE = {
    " ": "/",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----."
}


def encode_to_morse(text: str) -> str:
    """
    Encode a string into Morse Code.
    """
    try:
        morse_code = [NESTED_MORSE[char.upper()] for char in text]
        return " ".join(morse_code)
    except:
        raise AssertionError('AssertionError: the arguments are bad')


def main():
    try:
        assert len(sys.argv) == 2, 'AssertionError: the arguments are bad'
        text = sys.argv[1]
        morse_code = encode_to_morse(text)
        print(morse_code)
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()