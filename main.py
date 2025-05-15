def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents

def main():
    from stats import num_words
    from stats import char_counts
    filepath = "books/frankenstein.txt"

    book_text = get_book_text(filepath)
    words = num_words(book_text)
    dict_count = char_counts(book_text)
    
    print(f"{words} words found in the document")
    print(dict_count)
    

main()    
    
