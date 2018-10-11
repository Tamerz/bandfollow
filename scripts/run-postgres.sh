#!/bin/sh

docker run -d -p 5432:5432 --name bandfollow-db -e POSTGRES_USER=bandfollow -e POSTGRES_PASSWORD=bandfollow postgres:10.5
