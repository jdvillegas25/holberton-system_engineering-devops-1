#!/bin/bash
# Takes a URL, sends a request, and returns the size of the body
curl -sI $1 | grep -e Content-Length | cut -f2 -d' '
