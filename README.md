Commands:

Install the application: 

    pip install requirements.txt

    django-admin startproject interview_app

    cd interview_app

    django-admin startapp questions

Start the application:

    python manage.py runserver

    python manage.py makemigrations

    python manage.py migrate

Explanation of Each Part: 
1. interview_app: 
This is the root directory of your Django project.

    manage.py: A command-line utility that lets you interact with this Django project. You use it to run commands such as runserver, migrate, and startapp.

2. interview_app/interview_app/
This is the inner directory that contains the main settings and configurations for your Django project.

    __init__.py: An empty file that tells Python this directory should be considered a Python package.
    asgi.py: Entry point for ASGI-compatible web servers to serve your project.
    settings.py: Contains settings and configurations for your Django project (e.g., database settings, installed apps).
    urls.py: The URL declarations for your project; a "table of contents" of your Django-powered site.
    wsgi.py: Entry point for WSGI-compatible web servers to serve your project.
3. interview_app/questions/
This is your Django app directory where you manage your application's models, views, templates, and static files.

    __init__.py: An empty file that tells Python this directory should be considered a Python package.
    admin.py: Configuration file for Django admin interface. Here you register models so that they can be managed through the Django admin interface.
    apps.py: Configuration file for the app.
    migrations/: Directory that stores database migrations; these are changes to the database schema.
    __init__.py: An empty file that tells Python this directory should be considered a Python package.
    models.py: File where you define the data models for your application. In this case, you defined Language and Question models.
    tests.py: File where you write tests for your application.
    views.py: File where you define the views (i.e., the functions/classes that handle requests and return responses).
    urls.py: URL configuration specific to this app. It includes URL patterns that route to the app’s views.
    templates/questions/: Directory that contains HTML template files.
    home.html: Template for the home page displaying the tiles for different languages/frameworks.
    detail.html: Template for the detail page displaying questions and answers for a selected language/framework.
    static/css/: Directory for static files (e.g., CSS, JavaScript, images).
    styles.css: CSS file for styling the templates.
4. db.sqlite3
This is the SQLite database file where your project's data is stored.

This structure organizes your Django project into reusable components, each with a clear purpose. This modular approach makes it easier to manage and scale your project.



interview_app/
├── interview_app/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── questions/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   ├── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   └── questions/
│   │       ├── home.html
│   │       └── detail.html
│   ├── static/
│       └── css/
│           └── styles.css
├── db.sqlite3
├── manage.py
