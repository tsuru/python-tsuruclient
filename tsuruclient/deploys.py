from tsuruclient.base import Manager as Base


class Manager(Base):
    """
    Manager deploys (despite that name, it only shows deploy's info).
    """
    def list(self, deploy_id=None, **kwargs):
        """
        Display deploy information. When the deploy_id argument is assigned,
        show only info about that deploy (if any).
        """
        if deploy_id is not None:
            return self.request("get", "/deploys/{}".format(deploy_id))

        def handler(response):
            return [] if response.status_code == 204 else response.json()

        return self.request("get", "/deploys", params=kwargs, handle_response=handler)
