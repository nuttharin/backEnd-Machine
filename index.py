from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

@app.route("/test")
def test():
        return "test api flask"



if __name__ == "__main__":
    app.run(debug=True , port=5000)

print("ddd")