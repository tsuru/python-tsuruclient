
from tsuruclient.base import Manager as Base


class Manager(Base):
    """
    Manage Events resources.
    """

    def list(self, **kwargs):
        """
        List events.
        """
        return self.request("get", "/events", version=1.1, params=kwargs)

    def list_kinds(self):
        """
        List event kinds.
        """
        return self.request("get", "/events/kinds", version=1.1)

    def get(self, id):
        """
        Get event info.
        """
        return self.request("get", "/events/{}".format(id), version=1.1)

    def cancel(self, id):
        """
        Cancel event.
        """
        return self.request("post", "/events/{}/cancel".format(id), version=1.1)
