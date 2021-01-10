# Django Web Application
A Web application based on `python3.9` and `Django3.1`.

## Step 1: create virtual environment
`//pip install virtualenv`

`//virtualenv env`

`python -m venv env`

## Step 2: activate that environment
`env\Scripts\activate`

## Step 3: install Django in that environment
`//pip install -r requirements.txt -t ./env/Lib/site-packages/`

`//pip install Django -t env/Lib/site-packages/`

`pip install django`

## Step 4: create django project named mysite
`django-admin startproject mysite`

## Run project
`python manage.py runserver`

## Start app
`python manage.py startapp polls`
