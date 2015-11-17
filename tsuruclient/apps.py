import json
import requests


class Manager(object):
    """
    Manage App resources.
    """

    def __init__(self, target):
        self.target = target

    def list(self):
        """
        Get a list of all apps.
        """
        response = requests.get("{0}/apps".format(self.target))
        return response.json

    def get(self, appname):
        """
        Get an app.
        """
        response = requests.get("{0}/apps/{1}".format(self.target, appname))
        return response.json

    def remove(self, appname):
        """
        Remove an app.
        """
        response = requests.delete("{0}/apps/{1}".format(self.target, appname))
        return response.json

    def create(self, name, framework):
        """
        Create an app.
        """
        data = {
            "name": name,
            "framework": framework,
        }
        response = requests.post(
            "{0}/apps".format(self.target),
            data=json.dumps(data)
        )
        return response.json
