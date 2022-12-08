#!/usr/bin/python3
def weight_average(my_list=[]):
    len_1 = len(my_list)
    if len_1 == 0:
        return (0)
    else:
        result = 0
        weight = 0
        for i in my_list:
            result += i[1] * i[0]
            weight += i[1]
        return (result / weight)
