import time
import json

def application(env, start_response):
	start_response('200 OK', [('Content-Type', 'text/html')])
	return [json.dumps({"time" : round(time.time(), 0), "url" : env['PATH_INFO']}).encode()]
