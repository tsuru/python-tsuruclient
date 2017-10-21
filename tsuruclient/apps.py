from tsuruclient.base import Manager as Base


class Manager(Base):
    """
    Manage App resources.
    """

    def list(self, **kwargs):
        """
        Get a list of apps by query string.
        """
        def handle(response):
            if response.status_code == 204:
                return []
            return response.json()
        return self.request("get", "/apps", handle_response=handle, params=kwargs)

    def get(self, appname):
        """
        Get an app.
        """
        return self.request("get", "/apps/{}".format(appname))

    def remove(self, appname):
        """
        Remove an app.
        """
        return self.request("delete", "/apps/{}".format(appname))

    def create(self, **kwargs):
        """
        Create an app.
        """
        return self.request("post", "/apps", stream=True, data=kwargs)

    def update(self, appname, **kwargs):
        """
        Update an app.
        """
        return self.request("put", "/apps/{}".format(appname), stream=True, data=kwargs)

    def restart(self, appname, **kwargs):
        """
        Restart an app.
        """
        return self.request("post", "/apps/{}/restart".format(appname), stream=True, data=kwargs)
