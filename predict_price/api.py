
from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

with open("./predict_price/dtr.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/", methods=['get','post'])
def main():
    if request.method == "POST":
        unit = request.form.get("unit")
        predicted = run_model(int(unit))
        output = {
            "unit" : unit,
            "predicted" : float(predicted)
        }
        return output
    return render_template("index.html")


def run_model(unit : int) :
    input = np.array([unit]).reshape(1,1)
    output = model.predict(input)
    # print(output)
    return output



if __name__ == "__main__" :
    app.run(debug=True, port=8000)