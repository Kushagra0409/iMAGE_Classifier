FROM python:3.7-slim-buster


RUN apt-get update && apt-get install -y python3-dev build-essential

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8080", "app.server:app"]
