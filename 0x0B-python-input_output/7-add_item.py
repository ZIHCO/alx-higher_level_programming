#!/usr/bin/python3
"""
This module uses sys, 5-save_to_json_file, 6-load_from_json_file
modules
"""

import sys
import os
save_to = __import__('5-save_to_json_file').save_to_json_file
load_from = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    """
    This script adds all commandline argument to a LIST
    """
    if os.path.exists('add_item.json'):
        obj_list = load_from("add_item.json")
    else:
        obj_list = []

    for i in range(1, len(sys.argv)):
        obj_list.append(sys.argv[i])

    save_to(obj_list, "add_item.json")
