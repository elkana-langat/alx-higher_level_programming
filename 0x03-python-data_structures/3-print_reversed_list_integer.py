#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    my_list.reverse()

    leng = len(my_list)
    for i in range(leng):
        print("{:d}".format(my_list[i]))
