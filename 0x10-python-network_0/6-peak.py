#!/usr/bin/python3
"""find the peak of a list"""


def find_peak(list_of_integers):
    """find peak"""
    if not list_of_integers:
        return
    return max(list_of_integers)
