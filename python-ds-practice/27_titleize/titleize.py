def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    list_phrase = phrase.split(" ")
    cap_list = [word.capitalize() for word in list_phrase]
    return " ".join(cap_list)


# return phrase.title()
