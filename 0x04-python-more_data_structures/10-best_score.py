#!/usr/bin/python3

def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    keys_a = list(a_dictionary.keys())[0]
    value_a = a_dictionary[keys_a]

    for i, j in a_dictionary.items():
        if j > value_a:
            value_a = j
            keys_a = i

    return (keys_a)
