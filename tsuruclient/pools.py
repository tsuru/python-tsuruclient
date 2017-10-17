from tsuruclient.base import Manager as Base


class Manager(Base):
    """
    Manage pool resources.
    """

    def rebalance(self, pool):
        """
        Rebalance a pool.
        """
        data = {"MetadataFilter.pool": pool}
        return self.request("post", "/node/rebalance",
                            data=data, stream=True)
