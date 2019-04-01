# Django REST-AUTH Demo App
A demo authentication app by django rest-auth

## Installation

### In local development

It is pretty-much straight forward.

1. Clone this repository
2. run docker using docker-compose build server
3. Run docker-compose exec server bash
4. Run pipenv run ./manage.py makemigrations
5. Run pipenv run ./manage.py migrate
6. Run docker-compose server bash

## What user can do

1. User can Register new account with email verification
2. User can login 
3. Only super admin can view all user-list
4. Normal user can create their onw profile data (Phone, Address, Profile Image)