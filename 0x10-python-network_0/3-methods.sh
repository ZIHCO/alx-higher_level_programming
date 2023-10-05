#!/bin/bash
# script displays all HTTP methods the server accept
curl -sIX OPTIONS "$1" | grep "Allow:" | cut -d ":" -f2 | sed 's| ||'
