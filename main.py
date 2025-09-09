def get_book_text(filepath):
    file_contents = None

    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


def count_words(filepath):
    text = get_book_text(filepath)
    words = text.split()
    words_count = 0

    for word in words:
        words_count += 1

    return words_count


def main():
    words_count = count_words("./books/frankenstein.txt")
    print(f"{words_count} words found in the document")


main()
