all: install migrate loaddata run

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
	tox -e py27,flake8
