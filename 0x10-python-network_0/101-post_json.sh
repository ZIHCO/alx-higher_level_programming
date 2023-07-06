#!/bin/bash
# script displays all HTTP methods the server accept
curl -sX POST "$1" -d "$(cat "$2")" -H "Content-Type: application/json"
