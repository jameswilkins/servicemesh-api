from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import requests

app = Flask(__name__)
api = Api(app)

count = 0

class HelloWorld(Resource):
    def get(self):
        return {'a day my ': 'ass'}

class SomeCrap(Resource):
    def get(self):
        return {'Calling from ' : '/foo'}

class Counter(Resource):
    def get(self):
        global count
        count += 1
        return {'Counter' : count}
class FetchCount(Resource):
    def get(self):
        r = requests.get('http://count-svc:5000/count')
        return {'Counter' : r.json().get('Counter')}
api.add_resource(HelloWorld, '/')
api.add_resource(SomeCrap, '/foo')
api.add_resource(Counter, '/count')
api.add_resource(FetchCount, '/fetch')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

