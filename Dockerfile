FROM python:3 

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . code/

WORKDIR /code/

RUN pip install -r requirements/local.txt

