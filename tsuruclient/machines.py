
from tsuruclient.base import Manager as Base


class Manager(Base):
    """
    Manage IaaS Machines.
    """

    def list(self):
        """
        List IaaS machines.
        """
        return self.request("get", "/iaas/machines")

    def delete(self, machine_id):
        """
        Delete IaaS machine.
        """
        return self.request("delete", "/iaas/machines/{}".format(machine_id))
