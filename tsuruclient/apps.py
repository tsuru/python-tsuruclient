import json
import requests

from base import Manager as Base


class Manager(Base):
    """
    Manage App resources.
    """

    def list(self):
        """
        Get a list of all apps.
        """
        response = requests.get("{}/apps".format(self.target), headers=self.headers)
        return response.json()

    def get(self, appname):
        """
        Get an app.
        """
        response = requests.get("{}/apps/{}".format(self.target, appname), headers=self.headers)
        return response.json()

    def remove(self, appname):
        """
        Remove an app.
        """
        response = requests.delete("{}/apps/{}".format(self.target, appname), headers=self.headers)
        return response.text

    def create(self, name, framework):
        """
        Create an app.
        """
        data = {
            "name": name,
            "framework": framework,
        }
        response = requests.post(
            "{}/apps".format(self.target),
            data=json.dumps(data),
            headers=self.headers
        )
        return response.json()
