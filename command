#! /bin/bash

APP="blog-app"
RUN_APP="docker-compose run --rm ${APP}"
BUILD_APP="docker-compose build"
MIGRATE="${RUN_APP} ./manage.py migrate"
UP_APP="docker-compose up -d"
DOWN_APP="docker-compose down"

case "$1" in
  "init")
    if [ ! -e '.env' ]; then
      cp .env.sample .env
    fi
    docker-compose down -v
    docker volume rm blog-pgdate | true
    docker volume rm blog-static | true
    docker volume rm blog-media | true
    $BUILD_APP
    $MIGRATE
    ;;
  
  "up")
    $BUILD_APP
    $MIGRATE
    $UP_APP
    ;;

  "down")
    $DOWN_APP
    ;;

  "restart")
    $DOWN_APP
    $BUILD_APP
    $MIGRATE
    $UP_APP
    ;;

  "createsuperuser")
    $RUN_APP ./manage.py createsuperuser
    ;;

  "makemigrations")
    $RUN_APP ./manage.py makemigrations
    ;;

  "migrate")
    $MIGRATE
    ;;

  "initdb")
    docker-compose rm -s -f -v blog-postgres
    docker volume rm blog-pgdata | true
    $MIGRATE
    ;;

  "login")
    docker exec -it $APP /bin/sh
    ;;

  "postgres")
    docker-compose exec blog-postgres psql -U postgres
    ;;

  "flake8")
    $RUN_APP flake8
    ;;

  "test")
    $RUN_APP ./manage.py test
    ;;
esac