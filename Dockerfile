FROM python:3.9
RUN mkdir /app
COPY ./requirements.txt /app
COPY . /app/
RUN python -m pip install -r /app/requirements.txt
WORKDIR /app/calculator



