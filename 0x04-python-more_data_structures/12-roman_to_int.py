#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return (0)
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    roman_list = list(roman_string)
    len_1 = len(roman_list)
    result = 0

    if len_1 == 1:
        result = roman_dict[roman_list[0]]
        return result
    elif len_1 > 1:
        if roman_dict[roman_list[0]] > roman_dict[roman_list[1]]:
            for i in roman_list:
                result += roman_dict[i]
            return (result)
        else:
            last = roman_dict[roman_list[len_1 - 1]]
            for i in range(0, len_1 - 1):
                result += roman_dict[roman_list[i]]
            return (last - result)
