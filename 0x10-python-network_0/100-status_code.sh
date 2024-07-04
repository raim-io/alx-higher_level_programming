#!/bin/bash
# Display only status code of input URL response
curl -so /dev/null -w "%{http_code}" "$1"
