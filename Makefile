clean:
	@find . -name "*.pyc" -delete

deps:
	@pip install -r test-requirements.txt

test: deps clean
	@coverage run -m unittest discover
	@coverage report --omit="*/tests/*" --include="./*" -m
	@flake8 --max-line-length 110 .
