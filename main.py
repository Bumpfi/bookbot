from stats import count_letters, count_words, get_book_text


def main():
    book_text = get_book_text("./books/frankenstein.txt")
    word_count = count_words("./books/frankenstein.txt")
    character_count = count_letters(book_text)

    print(f"{word_count} words found in the document")
    print(character_count)


main()
