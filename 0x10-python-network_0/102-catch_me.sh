#!/bin/bash
# Make input URL server respond with specific text in body
curl -sLX PUT  -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
