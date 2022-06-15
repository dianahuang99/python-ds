def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    lowercase_word = word.lower()
    lowercase_letter = letter.lower()
    empty_array = []
    for char in lowercase_word:
        if char == lowercase_letter:
            empty_array.append(char)
    return len(empty_array)


# could have just done this
# return word.lower().count(letter.lower())
