import requests
import json

from base import Manager as Base


class Manager(Base):
    """
    Manage Iaas Template resources.
    """

    def list(self):
        """
        List machine templates
        """
        response = requests.get("{}/iaas/templates".format(self.target), headers=self.headers)
        return response.json()

    def remove(self, name):
        """
        Remove machine templates
        """
        response = requests.delete(
            "{}/iaas/templates/{}".format(self.target, name),
            headers=self.headers
        )
        return response

    def create(self, name, iaas, **kwargs):
        """
        Create machine templates
        """
        data = kwargs
        data["iaas"] = iaas
        data["name"] = name
        response = requests.post(
            "{}/iaas/templates".format(self.target),
            data=json.dumps(data),
            headers=self.headers
        )
        return response
