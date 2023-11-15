import sys


def char_count(text: str) -> None:
    '''Takes in a string text, print infos about its charachters'''

    char_count = len(text)
    upper_count = sum(1 for char in text if char.isupper())
    lower_count = sum(1 for char in text if char.islower())
    space_count = sum(1 for char in text if char.isspace())
    digit_count = sum(1 for char in text if char.isdigit())
    punctuation_count = char_count - upper_count - lower_count - space_count - digit_count

    print(f"The text contains {char_count} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")

def main() -> None:
    assert len(sys.argv) <= 2, "Only one argument (text) is allowed."
    if len(sys.argv) == 2:
        char_count(sys.argv[1])
    else:
        text = input("What is the text to count?\n")
        char_count(text)
        


if __name__ == "__main__":
    main()