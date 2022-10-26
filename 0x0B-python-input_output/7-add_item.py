#!/usr/bin/python3
import sys
save_to = __import__('5-save_to_json_file').save_to_json_file
load_from = __import__('6-load_from_json_file').load_from_json_file


"""
This script adds all commandline argument to a LIST
"""
if __name__ == "__main__":
    obj_list = []
    for i in range(1, len(sys.argv)):
        obj_list.append(sys.argv[i])
    with open("add_item.json", 'w', encoding="utf-8") as f:
        save_to(obj_list, "add_item.json")
        load_from("add_item.json")
