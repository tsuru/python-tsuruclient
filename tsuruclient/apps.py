import requests


class AppManager(object):
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
