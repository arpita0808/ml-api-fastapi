FROM python:3.10

WORKDIR /app

# copy dependency list first (better caching)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# now copy app code
COPY . .

# expose port
EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
