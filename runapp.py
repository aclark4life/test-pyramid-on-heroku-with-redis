from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import os
import redis
import urlparse

if 'REDISTOGO_URL' in os.environ:
    urlparse.uses_netloc.append('redis')
    url = urlparse.urlparse(os.environ['REDISTOGO_URL'])
    REDIS = redis.Redis(host=url.hostname, port=url.port, db=0, password=url.password)
	REDIS.set("answer", 42)


def hello_world(request):
	return Response('The answer is %s' % REDIS.get("answer"))


if __name__ == '__main__':
	config = Configurator()
	config.add_route('hello', '/')
	config.add_view(hello_world, route_name='hello')
	app = config.make_wsgi_app()
	port = int(os.environ.get("PORT", 5000))
	server = make_server('0.0.0.0', port, app)
	server.serve_forever()
