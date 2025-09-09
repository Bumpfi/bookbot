import sys

from stats import count_letters, count_words, get_book_text, sort_char_by_count


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    word_count = count_words(sys.argv[1])
    character_count_dict = count_letters(book_text)
    char_count_sorted = sort_char_by_count(character_count_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in char_count_sorted:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()
