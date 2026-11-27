# Python - Network #1

Sending HTTP requests from Python, first with the standard library
`urllib`, then with the `requests` package: reading bodies and headers,
POSTing form data, handling HTTP errors, parsing JSON and calling the
GitHub API with Basic Authentication.

| File | Description |
| ---- | ----------- |
| `0-hbtn_status.py` | Fetches `/status` with `urllib` and shows the body as bytes and as text. |
| `1-hbtn_header.py` | Displays the `X-Request-Id` header of a URL, with `urllib`. |
| `2-post_email.py` | POSTs an email to a URL and displays the body, with `urllib`. |
| `3-error_code.py` | Displays the body of a URL, or `Error code: <code>` on an HTTP error, with `urllib`. |
| `4-hbtn_status.py` | Fetches `/status` with `requests` and shows the body. |
| `5-hbtn_header.py` | Displays the `X-Request-Id` header of a URL, with `requests`. |
| `6-post_email.py` | POSTs an email to a URL and displays the body, with `requests`. |
| `7-error_code.py` | Displays the body of a URL, or `Error code: <code>` when the status is 400 or more. |
| `8-json_api.py` | Searches a user by letter and displays `[<id>] <name>`. |
| `10-my_github.py` | Displays your GitHub id using Basic Authentication with a token. |
