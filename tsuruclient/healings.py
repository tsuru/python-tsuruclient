
from tsuruclient.base import Manager as Base


class Manager(Base):

    def update(self, **kwargs):
        """
        Update a healing.
        """
        return self.request("post", "/healing/node", version=1.2, data=kwargs)

    def remove(self, pool):
        """
        Delete an healing.
        """
        return self.request("delete", "/healing/node?pool={}".format(pool),
                            version=1.2)

    def list(self):
        """
        List healings.
        """
        return self.request("get", "/healing/node", version=1.2)
