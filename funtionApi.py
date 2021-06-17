from flask import Flask , jsonify , request
from flask_restful import Api

from env import *
from pclController import *
from command import *
from pyModbusTCP.client import ModbusClient
import requests
import time
import socket



def updateStatusMachine(status) :
    #return ip
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
    return "192.168.1.156"

