
import pickle
import numpy as np

mlr = pickle.load(open("./mlr.pkl","rb"))
dtr = pickle.load(open("./dtr.pkl","rb"))

test_data = np.array([15,89,2015,139568,1248,1,1161,6]).reshape(1,8)

mlr_prediction = mlr.predict(test_data)
print(f"Multiple Linear Regression {mlr_prediction}")

dtr_prediction = dtr.predict(test_data)
print(f"Decision Tree Regression {dtr_prediction}")
