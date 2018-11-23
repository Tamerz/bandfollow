# BandFollow

[![Build Status](https://travis-ci.org/Tamerz/bandfollow.svg?branch=master)](https://travis-ci.org/Tamerz/bandfollow)
#### Running with Docker

Make sure Docker is installed.
* macOS: <https://store.docker.com/editions/community/docker-ce-desktop-mac>
* Windows: <https://store.docker.com/editions/community/docker-ce-desktop-windows>

From a terminal:
```
$ docker-compose up --build
```

In a new terminal, go into the same directory and run:
```
$ docker-compose run web python3 manage.py migrate
```

Once it brings up the two machines, you should be able to browse to
<http://127.0.0.1:8000> on your local machine.

Image sources:
Icons from the Noun project:
 *** add event by Aneeque Ahmed 
 *** sign up by anon
 *** musician by corpus delicti
 *** Map by Anton Kovalev
