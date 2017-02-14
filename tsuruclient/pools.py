import json

from tsuruclient.base import Manager as Base


class Manager(Base):
    """
    Manage pool resources.
    """

    def rebalance(self, pool):
        """
        Rebalance a pool.
        """
        data = {"metadataFilter": {"pool": pool}}
        return self.request("post", "/docker/containers/rebalance",
                            data=json.dumps(data), stream=True)
