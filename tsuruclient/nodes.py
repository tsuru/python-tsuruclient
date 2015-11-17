import json
import requests


class NodeManager(object):
    """
    Manage Node resources.
    """

    def __init__(self, target):
        self.target = target

    def create(self, register=False, **kwargs):
        """
        Create a node.
        """
        register = "true" if register else "false"
        response = requests.post(
            "{}/docker/node?register={}".format(self.target, register),
            data=json.dumps(kwargs)
        )
        return response.json()
