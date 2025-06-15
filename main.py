import sys

from stats import num_of_words
from stats import chars_in_string
from stats import sort_chars

def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]

        text = get_book_text(path)

        num_words = num_of_words(text)
        chars = chars_in_string(text)
    
        sorted_chars = sort_chars(chars)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for dict in sorted_chars:
            char = dict["char"]
            if char.isalpha():
                print(f"{dict["char"]}: {dict["num"]}")
        

main()