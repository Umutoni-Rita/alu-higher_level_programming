#!/usr/bin/python3
"""Send a POST request with an email to a URL and display the response.

The URL is the first argument and the email is the second. The script
uses requests, sends the email in the email variable and prints the body.
"""
import sys
import requests


if __name__ == "__main__":
    response = requests.post(sys.argv[1], data={"email": sys.argv[2]})
    print(response.text)
