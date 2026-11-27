#!/usr/bin/python3
"""Display your GitHub user id using the GitHub API.

The first argument is the GitHub username and the second is a personal
access token, used as the password for Basic Authentication. The script
prints None when the credentials are wrong.
"""
import sys
import requests


if __name__ == "__main__":
    response = requests.get("https://api.github.com/user",
                            auth=(sys.argv[1], sys.argv[2]))
    print(response.json().get("id"))
