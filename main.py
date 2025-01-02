def main():    
    
    file_contents = get_book_text("books/frankenstein.txt")
    
    print(file_contents)

    num_words = get_num_words(file_contents)
    print(num_words)
    letters = get_num_letters(file_contents)
    print(letters)
    print(print_report(letters))


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_words(words):
    split_words = words.split()
    return split_words

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_letters(words):
    lowered_string = words.lower()
    split_string = list(lowered_string)
    letters = {"a": 0, "b": 0, "c":0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
    for letter in split_string:
        for char in letters:
            if letter == char:
                letters[char] += 1
    return letters

def print_report(letters):
    res = {key: val for key, val in sorted(letters.items(), key = lambda ele: ele[1], reverse=True)}
    for i in res:
        print(f"The {i} character was found {res[i]} times")
    return


main()