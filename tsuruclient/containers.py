
from tsuruclient.base import Manager as Base


class Manager(Base):
    """
    Manage Containers resources.
    """

    def move(self, src, dst):
        """
        Move containers.
        """
        data = {"from": src, "to": dst}
        return self.request("post", "/docker/containers/move", params=data,
                            stream=True)
