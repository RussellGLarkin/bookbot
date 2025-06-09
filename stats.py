def get_word_count(book_text):
    words =(book_text).split()
    return len(words)

def get_letter_count(book_text):
    letters = {}
    for char in(book_text):
        char = char.lower()
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
    return letters

def sort_list(letter_count):
    letter_count = list(letter_count.items())
    new_list = []
    for i in letter_count:
        letter_dictionary = {}
        letter_dictionary["char"] = i[0]
        letter_dictionary["num"] = i[1]
        new_list.append(letter_dictionary)
    new_list.sort(key=lambda x: x["num"], reverse=True)
    return new_list