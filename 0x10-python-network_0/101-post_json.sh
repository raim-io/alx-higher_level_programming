#!/bin/bash
# Display body of input URL response with JSON file request body
curl -sH "Content-Type: application/json" -d "$(cat "$2")" "$1"
