# MedProject
# To create environment pip for project
python -m venv   ./.venv

# To active pip env on window
. venv/Scripts/activate

# To install all library required for this project
 pip install -r requirements.txt

# To set environment deployment variable i.e db name etc
create a .env, then add your detail using key pair
Name=value
===================================
List of NameValue for .env file
===================================
==================================
DEBUG = True
ALLOWED_HOSTS = *
DATABASE_NAME = your-db-name
DATABASE_USER = your-username
DATABASE_PASSWORD = your-password
DATABASE_HOST = localhost
DATABASE_PORT = 5432
ALLOWED_HOSTS = *
===================================


# to run migration
python manage.py makemigrations

# to apply migration
python manage.py migrate

# to run app
python manage.py runserver



