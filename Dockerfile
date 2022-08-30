version: '3.9'
services:
  web:
    build: .
    command: ./wait-for-it.sh mysql:3306 -- ./docker-entrypoint.sh
    ports:
      - 8000:8000
    depends_on:
      - mysql
    restart: on-failure
    volumes:
      - .:/app
  mysql:
    image: mysql:8.0
    ports:
      - 3306:3306
    restart: always
    environment:
      - MYSQL_DATABASE=infludom
      - MYSQL_ROOT_PASSWORD=Infludom123?
    volumes:
      - mysqldata:/var/lib/mysql     
  tests:
    build: .
    command: ./wait-for-it.sh mysql:3306 -- ptw
    depends_on:
      - mysql
    tty: true
    volumes:
      - .:/app
volumes:
  mysqldata:
