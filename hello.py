def app(environ, start_response):
    response_body = environ['QUERY_STRING'].split('&')
    response = '\n'.join(response_body)
    response = response.encode()
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(response)))
    ])
    return iter([response])
