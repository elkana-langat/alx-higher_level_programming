#!/usr/bin/python3
"""Adds all arguments to a python list, and then save them to a file."""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    new_list = load_from_json_file(filename)
except FileNotFoundError:
    new_list = []
len_1 = len(sys.argv)
for i in range(1, len_1):
    new_list.append(sys.argv[i])
save_to_json_file(new_list, filename)
