FROM python:3 

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . code/

WORKDIR /code/

RUN cp commands/* /usr/bin/

RUN pip install -r requirements/local.txt

WORKDIR /usr/bin/

RUN chmod +x $(ls /code/commands)

WORKDIR /code/
