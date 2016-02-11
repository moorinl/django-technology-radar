all: install migrate run

install:
	pip install -e .[test]

migrate:
	python manage.py migrate

run:
	python manage.py runserver 0.0.0.0:8000

test:
	tox -e py27,flake8
