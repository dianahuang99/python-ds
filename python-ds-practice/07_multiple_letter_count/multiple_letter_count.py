def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    letterDict = {}
    for char in phrase:
        if char in letterDict:
            letterDict[char] += 1
        elif char not in letterDict:
            letterDict[char] = 1
    return letterDict

    # counter = {}

    # for ltr in phrase:
    #     counter[ltr] = counter.get(ltr, 0) + 1

    # return counter
