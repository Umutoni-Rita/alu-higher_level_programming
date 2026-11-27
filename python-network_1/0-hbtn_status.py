#!/usr/bin/python3
"""Fetch https://alu-intranet.hbtn.io/status with urllib and describe it.

The script prints the type of the raw body, the raw bytes, and the body
decoded as UTF-8.
"""
import urllib.request


if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        body = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode("utf-8")))
