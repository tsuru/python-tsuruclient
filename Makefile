clean:
	@find . -name "*.pyc" -delete

deps:
	@pip install -r requirements.txt

test: deps clean
	@nosetests -s . && flake8 .
