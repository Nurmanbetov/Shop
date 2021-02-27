# Shop

The first thing to do is to clone the repository:

$ git clone https://github.com/Nurmanbetov/Shop.git


Create a virtual environment to install dependencies in and activate it:

$ virtualenv venv
$ source venv/bin/activate

Then install the dependencies:

(venv)$ pip install -r requirements.txt

Before applying migrations, create a settings.py file in the Shop folder and write your own 
details instead of EXAMPLE:



We apply migrations and start the server:

(venv)$ python manage.py makemigrations

(venv)$ python manage.py migrate

(venv)$ python manage.py runserver