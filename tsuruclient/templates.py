import requests


class Manager(object):
    """
    Manage Iaas Template resources.
    """

    def __init__(self, target):
        self.target = target

    def list(self):
        """
        List machine templates
        """
        response = requests.get("{}/iaas/templates".format(self.target))
        return response.json()
