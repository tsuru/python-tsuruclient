from setuptools import setup, find_packages
from tsuruclient import __version__


with open('requirements.txt') as reqs:
    install_requires = []
    for line in reqs.read().split('\n'):
        if line and not line.startswith("--"):
            install_requires.append(line)


setup(
    name="python-tsuruclient",
    url="https://github.com/tsuru/python-tsuruclient",
    version=__version__,
    packages=find_packages(),
    description="Python bindings to tsuru REST API",
    author="timeredbull",
    author_email="timeredbull@corp.globo.com",
    install_requires=install_requires
)
