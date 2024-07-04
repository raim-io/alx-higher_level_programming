#!/usr/bin/env bash
# Display size of URL response body
curl -s "$1" | wc -c