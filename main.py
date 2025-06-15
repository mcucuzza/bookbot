from stats import *
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
        return contents

    raise Exception("couldn't open file")


def main():
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    try:
        text = get_book_text(sys.argv[1])
    except Exception as e:
        print (e)
        sys.exit(1)

    num_words = words_in_text(text)
    counts = count_letters(text)
    freqs = sort_frequencies(counts)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for freq in freqs:
        if (freq["letter"].isalpha()):
            print(freq["letter"] + ": " + str(freq["count"]))
    print("============= END ===============")

main()