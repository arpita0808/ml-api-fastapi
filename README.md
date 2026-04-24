# ML Model API using FastAPI & Docker

##  Overview
This project demonstrates how to deploy a trained machine learning model as a REST API using FastAPI and Docker.

## Features
- FastAPI-based API
- Model inference endpoint
- Docker container support
- Public access using ngrok

## Endpoints

### GET /
Returns API status

Response:
{
  "message": "API is running"
}



### POST /predict

Request:
{
  "features": [5.1, 3.5, 1.4, 0.2]
}

Response:
{
  "prediction": 0
}



##  Run Locally

pip install -r requirements.txt  
uvicorn app.main:app --reload  



##  Docker

docker build -t ml-api .  
docker run -p 8000:8000 ml-api  



## Demo
- Swagger UI tested
- Prediction endpoint working



##  Tech Stack
- Python
- FastAPI
- Scikit-learn
- Docker

- ## 📸 Demo

### Swagger UI
![Swagger UI](images/swagger.png)
<img width="2879" height="1725" alt="image" src="https://github.com/user-attachments/assets/c64f0343-09a4-4b4d-a82b-cc6e1c8ad942" />


### Prediction Output
![Output](images/output.png)
<img width="2724" height="602" alt="image" src="https://github.com/user-attachments/assets/de557be7-f912-4a59-8cd7-3503765040bc" />
