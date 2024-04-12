# Best-PC

## Description

- This project is part of the backend for my future app Best PC, which I plan to release in a couple of months. This repository's purpose is to show my backend skills to a future employer.
- About the app: a PCPartPicker copy but with support for shops from Romania. The app is still in development.
- Currently, the project uses the in-build Django template engine but I plan to make the backend an API using the Django REST framework.

## How to run the project?

- Firstly we need to create a virtual environment and then activate it.

```bash
virtualenv env

env\scripts\activate
```

- After that we need to install all the packages using `pip`.

```bash
pip install -r requirements.txt
```

- Now we only need to run the server
- We first go to the project directory and then we use the `manage.py` file to run the server

```bash
cd best-pc
python manage.py runserver
```

- To connect to an admin account use the username `admin` and password `admin`

## Features

- As with any Django project the project is broken down into multiple apps
- We will have 3 apps: one for posting blogs, one for building a PC, and one for checking the parts price history
- Currently working on the PC-building app

### Blog app - features

- Create a blog post by an admin
- Homepage with filter for posts and search
- User authentification
- Comment section and likes for blogs
- Comments can be deleted by the user or by an admin
