#!/usr/bin/python3
"""My_list module, contains MyList class, an subclass os the
list class
"""


class MyList(list):
    """MyList contains the print_sorted public instance method
    the print a list in sorted ascending prder"""

    def print_sorted(self):
        """Return - a sorted list in ascending order"""

        sorted_list = self[:]
        i = 0
        while i < len(self):
            j = 1
            k = 0
            while j < (len(self) - (i + 1)):
                if sorted_list[k] > sorted_list[j]:
                    tmp = sorted_list[j]
                    sorted_list[j] = sorted_list[k]
                    sorted_list[k] = tmp
                k += 1
                j += 1
            i += 1
        print(sorted_list)
