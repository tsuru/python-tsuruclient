
from tsuruclient.base import Manager as Base


class Manager(Base):
    """
    Manage Node resources.
    """

    def create(self, **kwargs):
        """
        Create a node.
        """
        return self.request("post", "/node", version=1.2, stream=True,
                            data=kwargs)

    def list(self):
        """
        List nodes.
        """
        return self.request("get", "/node", version=1.2)

    def remove(self, address, **kwargs):
        """
        Remove a node.
        """
        return self.request("delete", "/node/{}".format(address),
                            version=1.2, params=kwargs)

    def update(self, address, **kwargs):
        """
        Update a node.
        """
        return self.request("put", "/node", version=1.2, data=kwargs)
