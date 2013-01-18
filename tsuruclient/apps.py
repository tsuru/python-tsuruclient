import requests


class AppManager(object):
    """
    Manage App resources.
    """

    def list(self):
        """
        Get a list of all apps.
        """
        response = requests.get("/apps")
        return response.json
