FROM python:3.7-slim-buster

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . .

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "main.py"]
