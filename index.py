from flask import Flask , jsonify , request
from flask_restful import Api ,Resource
from env import *
from pclController import *


app = Flask(__name__)
api = Api(app)

@app.route("/test" , methods=['GET'])
def test():
    return jsonify({'tasks': "test api flask"})

@app.route("/test", methods=['POST'])
def test1():
    return  getIp()

@app.route("/testplc", methods=['GET'])
def testplc():
    testPCL()





if __name__ == "__main__":
    app.run(host=getIp() ,debug=True , port=5000)
   # app.run(debug=True , port=5000)
print("ddd")