uses python 3.6
Developed on Ubuntu 16.04

change to the base directory that has manage.py file in it

create a virtual env safhackathon
activate the virtual environment
install the requirements.txt dependencies

run python manage.py makemigrations
run python manage.py migrate
run python manage.py createsuperuser

The test credentials for the included sqlite DB are
username: admin
password: admin123

log in the application on http://127.0.0.1:8000/admin/