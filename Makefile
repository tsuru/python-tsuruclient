clean:
	@find . -name "*.pyc" -delete

deps:
	@pip install -r requirements.txt

test: deps clean
	@coverage run -m unittest discover
	@coverage report --omit="*/tests/*" --include="./*" -m
	@flake8 .
