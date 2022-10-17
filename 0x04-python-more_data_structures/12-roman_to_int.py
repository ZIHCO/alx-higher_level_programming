#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not roman_string) or type(roman_string) != str:
        return 0

    roman_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10,
                  'V': 5, 'I': 1}
    sum_num = 0
    num = 0
    i = 0
    while i < len(roman_string):
        for key in list(roman_dict):
            a = roman_string[i]
            if i + 1 != len(roman_string):
                b = roman_string[i + 1]
                if a == key and roman_dict[a] >= roman_dict[b]:
                    num = roman_dict[a]
                    sum_num += num
                elif a == key:
                    num = roman_dict[b] - roman_dict[a]
                    sum_num += num
                    i = i + 2
                    continue
            elif i == len(roman_string) - 1 and a == key:
                num = roman_dict[a]
                sum_num += num
        i += 1
    return sum_num
