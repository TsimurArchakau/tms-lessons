def get_most_frequent_word(text: str):
    word_dict = {}
    for word in text.split(' '):
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    word_quantity = 0
    most_frequent_word = ''
    for key, value in word_dict.items():
        if value > word_quantity:
            word_quantity = value
            most_frequent_word = key
    return most_frequent_word


assert get_most_frequent_word('My name is is is Timur') == 'is'
assert get_most_frequent_word('My name name name is Archakov Timur Timur Timur Timur') == 'Timur'
