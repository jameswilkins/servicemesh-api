from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'a day my ': 'ass'}

class SomeCrap(Resource):
    def get(self):
        return {'Calling from ' : '/foo'}

api.add_resource(HelloWorld, '/')
api.add_resource(SomeCrap, '/foo')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

