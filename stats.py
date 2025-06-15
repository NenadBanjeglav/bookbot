def num_of_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def chars_in_string(text):
    str_lower = text.lower()
    
    chars = {}
    

    for i in range(0, len(str_lower)):
        char = str_lower[i]
        if char in chars:
            chars[char] +=1
        else:
            chars[char]  =1

    return chars

def sort_on(dict):
    return dict["num"]
    
def sort_chars(dict):
    chars_list = []

    for char in dict:
        chars_list.append({"char": char, "num": dict[char]})

    chars_list.sort(reverse=True, key=sort_on)

    return chars_list