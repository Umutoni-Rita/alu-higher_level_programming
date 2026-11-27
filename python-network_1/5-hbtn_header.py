#!/usr/bin/python3
"""Send a request to a URL and display its X-Request-Id header.

The URL is the first command-line argument. The script uses requests
and prints the value of the X-Request-Id header of the response.
"""
import sys
import requests


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get("X-Request-Id"))
