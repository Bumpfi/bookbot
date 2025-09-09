from stats import count_letters, count_words, get_book_text, sort_char_by_count


def main():
    book_text = get_book_text("./books/frankenstein.txt")
    word_count = count_words("./books/frankenstein.txt")
    character_count_dict = count_letters(book_text)
    char_count_sorted = sort_char_by_count(character_count_dict)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in char_count_sorted:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()
