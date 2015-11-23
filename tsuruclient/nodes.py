import json
import requests

from base import Manager as Base


class Manager(Base):
    """
    Manage Node resources.
    """

    def create(self, register=False, **kwargs):
        """
        Create a node.
        """
        register = "true" if register is True else "false"
        response = requests.post(
            "{}/docker/node?register={}".format(self.target, register),
            data=json.dumps(kwargs),
            headers=self.headers
        )
        return response.json()
