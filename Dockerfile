FROM python:3.9

RUN python3 -m venv /venv
ENV PATH=/venv/bin:$PATH

WORKDIR /mqtt-dashboard

COPY requirements.txt requirements.txt

RUN python3 -m pip install -r requirements.txt


COPY . .


CMD ["python3", "./main.py"]
