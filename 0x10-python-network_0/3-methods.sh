#!/bin/bash
# Display valid methods for input URL
curl -sI  "$1" | grep "Allow" | cut -d " " -f 2-
