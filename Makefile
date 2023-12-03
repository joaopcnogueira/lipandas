all: source upload

source:
	# create source distribution
	python setup.py sdist

upload:
	# upload to PyPI
	twine upload dist/*

build:
	# install locally
	pip install -e .