from flask import Flask , jsonify , request
from flask_restful import Api ,Resource
from env import *
from pclController import *
from pyModbusTCP.client import ModbusClient



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
    c = ModbusClient(host=getIpPLC,port=getPortPLC,auto_open=True)
    print(c)
    is_ok = c.write_single_coil(0,1)
    print(is_ok)
    if is_ok:
        return "is ok"
    else:
        return "is not ok"





if __name__ == "__main__":
    app.run(host=getIp() ,debug=True , port=5000)
   # app.run(debug=True , port=5000)
print("ddd")