#!/bin/bash
# Displays all HTTP methods the server accepts for the URL given as argument
curl -sI -X OPTIONS "$1" | grep "^Allow:" | cut -d " " -f 2-
