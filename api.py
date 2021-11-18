from flask import Flask
from flask_restful import Resource, Api

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
api.add_resource(HelloWorld, '/')
api.add_resource(SomeCrap, '/foo')
api.add_resource(Counter, '/count')
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

