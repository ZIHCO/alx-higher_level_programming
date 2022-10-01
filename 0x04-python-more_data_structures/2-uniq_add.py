#!/usr/bin/python3
def uniq_add(my_list=[]):
    copy_list = my_list.copy()
    copy_list.sort()
    length = len(my_list)
    sum = 0
    if length > 0:
        sum = copy_list[0]
        for i in range(0, length):
            if copy_list[i] != copy_list[i - 1] and i != 0 and i != length - 1:
                sum = sum + copy_list[i]
        if copy_list[length - 1] != copy_list[length - 2]:
            sum += copy_list[length - 1]
    return sum
