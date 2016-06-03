import requests

from base import Manager as Base


class Manager(Base):
    """
    Manage Node resources.
    """

    def create(self, **kwargs):
        """
        Create a node.
        """
        response = requests.post(
            "{}/docker/node".format(self.target),
            data=kwargs,
            headers=self.headers,
            stream=True
        )
        return response
