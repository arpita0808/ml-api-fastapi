# ML Model API using FastAPI & Docker

##  Overview

This project demonstrates how to deploy a machine learning model as a REST API using FastAPI and Docker. The API provides real-time predictions based on input features.


##  Features

* FastAPI-based REST API
* Machine Learning model integration
* Real-time prediction endpoint
* Docker container support
* Interactive Swagger UI documentation



##  API Endpoints

###  GET /

Returns API status

**Response:**

```json
{
  "message": "API is running"
}
```

---

###  POST /predict

**Request:**

```json
{
  "features": [5.1, 3.5, 1.4, 0.2]
}
```

**Response:**

```json
{
  "prediction": 0
}
```


##  Model Info

* Dataset: Iris Dataset
* Algorithm: Logistic Regression *(change if different)*
* Output: Class prediction (0, 1, 2)

---

##  Tech Stack

* Python
* FastAPI
* Scikit-learn
* Docker



## How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the API

```bash
uvicorn app.main:app --reload
```

### 3. Open Swagger UI

[http://127.0.0.1:8000/docs](https://benson-inartificial-barbie.ngrok-free.dev/docs#/default/get_prediction_predict_post)

---

##  Run with Docker

### Build Docker Image

```bash
docker build -t ml-api .
```

### Run Container

```bash
docker run -p 8000:8000 ml-api
```


## Deployment

API can be exposed publicly using ngrok for testing and demo purposes.


##  Example Prediction

Input: [5.1, 3.5, 1.4, 0.2]
Output: 0



##  Demo

## Swagger UI
![Swagger](images/swagger.png)

## Prediction Output
![Output](images/output.png)
