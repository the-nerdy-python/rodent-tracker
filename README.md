# rodent-tracker
Local rodent tracking solution

## Common Commands

# Build the images:

`docker-compose -f docker-compose-dev.yml build`

# Run the containers:

`docker-compose -f docker-compose-dev.yml up -d`

# Create the database:

`docker-compose -f docker-compose-dev.yml run rats python manage.py recreate_db`

# Seed the database:

`docker-compose -f docker-compose-dev.yml run rats python manage.py seed_db`

# Run the tests:

`docker-compose -f docker-compose-dev.yml run rats python manage.py test`
