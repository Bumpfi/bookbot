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


# def count_letters(book_text):
#     letters = list(book_text)
#     letters_dict = {}

#     for letter in letters:
#         char = letter.lower()

#         if char in letters_dict:
#             letters_dict[char] += 1
#         else:
#             letters_dict[char] = 1

#     return letters_dict


def count_letters(book_text):
    letters = list(book_text)
    letters_dict = {}

    for letter in letters:
        char = letter.lower()
        if char.isalpha():  # Only count alphabetic characters
            if char in letters_dict:
                letters_dict[char] += 1
            else:
                letters_dict[char] = 1

    return letters_dict


# Helper Function for sorting
def get_num_key(dict_item):
    return dict_item["num"]


def sort_char_by_count(char_dict):
    char_list = []

    for char, count in char_dict.items():
        char_list.append({"char": char, "num": count})

    char_list.sort(key=get_num_key, reverse=True)

    return char_list
