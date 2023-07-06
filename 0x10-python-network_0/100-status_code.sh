#!/bin/bash
# script displays all HTTP methods the server accept
curl -sw "%{http_code}" -o /dev/null "$1"
