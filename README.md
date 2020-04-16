# MedProject
# To create environment pip for project
python -m venv   ./.venv

# To active pip env on window
. venv/Scripts/activate

# To install all library required for this project
. pip install -r requirements.txt

# To set environment deployment variable i.e db name etc
create a .env.dev, then add your detail using key pair
Name=value

# migrate database
python manage.py makemigrations
python manage.py migrate

# to run app
python manage.py runserver



