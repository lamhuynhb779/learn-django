## Django Web Application
A Web application based on `python3.9` and `Django3.1`.

# Step 1: create virtual environment
//pip install virtualenv
//virtualenv env
python -m venv env

# Step 2: activate that environment
env\Scripts\activate

# Step 3: install Django in that environment
//pip install -r requirements.txt -t ./env/Lib/site-packages/
//pip install Django -t env/Lib/site-packages/
pip install django

# Step 4: create django project named mysite
django-admin startproject mysite

# Run project
python manage.py runserver

# Start app
python manage.py startapp polls

# Create migrations
cd mysite
python manage.py makemigrations

# Create database (file db.sqlite3) from file migrations
python manage.py migrate

# Go to shell to check DB
python manage.py shell
>>> from polls.models import Question

# Get all records of Question
>>> Question.objects.all()

# Create record of Question
>>> from django.utils import timezone
>>> q = Question(question_text = "ban thich mau gi?", time_public = timezone.now())
>>> q.save()
>>> q.id

# Create record of Choice
>>> from polls.models import Choice
>>> c = Choice(question = q, choice_text = "do", vote = 0)
>>> c.save()
>>> d = Choice(question = q, choice_text = "xanh", vote = 0)
>>> d.save()

# Create account admin
python manage.py createsuperuser
