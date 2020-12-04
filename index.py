from flask import Flask , jsonify
from flask_restful import Api
from env import *

print(getIp())
app = Flask(__name__)
api = Api(app)

@app.route("/test" , methods=['GET'])
def test():
    return jsonify({'tasks': "test api flask"})



if __name__ == "__main__":
    #app.run(host="0.0.0.0" ,debug=True , port=80)
    app.run(debug=True , port=5000)
print("ddd")