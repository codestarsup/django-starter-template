# Django Project Boilerplate

This repository is a boilerplate Django project for quickly getting started. Created by **Code Stars Up** team

<br>

## Table Of Contents

- [Getting Started](#getting-started)
- [Custom Commands](#custom-commands)

  - [startapp](#startapp)
  - [startapi](#startapi)
  - [Firebase cloud messaging instruction](#firebase-cloud-messaging)
- [Notes](#notes)
   - [Database host & name](#db_and_host_name)

## Getting Started

1. Before anything, please run below command to add pre-commit hook, for code quality assurance:
    ```bash
    # If `make` is installed
    $ make githook

    # or

    # If `make` is an unrecognized command
    $ git config --local core.hooksPath ./.githooks/
    ```
   Make sure you will have your pipeline on GitLab, referencing `.gitlab-ci.yml` file.<br><br>

2. First you must clone the boilerplate, to do it so use the command below in terminal:
    ```bash
    $ git clone git@github.com:codestarsup/django-starter-template.git
    ```

3. Build the dockerfile (Note: If you don't have docker and docker compose -f docker-compose.local.yml already installed (** Consider renaming the environment variables' files to .django, .postgres and .redis **)
   flow the instructions of [Docker official docs](https://docs.docker.com/compose/install/) to install them):

    ```bash
    $ docker compose -f docker-compose.local.yml build
    ```
4. Your image is ready, and you can run your project by typing `$ docker compose -f docker-compose.local.yml up -d` in
   the terminal

<br>

5. To interact with docker and run you bash scripts like `python manage.py makemigrations` you can write the command
   like bellow
    ```bash
    $ docker compose -f docker-compose.local.yml run web python manage.py <your_command>
    ```
   Or open a terminal session inside container and run with your django project commands simply
    ```bash
    $ docker compose -f docker-compose.local.yml run web bash

    >> django@ :/code$ python manage.py makemigrations
    ```

## Custom Commands

In this boilerplate we have written some usefully commands to make it easier to work with django in this environment.

### startapp

**usage**:
Create django apps within the boilerplate structure.

**config**:
You can change the variable `APPS_DIR` in `config/settings/apps.py` which points to absolute path of the django apps
directory to change the default one.

**example**:

```bash
$ docker compose -f docker-compose.local.yml run web python manage.py startapp core
```

or ignore `APPS_DIR` and give the directory yourself, which is not recommended at all:

```bash
$ docker compose -f docker-compose.local.yml run web python manage.py startapp core --appdir /home/django/core/apps/app
```

### startapi

**usage**:
Create files and directories needed to develop restful apis in the app directory.

**example**:

```bash
$ docker compose -f docker-compose.local.yml run web python manage.py startapi core #To create files needed for rest api development in the core app directory
```

or you can create the files within every other directory your app lives in:

```bash
$ docker compose -f docker-compose.local.yml run web python manage.py startapi core --appdir /code/foo/
```

### Firebase cloud messaging

For setup firebase in your project please run this command and **install** the **requirements**

**example**:

```bash
$ docker compose -f docker-compose.local.yml run web python manage.py fcmup
```

For local development run

```bash
$ pip install -r requirements\base.txt
```

For Docker

```
$ When you build the docker image it's automatically installs the requirements for project
```

After the installation is complete you will see the `fcm.py` in core directory.

Then follow these steps to set up the firebase configuration.

1. Go to https://firebase.google.com/ and create an account.
2. Use this https://console.firebase.google.com/ and add your project to the firebase console.
3. Credentials file will be generated through Project **settings -> Service accounts tab -> Generate new private key
   button**,
   within the Firebase console.
4. Put the credential file in the **django-starter project directory**.
5. Rename the json file to `firebase_key.json`.
6. if `FIREBASE_CREDENTIALS_FILE_NAME` should be anything rather than `firebase_key.json`, it must be added in
   **.gitignore**
   and change the file name in **Dockerfiles**. (If you have changed the file name in **step 5** you can skip this
   step.)
7. Set `FIREBASE_CREDENTIALS_FILE_NAME` with the credential file name. You can access
   this variable within `django-starter/envs/.django.example`.
8. Default _GCP resource location_ configuration should be set, in **Project Settings -> General tab**, within Firebase
   console.
9. Add your app through **project settings -> General tab -> Add app**. And then for the frontend provide the SDK
   configuration or JSON file Or you can simply add the developers to the project in firebase console so they can get
   whatever they need.
10. For the backend, you're done with the job, Enjoy the Notifications :)

### renameproject

**usage**:
Rename the project in all necessary files.

**example**:

```bash
$ docker compose -f docker-compose.local.yml run web python manage.py renameproject config codestars # "config" is the current name of project and "codestars" is the new name
```


## Notes

### Database host & name

**Note #1:** If you are going to change database container name from starter_database to another name such as project_x_database. consider to change the .postgres env file accordingly. You should set the host name
to project_x_database. 
