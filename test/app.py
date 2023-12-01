from flask import Flask,jsonify

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/",methods=['get'])
def index():
    return "Index Screen"

@app.route("/time",methods=['get'])
def getTime():
    result = [
        {"time" : 1,
        "more" : True},
        {"time" : 2,
        "more" : True},
        {"time" : 3,
        "more" : False},
        {"time" : 4,
        "more" : True},
        {"time" : 5,
        "more" : False},
        {"time" : 6,
        "more" : False},
    ]

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, port=8080)