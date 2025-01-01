def main():    
    
    file_contents = get_book_text("books/frankenstein.txt")
    
    print(file_contents)

    num_words = get_num_words(file_contents)
    print(num_words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

main()