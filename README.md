python-tsuruclient
==================

[![Build Status](https://travis-ci.org/tsuru/python-tsuruclient.svg?branch=master)](https://travis-ci.org/tsuru/python-tsuruclient)

Python client library for tsuru API http://tsuru.io

# Install

```bash
$ pip install tsuruclient
```

# Contribute

## install the dependencies

```bash
$ pip install -r test-requirements.txt
```

## run the tests

```bash
make test
```

## commit, push etc
## send a pull request

# Publishing a new version

Create a `$HOME/.pypirc` file with the following contents:

```
[server-login]
repository: https://upload.pypi.org/legacy/
username: <pypi username>
password: <pypi pasword>
```

Update `./tsuruclient/__init__.py` file with the new version and run `make dist`
