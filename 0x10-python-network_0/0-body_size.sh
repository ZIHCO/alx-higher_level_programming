#!/bin/bash
# What is my content byte size
curl -s "$1" | wc -m
