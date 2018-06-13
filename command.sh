sudo apt-get install python-gevent python-gevent-websocket

it will use to run as following


http_server = WSGIServer(('', 5000), app)
http_server.serve_forever()
