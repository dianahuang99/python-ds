from sqlalchemy import false


def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    # Alternate possibilities: use all() with a generator comprehension,
    # though that isn't something we've covered yet:
    #
    # return all(isinstance(item, list) for item in lst)

    for item in lst:
        if not isinstance(item, list):
            return False

    return True

    # why can't we do this
    # for item in lst:
    #     if type(item) != list:
    #         return False
    #     else:
    #         return True
    # for item in lst:
    #     if not isinstance(item, list):
    #         return False

    # return True

    # Alternate possibilities: use all() with a generator comprehension,
    # though that isn't something we've covered yet:
    #
    # return all(isinstance(item, list) for item in lst)

