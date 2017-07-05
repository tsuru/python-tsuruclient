from tsuruclient.base import Manager as Base


class Manager(Base):

    def list(self, **kwargs):
        """
        List all users in tsuru. It may also filter users by user email or role name with context value.
        """
        return self.request("get", "/users", params=kwargs)

    def info(self):
        """
        Get info on the current user.
        """
        return self.request("get", "/users/info")
