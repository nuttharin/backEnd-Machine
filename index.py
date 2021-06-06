from flask import Flask , jsonify , request
from flask_restful import Api ,Resource

from env import *
from pclController import *
from command import *
from pyModbusTCP.client import ModbusClient
import requests



app = Flask(__name__)
api = Api(app)
c = ModbusClient(host=getIpPLC(),port=getPortPLC(),auto_open=True)
is_ok = True
 
coil_return = 0
coil_receive = 1


@app.route("/test" , methods=['GET'])
def test():
    return jsonify({ 
            "status": "success",
            "statusCode": 201
        })

@app.route("/test", methods=['POST'])
def test1():
    return  getIp()




# @app.route("/testplc", methods=['GET'])
# def testplc():
#     # c = ModbusClient(host=getIpPLC(),port=getPortPLC(),auto_open=True)
#     print(c)
#     is_ok = c.write_single_coil(0,1)
#     print(is_ok)
#     response = requests.post('http://192.168.1.132:8080/app/post/test1')
#     print(response.json())
#     data = response.json()
#     print(data["data"])
#     if is_ok:
#         return jsonify({
#             "status": "success",
#             "statusCode": 201,
#             "data" : True
#         })
#         # 192.168.1.132:8080/app/post/test1        
#     else:
#         return jsonify({
#             "status": "success",
#             "statusCode": 200,
#             "data" : False
#         })

@app.route("/machine/command/gasOutx" , methods = ['POST'])
def machineCommandGasOutx():
    # return jsonify({"data" : request.form['number_order']})    
    number_order = request.json['number_order']
    order_id = request.json['order_id']
    print(number_order)
    print(order_id)
    if number_order is None:
        return  jsonify({
                "status": "error",
                "statusCode": 200,
                "data" : "not have parameter ( number_order )"
            })
    else:        
        # c = ModbusClient(host=getIpPLC(),port=getPortPLC(),auto_open=True)
        i = 1
        while i <= number_order :
            print("status write") 
            is_ok = True                   
            # is_ok = c.write_single_coil(0,1)
            # print(c)            
            # print(is_ok)
           
            if is_ok : 
                # api update
                # print("if is_ok")
                url = "http://"+getIpApi()+"/app/post/fromMachine/update/quality/gasOut"
                myobj = {
                            'order_id': order_id ,  
                            'quality' : i
                        }
                resJson = requests.post(url, data = myobj)
                # print(i)
                # print(number_order)
                # print(resJson.json()["statusCode"])

                if resJson.json()["statusCode"] == 201 : 
                    # print("update complete")
                    i+=1

                if i == number_order :
                    return  jsonify({
                            "status": "success",
                            "statusCode": 201,
                            "data" : "write_single_coil complete"
                        })
                # i+=1
            else :
                print("else is_ok")
                return  jsonify({
                    "status": "error",
                    "statusCode": 200,
                    "data" : "error write_single_coil"
                })
        
@app.route("/machine/command/gasInx" , methods = ['POST'])
def machineCommandGasInx():
    # return jsonify({"data" : request.form['number_order']})    
    number_order = request.json['number_order']
    order_id = request.json['order_id']
    print(number_order)
    print(order_id)
    if number_order is None:
        return  jsonify({
                "status": "error",
                "statusCode": 200,
                "data" : "not have parameter ( number_order )"
            })
    else:        
        # c = ModbusClient(host=getIpPLC(),port=getPortPLC(),auto_open=True)
        i = 1
        while i <= number_order :
            print("status write") 
            is_ok = True                   
            # is_ok = c.write_single_coil(0,1)
            # print(c)            
            # print(is_ok)
           
            if is_ok : 
                # api update
                # print("if is_ok")
                url = "http://"+getIpApi()+"/app/post/fromMachine/update/quality/gasOut"
                myobj = {
                            'order_id': order_id ,  
                            'quality' : i
                        }
                resJson = requests.post(url, data = myobj)
                # print(i)
                # print(number_order)
                # print(resJson.json()["statusCode"])

                if resJson.json()["statusCode"] == 201 : 
                    # print("update complete")
                    i+=1

                if i == number_order :
                    return  jsonify({
                            "status": "success",
                            "statusCode": 201,
                            "data" : "write_single_coil complete"
                        })
                # i+=1
            else :
                print("else is_ok")
                return  jsonify({
                    "status": "error",
                    "statusCode": 200,
                    "data" : "error write_single_coil"
                })


@app.route("/machine/command/getVolume" , methods = ['POST'])
def machineCommandGetVolume():
    # return jsonify({"data" : request.form['number_order']})    
    command_str = request.json['command_str']
    coil_number = getCommandWrite(command_str)
    print(coil_number)
    print("status write coil") 
    is_ok = True                   
    is_ok = c.write_single_coil(0,coil_number)
    print(c)            
    print(is_ok)
    return jsonify({ 
            "status": "success",
            "statusCode": 201
        })
        

@app.route("/machine/command/test" , methods = ['POST'])
def machineCommandTest():
    # return jsonify({"data" : request.form['number_order']})    
    print("api => /machine/command/test") 
    command_str_0 = request.json['command_str_0']
    command_str_1 = request.json['command_str_1']
    coil_number_1 = command_str_1                  
    is_ok = c.write_single_coil(command_str_0,coil_number_1)
    print(c)            
    print(is_ok)
    if is_ok :
        print("success")
    
    else :
        print("not success")

    return jsonify({ 
            "status": "success",
            "statusCode": 201
        })


@app.route("/machine/command/gasOut" , methods = ['POST'])
def machineCommandGasOut():
    print("api => /machine/command/test") 
    command_str_0 = request.json['command_str_0']
    command_str_1 = request.json['command_str_1']
    coil_number_1 = command_str_1                  
    is_ok = c.write_single_coil(command_str_0,coil_number_1)
    print(c)            
    print(is_ok)
    if is_ok :
        print("success")
    
    else :
        print("not success")

    return jsonify({ 
            "status": "success",
            "statusCode": 201
        })




        
@app.route("/machine/command/gasIn" , methods = ['POST'])
def machineCommandGasIn():
    print("api => /machine/command/test") 
    command_str_0 = request.json['command_str_0']
    command_str_1 = request.json['command_str_1']
    coil_number_1 = command_str_1                  
    is_ok = c.write_single_coil(command_str_0,coil_number_1)
    print(c)            
    print(is_ok)
    if is_ok :
        print("success")
    
    else :
        print("not success")

    return jsonify({ 
            "status": "success",
            "statusCode": 201
        })

        





























if __name__ == "__main__":
    app.run(host="192.168.250.12" ,debug=True , port=5000)
    # app.run(debug=True , port=5000)
print("ddd")