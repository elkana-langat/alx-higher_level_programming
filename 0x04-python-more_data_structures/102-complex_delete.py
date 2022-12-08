#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new = []
    for i, j in a_dictionary.items():
        if j == value:
            new.append(i)
    for k in new:
        del a_dictionary[k]
    return (a_dictionary)
