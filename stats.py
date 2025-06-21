def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_dict = {}
    #creates a set with all unique letters and symbols    
    for char in text:
        lowered = char.lower()
        if lowered in char_dict:
            char_dict[lowered] += 1
        else:
            char_dict[lowered] = 1
    return char_dict
    
def sort_dict(counted_dict):
   
    result_list = []
    for key, value in counted_dict.items():
        new_dict = {"char": key, "num": value}
        result_list.append(new_dict)

    result_list.sort(reverse=True, key=sort_on)
    return result_list

def sort_on(items):
    return items["num"]

