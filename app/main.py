from fastapi import FastAPI
from app.schema import InputData, PredictionOutput
from app.model import predict

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/predict", response_model=PredictionOutput)
def get_prediction(data: InputData):
    result = predict(data.features)
    return {"prediction": result}
