from tsuruclient.base import Manager as Base


class Manager(Base):

    def info(self):
        """
        Get info on the current user.
        """
        return self.request("get", "/users/info")
