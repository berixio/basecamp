SHELL := /bin/bash

init:
	virtualenv --distribute --no-site-packages .
requirements:
	pip install -r requirements.txt
register:
	python setup.py register
publish:
	python setup.py sdist bdist_egg upload 
