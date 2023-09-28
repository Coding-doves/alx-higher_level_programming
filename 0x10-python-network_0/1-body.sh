#!/bin/bash
# displays the body of the response
curl -s -o /dev/null -w "%{http_code}" "$1" | [ $(cat) = "200" ] && curl -s "$1"
