
from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

with open("mlr.pkl", "rb") as file:
    mlr = pickle.load(file)

@app.route("/", methods=['get','post'])
def main():
    if request.method == "POST":
        unit = request.form.get("unit")
        predicted = run_model(int(unit))
        output = f"unit : {unit} <br> Predicted Price: {predicted}"
        return output
    return render_template("index.html")


def run_model(unit : int) :
    input = np.array([unit]).reshape(1,1)
    output = mlr.predict(input)
    # print(output)
    return output



if __name__ == "__main__" :
    app.run(debug=True, port=8000)