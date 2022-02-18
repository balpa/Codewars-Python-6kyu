"""
You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.
"""


def sort_array(source_array):
    odds = sorted(x for x in source_array if x % 2 == 1)
    newlist = []
    for n in source_array:
        if n % 2:
            newlist.append(odds.pop(0))
        else:
            newlist.append(n)
    return list(newlist)
