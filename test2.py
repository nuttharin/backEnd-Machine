
from flask import Flask , jsonify , request
from flask_restful import Api ,Resource

from env import *
from pclController import *
from command import *
from pyModbusTCP.client import ModbusClient
import requests


ip_address = Flask.request.remote_addr
print("Requester IP: " + ip_address)