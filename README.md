# rodent-tracker
Local rodent tracking solution

[![Build Status](https://travis-ci.com/the-nerdy-python/rodent-tracker.svg?branch=master)]

## Common Commands

### Build the images:

`docker-compose -f docker-compose-dev.yml build`

### Run the containers:

`docker-compose -f docker-compose-dev.yml up -d`

### Create the database:

`docker-compose -f docker-compose-dev.yml run rats python manage.py recreate_db`

### Seed the database:

`docker-compose -f docker-compose-dev.yml run rats python manage.py seed_db`

### Run the tests:

`docker-compose -f docker-compose-dev.yml run rats python manage.py test`
