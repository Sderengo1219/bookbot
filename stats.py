def num_words(text):
    list_words = text.split()
    num_words = len(list_words)

    return num_words

def char_counts(text):
    new_text = text.lower()
    dict_count = {}

    for i in new_text:
        if i not in dict_count:
            dict_count[i] = 1
        else:
            dict_count[i] = dict_count[i] + 1

    return dict_count

def sort_dic(dic):
    char_list = []

    for char, count in dic.items():
        char_list.append({"char": char, "num": count})
    
    char_list.sort(reverse=True, key=lambda x: x["num"])
    
    return char_list