#!/usr/bin/python3
"""Search a user by letter through http://0.0.0.0:5000/search_user.

The letter is the first argument, sent in the variable q (empty when no
argument is given). The script prints "[<id>] <name>" for the result,
"No result" when the JSON is empty and "Not a valid JSON" when the body
is not JSON.
"""
import sys
import requests


if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    response = requests.post("http://0.0.0.0:5000/search_user",
                             data={"q": q})
    try:
        user = response.json()
        if user:
            print("[{}] {}".format(user.get("id"), user.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
