
import pickle
import pandas as pd
import numpy as np
import json
from flask import Flask, request
from flask_cors import CORS

ev_df = pd.read_csv('imp_ev_col.csv')
img_links = pd.read_csv("images.csv")

# to predict range
rf_range_model = pickle.load(open("rf_range_predict.pkl", "rb"))

# to predict top speed
rf_speed_model = pickle.load(open("rf_speed_predict.pkl", "rb"))

# standard format to output data response
def output_format(output) -> dict:
    return {
        "output": output
    }

# model prediction
def make_prediction(model, *args) -> int:
    input = np.array(args).reshape(1, -1)
    result = model.predict(input)[0]
    return round(result, 2)

# routes
route_dict = {
    "range" : "Electric Range",
    "speed" : "Top Speed",
}


app = Flask(__name__)
CORS(app)


@app.route("/")
def main():
    return "Flask Server"


@app.route("/predict/<key>", methods=['post'])
def get_range(key: str):

    # route
    try:
        route = route_dict[key]
    except Exception as e:
        return output_format(404)

    # get data from request
    requested_data = request.json
    # parameter to predict range => speed, battery, weight
    param = list(requested_data.values())

    result = make_prediction(rf_range_model, *param)

    # Acceleration, speed, range, battery, weight
    data = ev_df[ev_df[route] >= result].reset_index(drop=True)

    # id, brand, link
    img = img_links[img_links['id'].isin(data['id'])].reset_index(drop=True)

    # 'Acceleration 0 - 100 km/h', 'Top Speed', 'Electric Range', 'Battery Capacity','Gross Vehicle Weight (GVWR)'

    filter_list = [
        {
            "id": str(img['id'][i]),
            "brand": img['Brand'][i],
            "link": img['link'][i],
            "acceleration": str(data['Acceleration 0 - 100 km/h'][i]),
            "speed": str(data['Top Speed'][i]),
            "range": str(data['Electric Range'][i]),
            "battery": str(data['Battery Capacity'][i]),
            "weight": str(data['Gross Vehicle Weight (GVWR)'][i]),
        }
        for i in range(data.shape[0])
    ]

    return output_format(
        {
            'result': str(result),
            'filter_list': json.dumps(filter_list)
        }
    )

if __name__ == "__main__":
    app.run(debug=True, port=8000)
