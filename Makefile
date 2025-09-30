up:
	docker compose up -d

stop:
	docker compose stop

build:
	docker compose down
	docker compose up -d --build

migrate:
	docker compose exec web sh -c 'python manage.py migrate'

pgsql:
	docker compose exec pgsql bash -c 'psql -U ${DB_USER} -d ${DB_NAME}'

shell:
	docker compose exec web bash

down:
	docker compose down

# seed:
# 	docker compose exec web sh -c 'python manage.py seed'
