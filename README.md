# MedProject

# Getting started
You will need to copy the .settings.env file and rename it .env
Inside there you can fill in the values of the environment variables and you're all good to go.

# or

# To set environment deployment variable i.e db name etc
create a .env, then add your detail using key pair
Name=value
===================================
List of NameValue for .env file
===================================
==================================
DEBUG = True
ALLOWED_HOSTS = http://localhost:4200,http://127.0.0.1:9000
DATABASE_NAME = your-db-name
DATABASE_USER = your-username
DATABASE_PASSWORD = your-password
DATABASE_HOST = localhost
DATABASE_PORT = 5432
===================================


# To create environment pip for project
python -m venv   ./venv

# To active pip env on window
# if using bash
. venv/Scripts/activate
# if using cmd for windows
.\venv\Scripts\activate
# for mac
./Scripts/activate.bat

# To install all library required for this project
pip install -r requirements.txt

# to run migration
python manage.py makemigrations

# to apply migration
python manage.py migrate

# to run app
python manage.py runserver



