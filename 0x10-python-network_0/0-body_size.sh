#!/usr/bin/bash
# Takes a url, sends a request to the url, and displays the size
curl "$1" -sIw '%{size_request}\n'
