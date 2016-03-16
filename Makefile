.PHONY: docs

all: install migrate run

docs:
	cd docs && make clean && make html

install:
	pip install .
	pip install -e .[docs]
	pip install -e .[test]

migrate:
	python manage.py migrate

run:
	python manage.py runserver 0.0.0.0:8000

test:
	tox -e py27-dj18
	tox -e py27-dj19
	tox -e flake8
