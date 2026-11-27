#!/usr/bin/python3
"""Send a request to a URL and display its X-Request-Id header.

The URL is the first command-line argument. The script uses urllib and
prints the value of the X-Request-Id header of the response.
"""
import sys
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers.get("X-Request-Id"))
