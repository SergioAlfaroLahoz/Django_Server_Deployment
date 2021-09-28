# Django Server Deployment

## How to start?
CMD console
  - django-admin startproject Project_name
  - python manage.py migrate --> Activates project, creates the database 
  - python manage.py runserver --> Execute the server

## Dependencies
Project1
* `__init__.py` File necessary for python, to detect the folder as package
* `settings.py` Configurations
* `urls.py` Index, Content table
* `wsgi.py` Web server
* `asgi.py` Asynchronous Web server

`manage.py` All comands to use

### Manage.py Options

`python manage.py startapp name` Creates new App
  * `__init__.py` Root of our app
  * `admin.py` 
  * `apps.py`
  * `models.py` Main file
  * `tests.py`
  * `views.py` Views manager

`python manage.py (appname)` Checks if there any error in the app code
`python manage.py makemigrations` Creates the database
`python manage.py sqlmigrate (appname) (migratioNumber)` Generates SQL code
`python manage.py migrate` Creates tables in our database
`python manage.py shell` Opens the shell
`python manage.py createsuperuser` Creates a super user to access to admin panel

## Objects
* Request
* HttpResponse
