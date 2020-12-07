from flask import Flask , jsonify , request
from flask_restful import Api ,Resource

from env import *
from pclController import *
from pyModbusTCP.client import ModbusClient
import requests



app = Flask(__name__)
api = Api(app)

@app.route("/test" , methods=['GET'])
def test():
    return jsonify({ 
            "status": "success",
            "statusCode": 201
        })

@app.route("/test", methods=['POST'])
def test1():
    return  getIp()

@app.route("/testplc", methods=['GET'])
def testplc():
    c = ModbusClient(host=getIpPLC(),port=getPortPLC(),auto_open=True)
    print(c)
    is_ok = c.write_single_coil(0,1)
    print(is_ok)
    response = requests.post('http://192.168.1.132:8080/app/post/test1')
    print(response.json())
    data = response.json()
    print(data["data"])
    if is_ok:
        return jsonify({
            "status": "success",
            "statusCode": 201,
            "data" : True
        })
        # 192.168.1.132:8080/app/post/test1        
    else:
        return jsonify({
            "status": "success",
            "statusCode": 200,
            "data" : False
        })

@app.route("/machine/command/gasOut" , methods=["POST"])
def machineCommandGasOut():
    # return jsonify({"data" : request.form['number_order']})
    return jsonify({
                "status": "success",
                "statusCode": 201,
                "data" : True
            })































if __name__ == "__main__":
    app.run(host="192.168.1.156" ,debug=True , port=5000)
    # app.run(debug=True , port=5000)
print("ddd")