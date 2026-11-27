#!/usr/bin/python3
"""Send a request to a URL and display the body, or the HTTP error code.

The URL is the first argument. The body is printed decoded in UTF-8.
When the server answers with an HTTP error, the script prints
"Error code:" followed by the status code instead.
"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
