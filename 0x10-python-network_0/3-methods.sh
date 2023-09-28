#!/bin/bash
# displays all HTTP methods the server will accept.
curl -s -I -X OPTIONS "$1" | grep "Allow:" | tr -d '\r' | awk -F': ' '{print $2}'
