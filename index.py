def worker(req):
    return Response("Hello from Python in WebAssembly")

    body = '''\
        <!DOCTYPE html>
        <body>
        <h1>Hello from Wasm Workers Server</h1>
        <p>Replying to {url}</p>
        <p>Method: {method}</p>
        <p>User Agent: {agent}</p>
        <p>Payload: {body}</p>
        <p>This page was generated by a Python file inside WebAssembly</p>
        </body>
    '''.format(
        url=req.url,
        method=req.method,
        agent=req.headers["user-agent"],
        body=req.body
    )

    res = Response(body)

    res.headers["x-generated-by"] = "wasm-workers-server"

    return res
