#!/usr/bin/python3
def uniq_add(my_list=[]):
    copy_list = my_list.copy()
    copy_list.sort()
    sum = 0
    for i in range(0, len(my_list)):
        if i + 1 < len(my_list):
            if copy_list[i] != copy_list[i + 1]:
                sum = sum + copy_list[i]
    if copy_list[len(my_list) - 1] != copy_list[len(my_list) - 2]:
        sum += copy_list[len(my_list) - 1]
    return sum

        
