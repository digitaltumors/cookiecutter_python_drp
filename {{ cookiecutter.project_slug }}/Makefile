.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help

# 1. Find all source files in the platform directory
MD_SOURCES := $(wildcard platforms/dnanexus/{{cookiecutter.project_slug}}/*.md)
SH_SOURCES := $(wildcard platforms/dnanexus/{{cookiecutter.project_slug}}/src/*.sh)
PY_SOURCES := $(wildcard platforms/dnanexus/{{cookiecutter.project_slug}}/test/*.py)

# 2. Convert source paths to build paths
MD_TARGETS := $(patsubst platforms/dnanexus/{{cookiecutter.project_slug}}/%.md, build/{{cookiecutter.project_slug}}/%.md, $(MD_SOURCES))
SH_TARGETS := $(patsubst platforms/dnanexus/{{cookiecutter.project_slug}}/src/%.sh, build/{{cookiecutter.project_slug}}/src/%.sh, $(SH_SOURCES))
PY_TARGETS := $(patsubst platforms/dnanexus/{{cookiecutter.project_slug}}/test/%.py, build/{{cookiecutter.project_slug}}/test/%.py, $(PY_SOURCES))

# Python files
PY_DEPS := $(wildcard {{cookiecutter.project_slug}}/*.py) setup.py requirements.txt pyproject.toml


define BROWSER_PYSCRIPT
import os, webbrowser, sys

try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

lint: ## check style with flake8
	flake8 {{ cookiecutter.project_slug }} tests

test: ## run tests quickly with the default Python
	pytest

test-all: ## run tests on every Python version with tox
	tox

coverage: ## check code coverage quickly with the default Python
	coverage run --source {{ cookiecutter.project_slug }} -m unittest discover
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

docs: ## generate Sphinx HTML documentation, including API docs
	sphinx-apidoc -o docs/ {{ cookiecutter.project_slug }}
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

testrelease: dist ## package and upload a TEST release
	twine check dist/*
	twine upload dist/* -r testpypi

release: dist ## package and upload a release
	twine check dist/*
	twine upload dist/*

dist: clean ## builds source and wheel package
	python -m build
	ls -l dist

install: clean ## install the package to the active Python's site-packages
	python -m pip install .

dockerbuild: ## build docker image and store in local repository
	@cv=`grep '__version__' {{cookiecutter.project_slug}}/__init__.py | sed "s/^.*= *'//" | sed "s/'.*//"`; \
	docker build -t {{cookiecutter.docker_owner}}/{{cookiecutter.project_slug}}:$$cv -f docker/Dockerfile .

dockerpush: ## push image to dockerhub
	@cv=`grep '__version__' {{cookiecutter.project_slug}}/__init__.py | sed "s/^.*= *'//" | sed "s/'.*//"`; \
	docker push {{cookiecutter.docker_owner}}/{{cookiecutter.project_slug}}:$$cv

build/{{cookiecutter.project_slug}}/py.changed: $(PY_DEPS) ## Touches a file to trigger rebuild
	@mkdir -p `dirname $@`
	@touch $@

build/{{cookiecutter.project_slug}}/resources/{{cookiecutter.project_slug}}.tar.gz: build/{{cookiecutter.project_slug}}/py.changed ## Builds {{cookiecutter.project_slug}} Docker Container file
	@mkdir -p `dirname $@`
	@cv=`grep '__version__' {{cookiecutter.project_slug}}/__init__.py | sed "s/^.*= *'//" | sed "s/'.*//"`; \
	docker build -t {{cookiecutter.docker_owner}}/{{cookiecutter.project_slug}}:$$cv -f docker/Dockerfile .; \
	docker save {{cookiecutter.docker_owner}}/{{cookiecutter.project_slug}}:$$cv -o $@

build/{{cookiecutter.project_slug}}/dxapp.json: platforms/dnanexus/{{cookiecutter.project_slug}}/dxapp.json ## Builds dxapp.json with version
	@mkdir -p `dirname $@`
	@cv=`grep '__version__' {{cookiecutter.project_slug}}/__init__.py | sed "s/^.*= *'//" | sed "s/'.*//"`; \
	cat $< | sed "s/@@VERSION@@/$$cv/g" > $@

build/{{cookiecutter.project_slug}}/test/%.py: platforms/dnanexus/{{cookiecutter.project_slug}}/test/%.py ## Builds test files with version
	@mkdir -p `dirname $@`
	@cp $< $@

build/{{cookiecutter.project_slug}}/%.md: platforms/dnanexus/{{cookiecutter.project_slug}}/%.md ## Builds markdown files
	@mkdir -p `dirname $@`
	@cp $< $@

applet: build/{{cookiecutter.project_slug}}/resources/{{cookiecutter.project_slug}}.tar.gz \
        build/{{cookiecutter.project_slug}}/dxapp.json \
		$(MD_TARGETS) $(SH_TARGETS) $(PY_TARGETS) ## Builds the DNAnexus applet

dockerpush: ## push image to dockerhub
	@cv=`grep '__version__' {{cookiecutter.project_slug}}/__init__.py | sed "s/^.*= *'//" | sed "s/'.*//"`; \
	docker push {{cookiecutter.docker_owner}}/{{cookiecutter.project_slug}}:$$cv
