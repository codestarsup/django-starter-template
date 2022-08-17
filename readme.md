# Django Project Boilerplate
This repository is a boilerplate Django project for quickly getting started. Created by **Code Stars Up** team

</br>

## Table Of Contents
- [Getting Started](#getting-started)
- [Custom Commands](#custom-commands)
    -[startapp](#startapp)

## Getting Started

1. First you must clone the boilerplate, to do it so use the command below in terminal:
    ```bash
    $ git clone git@github.com:codestarsup/django-starter-template.git
    ```

2. Build the dockerfile (Note: If you dont have docker and docker compose already installed flow the instructions of [Docker official docs](https://docs.docker.com/compose/install/) to install them):

    ```bash
    $ docker compose build
    ```
3. Your image is ready and you can run your project by typing `$ docker compose up` in the terminal

5. To intract with docker and run you bash scripts like `python manage.py makemigrations` you can write the command like bellow
    ```bash
    $ docker compose run web python manage.py <your_command>
    ```
    Or open a terminal session inside container and run with your django project commands simply
    ```bash
    $ docker compose run web bash
    
    >> django@ :/code$ python manage.py makemigrations
    ```

## Custom Commands

In this boilerplate we have written some usefull commands to make it easier to work with django in this environment.

### startapp

**usage**:
Create django apps within the boilerplate structure

**config**: 
You can change the variable `APPS_DIR` in `config/settings/apps.py` which points to abolute path of the django apps directory to change the default one.

**example**:
```bash
$ docker compose run web python manage.py startapp core
``` 
or ignore `APPS_DIR` and give the directory yourself, which is not recommended at all:
```bash
$ docker compose run web python manage.py startapp core --appdir /home/django/core/apps/app
```

### rmapp

**usage**:
Remove existing django application.

**example**:
```bash
$ docker compose run web python manage.py rmapp core
```

### renameproject

<!-- TODO: complete this part by shfra -->