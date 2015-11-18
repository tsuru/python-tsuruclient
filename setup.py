from setuptools import setup, find_packages
from tsuruclient import __version__


with open('requirements.txt') as reqs:
    install_requires = []
    for line in reqs.read().split('\n'):
        if line and not line.startswith("--"):
            install_requires.append(line)


setup(
    name="tsuruclient",
    url="https://github.com/tsuru/python-tsuruclient",
    version=__version__,
    packages=find_packages(),
    description="Python client library for tsuru API",
    author="tsuru",
    author_email="tsuru@corp.globo.com",
    install_requires=install_requires
)
