from flask import Flask , jsonify , request
from flask_restful import Api ,Resource
from env import *
from pclController import *


app = Flask(__name__)
api = Api(app)

todos = {}
# @app.route("/test" , methods=['GET'])
# def test():
#     return jsonify({'tasks': "test api flask"})

# @app.route("/test", methods=['POST'])
# def test1():
#     return  getIp()

# @app.route("/testplc", methods=['GET'])
# testPCL()

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}
    
    def post(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api.add_resource(TodoSimple, '/test')
api.add_resource(TodoSimple, '/<string:todo_id>')



if __name__ == "__main__":
    app.run(host=getIp() ,debug=True , port=5000)
   # app.run(debug=True , port=5000)
print("ddd")