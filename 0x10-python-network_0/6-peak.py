#!/usr/bin/python3
"""Find a peak"""

def find_peak(list_of_integers):
    """Finds a peak in the list of unsorted integers"""

    if not list_of_integers:
        return None

    length = len(list_of_integers)
    mid = int(length / 2)
    list = list_of_integers

    if mid - 1 < 0 and mid + 1 >= length:
        return list[mid]
    elif mid - 1 < 0:
        return list[mid] if list[mid] > list[mid + 1] else list[mid + 1]
    elif mid + 1 >= length:
        return list[mid] if list[mid] > list[mid - 1] else list[mid - 1]

    if list[mid - 1] < list[mid] > list[mid + 1]:
        return list[mid]

    if list[mid + 1] > list[mid - 1]:
        return find_peak(list[mid:])
    return find_peak(list[:mid])
