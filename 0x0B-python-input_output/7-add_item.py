#!/usr/bin/python3
"""
7-add_item module
"""
import sys
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file = "add_item.json"
list = []

if os.path.exists(file):
    list = load_from_json_file(file)

for i in range(1, len(sys.argv)):
    list.append(sys.argv[i])

save_to_json_file(list, file)