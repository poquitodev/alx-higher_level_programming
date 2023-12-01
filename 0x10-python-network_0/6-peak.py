#!/usr/bin/python3
"""contains the function find_peak"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    my_list = list_of_integers
    l = len(my_list)
    if l == 0:
        return
    k = l // 2
    if (k == l - 1 or my_list[k] >= my_list[k + 1]) and (k == 0 or my_list[k] >= my_list[k - 1]):
        return my_list[k]
    if k != l - 1 and my_list[k + 1] > my_list[k]:
        return find_peak(my_list[k + 1:])
    return find_peak(my_list[:k])
