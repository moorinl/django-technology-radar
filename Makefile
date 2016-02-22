.PHONY: docs

all: install migrate loaddata run

docs:
	cd docs && make clean && make html

install:
	pip install .
	pip install -e .[docs]
	pip install -e .[test]

loaddata:
	python manage.py loaddata radar

migrate:
	python manage.py migrate

run:
	python manage.py runserver 0.0.0.0:8000

test:
	tox -e py27-dj18
	tox -e py27-dj19
	tox -e flake8
