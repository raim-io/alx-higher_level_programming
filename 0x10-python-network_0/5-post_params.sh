#!/bin/bash
# Display input URL response with custom request params
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
