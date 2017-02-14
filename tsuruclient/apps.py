import json

from tsuruclient.base import Manager as Base


class Manager(Base):
    """
    Manage App resources.
    """

    def list(self):
        """
        Get a list of all apps.
        """
        return self.request("get", "/apps")

    def get(self, appname):
        """
        Get an app.
        """
        return self.request("get", "/apps/{}".format(appname))

    def remove(self, appname):
        """
        Remove an app.
        """
        return self.request("delete", "/apps/{}".format(appname))

    def create(self, name, framework):
        """
        Create an app.
        """
        data = {
            "name": name,
            "framework": framework,
        }
        return self.request("post", "/apps", data=json.dumps(data))
