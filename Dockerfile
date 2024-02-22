FROM python:3.11

WORKDIR /opt/aoo-app

COPY age_of_origins .
COPY requirements.txt .

RUN pip3 install -r requirements.txt && \
    python manage.py migrate

CMD ["python","manage.py", "runserver", "0.0.0.0:8000"]