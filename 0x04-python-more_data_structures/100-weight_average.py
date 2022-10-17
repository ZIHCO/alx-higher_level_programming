#!/usr/bin/python3
def weight_average(my_list=[]):
    sum_of_fx = 0
    sum_of_f = 0
    if my_list:
        for tup in my_list:
            sum_of_fx += (tup[0] * tup[1])
            sum_of_f += tup[1]
        return sum_of_fx / sum_of_f
    return 0
