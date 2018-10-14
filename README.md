# BandFollow

[![Build Status](https://travis-ci.org/Tamerz/bandfollow.svg?branch=master)](https://travis-ci.org/Tamerz/bandfollow)

#### Requirements
Create a file to store secrets in the main project folder. Use the below for testing:

`secrets.json`
```json
{
  "secret_key": "xkqv7i-ec^#a$3i@_#5oci$rzyez!&54(7tf&=r_=4pk13f98*",
  "allowed_hosts": [],
  "database_name": "bandfollow",
  "database_user": "bandfollow",
  "database_password": "bandfollow",
  "database_host": "db",
  "database_port": "5432",
  "debug": true
}
```

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


Bootstraps elements borrowed from:

*** https://getbootstrap.com/docs/3.3/examples/carousel/