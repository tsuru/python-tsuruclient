import requests
import json


class Manager(object):
    def __init__(self, target, token):
        self.target = target
        self.token = token

    @property
    def headers(self):
        return {"authorization": "bearer {}".format(self.token)}

    def json_parse(self, response):
        try:
            return response.json()
        except:
            return {}

    def stream_parse(self, response):
        for line in response.iter_lines():
                yield json.loads(line)

    def request(self, method, path, version=None, **kwargs):
        url = self.target
        if version is not None:
            url = "{}/{}".format(url, version)
        url = "{}{}".format(url, path)
        kwargs["headers"] = self.headers
        response = requests.request(method, url, **kwargs)
        response.raise_for_status()

        if "stream" in kwargs:
            return self.stream_parse(response)

        return self.json_parse(response)
