from flask import Flask, request
import json, cherrypy

app = Flask(__name__)

d = {}

class Root(object):

    def __init__(self, content):
        self.content = content
        print(self.content)  # this works

    exposed = True

    def GET(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        return json.dumps(self.content)

    def POST(self):
        return self.content


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)