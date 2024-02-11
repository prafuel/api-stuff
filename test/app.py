from flask import Flask,jsonify

from flask_cors import CORS

import time

app = Flask(__name__)
CORS(app)

@app.route("/",methods=['get'])
def index():
    return "Index Screen"

@app.route("/time",methods=['get'])
def getTime():
    result = {
        "local_time" : time.localtime()
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, port=8080)