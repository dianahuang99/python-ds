def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    lst_num1 = list(str(num1))
    lst_num2 = list(str(num2))
    lst_num1.sort()
    lst_num2.sort()
    if lst_num1 == lst_num2:
        return True
    elif lst_num1 != lst_num2:
        return False


# def freq_counter(coll):
#     """Returns frequency counter mapping of coll."""

#     counts = {}

#     for x in coll:
#         counts[x] = counts.get(x, 0) + 1

#     return counts


# def same_frequency(num1, num2):
#     """Do these nums have same frequencies of digits?

#         >>> same_frequency(551122, 221515)
#         True

#         >>> same_frequency(321142, 3212215)
#         False

#         >>> same_frequency(1212, 2211)
#         True
#     """

#     return freq_counter(str(num1)) == freq_counter(str(num2))
