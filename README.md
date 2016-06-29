# Introduction to Docker

This repo is tied to the presentation given at [CMP Group](http://teamcmp.com)

# Run containers

```
$ docker run -ti --rm alpine:latest /bin/sh
/ # hostname
1ccd4c0df2fb
```

# Delete containers

```bash
$ docker run alpine:latest echo 'true'
true
$ docker ps -a
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                      PORTS               NAMES
5ed58dbc02ad        alpine:latest       "echo true"         48 seconds ago      Exited (0) 47 seconds ago                       lonely_elion
$ docker rm -v lonely_elion
```

# Dockerfile

```bash
$ docker build -t marclop/awesome-term awesome-term
[ .. ]
$ docker run -ti --rm marclop/awesome-term
bash-4.3#
$ docker run -d --name myterm marclop/awesome-term sleep 30
a8fc2362543aaa3f983c562f9094cc26db2be3e244113558a37952e85ffd4f3b
$ docker ps
CONTAINER ID        IMAGE                  COMMAND             CREATED             STATUS              PORTS               NAMES
a8fc2362543a        marclop/awesome-term   "sleep 30"          2 seconds ago       Up 1 seconds                            myterm
```

# Link containers (simple)

```bash
$ docker run -d --name mariadb -e MYSQL_ROOT_PASSWORD=1234 mariadb
bbf7e87848e0de44f59947eefbce06051f3baba7187f2a4cf4e8ec49ec4c5932
$ docker build -t marclop/awesome-mysql-client awesome-mysql-client
[ .. ]
# Run mysql agains the Database typing the password
$ docker run -ti -e USER=root -e HOST=mariadb --link mariadb marclop/awesome-mysql-client
Enter password:
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 2
Server version: 10.1.14-MariaDB-1~jessie mariadb.org binary distribution

Copyright (c) 2000, 2016, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]>

# Connect to MySQL without typing password

$ docker run -ti -e USER=root -e HOST=mariadb -e PASS=1234 --link mariadb marclop/awesome-mysql-client
```


# Using docker-compose to ease life

```bash
$ cd awesome-mysql-client
$ docker-compose -p demo up
```

# Real world scenario

```bash
$ cd awesome-app
$ docker-compose up --build
[ .. ]
$ curl localhost:3000
I said Whale Hello 2 times!
```
