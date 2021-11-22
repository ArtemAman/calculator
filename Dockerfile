FROM python:3.9
RUN mkdir /app
COPY ./requirements.txt /app
COPY . /app/
RUN python -m pip install -r /app/requirements.txt
WORKDIR /app/calculator
RUN python manage.py migrate
ENTRYPOINT ["python","manage.py","runserver", "0.0.0.0:8000"]


