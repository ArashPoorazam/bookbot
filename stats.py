def get_book_text(file_path):
    with open(file_path) as f:
        book = f.read()
        return book
    

def count_words(book):
    words = book.split()
    count = len(words)
    return count


def count_characters(book):
    dictionary = {}
    for ch in book:
        key = ch.lower()
        dictionary[key] = dictionary.get(key, 0) + 1

        

    return dictionary


def sort_char_counts(char_dict):
    items = [{"char": k, "num": v} for k, v in char_dict.items()]

    def get_num(item):
        return item["num"]

    # sort in-place from greatest to least
    items.sort(key=get_num, reverse=True)
    return items