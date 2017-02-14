import json

from tsuruclient.base import Manager as Base


class Manager(Base):
    """
    Manage Iaas Template resources.
    """

    def list(self):
        """
        List machine templates
        """
        return self.request("get", "/iaas/templates")

    def remove(self, name):
        """
        Remove machine templates
        """
        return self.request("delete", "/iaas/templates/{}".format(name))

    def create(self, name, iaas, **kwargs):
        """
        Create machine templates
        """
        data = kwargs
        data["iaas"] = iaas
        data["name"] = name
        return self.request("post", "/iaas/templates", data=json.dumps(data))
