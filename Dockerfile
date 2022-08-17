FROM python:3 

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN useradd -d /home/django -m -s /bin/bash django && echo "django:django" | chpasswd && adduser django sudo 

USER django

COPY --chown=django:django . code/

WORKDIR /code/

RUN pip install -r requirements/local.txt
