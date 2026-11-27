#!/usr/bin/python3
"""Send a request to a URL and display the body, or the HTTP error code.

The URL is the first argument. When the status code is 400 or more the
script prints "Error code:" followed by the code, else it prints the body.
"""
import sys
import requests


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
