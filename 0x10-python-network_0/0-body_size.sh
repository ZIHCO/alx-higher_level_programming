#!/bin/bash
# Takes a url, sends a request to the url, and displays the size
curl -sI "$1" | grep "Content-Length:" | cut -d' ' -f2
