def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    lower_phrase = phrase.lower()
    vowels = "aeiou"
    letterDict = {}
    for char in lower_phrase:
        if char in vowels:
            if char in letterDict:
                letterDict[char] += 1
            elif char not in letterDict:
                letterDict[char] = 1
    return letterDict


#  phrase = phrase.lower()
#     counter = {}

#     for ltr in phrase:
#         if ltr in VOWELS:
#             counter[ltr] = counter.get(ltr, 0) + 1

#     return counter
