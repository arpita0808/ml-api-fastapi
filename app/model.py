import pickle
import numpy as np

with open("app/model.pkl", "rb") as f:
    model = pickle.load(f)

def predict(data):
    arr = np.array(data).reshape(1, -1)
    return int(model.predict(arr)[0])
