import requests


class Manager(object):
    def __init__(self, target, token):
        self.target = target
        self.token = token

    @property
    def headers(self):
        return {"authorization": "bearer {}".format(self.token)}

    def request(self, method, path, version=None, **kwargs):
        url = self.target
        if version is not None:
            url = "{}/{}".format(url, version)
        url = "{}{}".format(url, path)
        kwargs["headers"] = self.headers
        response = requests.request(method, url, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except:
            return {}
