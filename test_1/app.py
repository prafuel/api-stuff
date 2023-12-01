
from flask import Flask,request,render_template,jsonify


app = Flask(__name__)

@app.route("/",methods=['get','post'])
def server():
    if request.method == "POST":
        return jsonify(request.form)
    return "Server"



if __name__ == "__main__":
    app.run(port=8000, debug=True)