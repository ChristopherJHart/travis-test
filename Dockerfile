FROM python:3.8

EXPOSE 8990/udp

WORKDIR /app

COPY script.py ./
COPY requirements.txt ./

RUN pip install -r requirements.txt

CMD [ "python", "script.py" ]
