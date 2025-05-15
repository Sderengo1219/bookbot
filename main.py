def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents

def main():
    from stats import num_words
    from stats import char_counts
    from stats import sort_dic

    filepath = "books/frankenstein.txt"

    book_text = get_book_text(filepath)
    words = num_words(book_text)
    dict_count = char_counts(book_text)
    sorted_list = sort_dic(dict_count)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
   
    print("----------- Word Count ----------")
    print(f"{words} words found in the document")

    print("--------- Character Count -------")

    for each in sorted_list:
        if each.isalpha() == True:
            print(each)

    

main()    
    
