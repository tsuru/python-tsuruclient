import json
import requests

from base import Manager as Base


class Manager(Base):
    """
    Manage pool resources.
    """

    def rebalance(self, pool):
        """
        Rebalance a pool.
        """
        data = {"metadataFilter": {"pool": pool}}
        response = requests.post(
            "{}/docker/containers/rebalance".format(self.target),
            data=json.dumps(data),
            headers=self.headers,
            stream=True
        )
        return response
