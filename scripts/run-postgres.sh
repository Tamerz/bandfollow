#!/bin/sh

docker run -d -p 5432:5432 --name bandfollow-db -e POSTGRES_PASSWORD=postgres postgres:10.5
