from tsuruclient.base import Manager as Base


class Manager(Base):
    """
    Manage Plans.
    """

    def list(self, **kwargs):
        """
        Get a list of plans by query string.
        """
        def handle(response):
            if response.status_code == 204:
                return []
            return response.json()
        return self.request("get", "/plans", handle_response=handle, params=kwargs)

    def remove(self, planname):
        """
        Remove a plan.
        """
        return self.request("delete", "/plans/{}".format(planname))

    def create(self, **kwargs):
        """
        Create a plan.
        """
        return self.request("post", "/plans", stream=True, data=kwargs)
