import requests

from tsuruclient.base import Manager as Base


class Manager(Base):
    """
    Manage Node resources.
    """

    def create(self, **kwargs):
        """
        Create a node.
        """
        response = requests.post(
            "{}/1.2/node".format(self.target),
            data=kwargs,
            headers=self.headers,
            stream=True
        )
        return response

    def list(self):
        """
        List nodes.
        """
        response = requests.get(
            "{}/1.2/node".format(self.target),
            headers=self.headers
        )
        return response.json()

    def remove(self, address, **kwargs):
        """
        Remove a node.
        """
        response = requests.delete(
            "{}/1.2/node/{}".format(self.target, address),
            headers=self.headers,
            params=kwargs
        )
        return response

    def update(self, address, **kwargs):
        """
        Update a node.
        """
        response = requests.put(
            "{}/1.2/node".format(self.target),
            headers=self.headers,
            data=kwargs,
        )
        return response
