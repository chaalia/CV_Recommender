### Author
*************** SOGIT ***************

khaledhadjali1@gmail.com

rjab.chaalia@isimg.tn

# cv_uploader

cv_uploader is a _short description_. It is built with [Python3 using the [Django Web Framework][1].

This project has the following basic apps:

* App1 accounts
the account app is about authentication and regestration , reset passwrod ................... etc
* App2 cv_uploader
this app contain the genral settings of the project and the main urls .
* App3 profiles
the profile app which contain the process of uploading CV and extracting data from .

## Installation
* to build image --- build without cache
docker-compose build .
docker-compose build --no-cache .
### Quick start
docker-compose up -d

### enter container
docker-compose exec my_parser bash
after entering the container u have to run migration
Run migrations:

    python manage.py migrate

### Detailed instructions

Take a look at the docs for more information.

[0]: https://www.python.org/
