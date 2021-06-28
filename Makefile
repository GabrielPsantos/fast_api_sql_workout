.PHONY = makefile that help you make stuff without headache

up-first: build
	docker-compose up --b

up: build
	docker-compose up --d

clean-volumes:
	docker volume prune -f

keep-eye-on:
	docker attach fast_api_sql_workout_fast-api-application_1

go-inside:
	docker exec -it fast_api_sql_workout_fast-api-application_1 /bin/sh

restart: 
	make down
	make clean-volumes
	make up-first

down:
	docker-compose down

build:
	docker-compose build

migrate:
	docker exec -it fast_api_sql_workout_fast-api-application_1 python migrate.py

migrate-test:
	python ./app/migrate.py

install-test:
	python -m venv ./app/.venv
	pip install -r ./app/requirements.txt

run-test:
	coverage run --source=./app/ --omit=./app/.venv -m pytest 
	
test: install-test run-test

coverage: test
	coverage report -m --fail-under=86

coverage-html: coverage
	coverage html


help:
	@echo "---------------HELP-----------------"
	@echo "To run the project type run-local"
	@echo "To test the project type make test"
	@echo "To stop the project type make down"
	@echo "To run the migrations type make migrate"
	@echo "------------------------------------"
