# Python - Network #0

Talking to a web server from the command line with `curl`: reading the
response body, choosing the HTTP method, listing allowed methods,
sending custom headers and sending POST form data.

Every script takes the URL as its first argument, for example:

```
./0-body_size.sh 0.0.0.0:5000
```

| File | Description |
| ---- | ----------- |
| `0-body_size.sh` | Displays the size of the response body, in bytes. |
| `1-body.sh` | Displays the body of the response, only for a 200 status code. |
| `2-delete.sh` | Sends a `DELETE` request and displays the body. |
| `3-methods.sh` | Displays the HTTP methods the server accepts for the URL. |
| `4-header.sh` | Sends the header `X-School-User-Id: 98` and displays the body. |
| `5-post_params.sh` | Sends `email` and `subject` as POST data and displays the body. |
