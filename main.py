def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents

def main():
    from stats import num_words
    from stats import char_counts
    from stats import sort_dic
    import sys 

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]

    book_text = get_book_text(filepath)
    words = num_words(book_text)
    dict_count = char_counts(book_text)
    sorted_list = sort_dic(dict_count)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
   
    print("----------- Word Count ----------")
    print(f"Found {words} total words")

    print("--------- Character Count -------")

    for each in sorted_list:
        if each["char"].isalpha() == True:
            print(f"{each["char"]}: {each["num"]}")

main()    
    
