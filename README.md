# Django/Python CRUD

The CRUD is fundamentals of every web application. In this instance, you have the simple web application with registration form and products list. The focus wasn't on the frontend, but bootstrap is included in the project for further developing.

## Installing

1. Using Command Prompt or Node install `virtualenv venv` to your created folder and       start it with `.\venv\Scripts\activate.bat`
2. install Django `pip install Django==1.11.0`
3. mkdir src && cd src
4. git init
5. git clone https://igortosic@bitbucket.org/igortosic/django-python-crud.git
6. cd djagno-python-crud
7. `python manage.py runserver` <port>

You might install `pip install Pillow` after you start the server

## Default user is:
    user: admin
    password: administrator

## Notes:
Also, you can create superuser with `python manage.py createsuperuser` from Command Prompt.

Default local server is: http://127.0.0.1:8000

Manage your products from: http://127.0.0.1:8000/admin/

Logout link is not in use. Logout from admin dashboard.
