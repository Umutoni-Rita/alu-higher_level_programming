#!/usr/bin/python3
"""Send a POST request with an email to a URL and display the response.

The URL is the first argument and the email is the second. The email is
sent in the email variable and the body is printed decoded in UTF-8.
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    data = urllib.parse.urlencode({"email": sys.argv[2]}).encode("ascii")
    request = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
