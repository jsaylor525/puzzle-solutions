# Python Django Crash Course

Working through a crash course of Django framework.

https://www.youtube.com/watch?v=D6esTdOLXh4

## High Level Framework

* Do things the "Danjo" way
* * Structured
* Usually the best way possible
* Less freedom but less chances of screwing up
* Good for beginners

## Why Use Django

* Rapid Development
* Full Featured
* High Performance
* Very Secure
* Scalability
* Versatile

## Example sites

* Disqus
* Instagram
* Bitbucket
* Nasa
* Firefox Help Site
* Pinterest
* Onion
* Washington Post
* EventBrite
* Mahalo

## Is Django not quite MVC (Model-View-Controller)

* Django is sometimes referred to as MVC
* Not a "true" MVC framework
* Heavily influenced and uses MVC Concepts
* The "C" is handled by the framework itself


## MVT (Model-Template-View)

* **Model**: Data Access Layer - anything to do with interacting, relating, and validing the data
* **Template**: Presentation Layer - presentation-related decisions
* **View**: Business logic layer - accesses the model and displays the appropriate template

## The Concept of Apps

* Each project/website has separate "apps"
* Can have a single app

Example

```sequence
Project/Website->Blog App
Project/Website->Client App
Project/Website->Store App
```

## Python Virtual Env

* Recommended way to use Django
* Create isolated environments with their own directories
* Separates your Django project instances
* Now very easy to setup on Windows!

## Getting started

### Downloading required Software

* Download python - already have 3.5.3 installed
* Download pip - already have 9.0.1 upgrading to 9.0.3
* * Makesure to do in admin cmd window, errored out in standard cmd window.

### Configure Virtual Envirnoment

* cd into directory and make environment
* <pre>CMD> mkvirtualenv py1</pre>
* Now install packages need for this project
* * <pre>
    workon py1
    pip install django
    pip install mysqlclient
    </pre>

### Create project

* <pre> CMD> django-admin startproject *project-name* </pre>
* **NOTE** in settings.py keep the SECRET_KEY off github for production code, use for SSL
* Install mySQL (Did that already)

### Open up Project

<pre>
python manager.py runserver
</pre>

Visit http://localhost:8000 in browser


### Create Database

* phpMyAdmin
* Machine needs php, mysql, apache httpd ...
* Need to install this following https://www.wikihow.com/Install-phpMyAdmin-on-Your-Windows-PC

Skipping for now

### Create "app" posts

<pre>
python manage.py startapp posts
</pre>

* add posts to INSTALLED_APPS list in settings.py
* add posts/ to urlpatterns list in urls.py
* add view index link in posts/urls.py
* * NOTE name='index' if you don't wrap in quotes to make index a string you get an obscure error
* add function to views.py to return response

