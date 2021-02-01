.ONESHELL:

.PHONY: clean install tests run all

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

install:
	virtualenv env; \
	. env/bin/activate; \
	pip install -r requirements.txt;

tests:
	. env/bin/activate; \
	python3 manage.py test

run:
	. env/bin/activate; \
	python3 manage.py run

all: clean install tests run