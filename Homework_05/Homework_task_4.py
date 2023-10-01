def get_longest_word(text: str):
    word_length = 0
    longest_word = ''
    for word in text.split(' '):
        if len(word) > word_length:
            word_length = len(word)
            longest_word = word
    return longest_word


assert get_longest_word('My name is Timur') == 'Timur'
assert get_longest_word('My name is Archakov Timur') == 'Archakov'
