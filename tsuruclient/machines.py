import requests

from tsuruclient.base import Manager as Base


class Manager(Base):
    """
    Manage IaaS Machines.
    """

    def list(self):
        """
        List IaaS machines.
        """
        response = requests.get(
            "{}/iaas/machines".format(self.target),
            headers=self.headers
        )
        return response.json()

    def delete(self, machine_id):
        """
        Delete IaaS machine.
        """
        response = requests.delete(
            "{}/iaas/machines/{}".format(self.target, machine_id),
            headers=self.headers
        )
        return response
