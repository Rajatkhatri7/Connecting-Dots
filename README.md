# Connecting-Dots


## Steps to start

## Option 1

* Install and start the mongoDB service on your computer

[Click here for MongoDB installation documentation](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/)

**Command to start the service locally: ** `sudo systemctl start mongod`
**Command to check the service is running or not: ** `sudo systemctl status mongod`


* Run the Django server

** Command: ** `python manage.py runserver`

## Option 2

* use docker-conpose file to run the database locally.

* Navigate to the directory where **docker-compose.yaml** file is present.

**command to start the DB service: ** `docker-compose up`

* Open the browser and go to address `localhost:8081` (at port 8081 mongo-express is running)
