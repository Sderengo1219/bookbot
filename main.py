def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents

def num_words(text):
    list_words = text.split()
    num_words = len(list_words)

    return num_words

def main():
    filepath = "books/frankenstein.txt"

    book_text = get_book_text(filepath)
    words = num_words(book_text)
    
    print(f"{words} words found in the document")

main()    
    
