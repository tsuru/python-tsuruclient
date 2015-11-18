from tsuruclient import client

import json
import mock
import unittest


class AppsTestCase(unittest.TestCase):
    def setUp(self):
        self.headers = {"authorization": "bearer abc123"}

    @mock.patch("requests.get")
    def test_list_apps(self, get):
        cl = client.Client("target", "abc123")
        cl.apps.list()
        get.assert_called_with("target/apps", headers=self.headers)

    @mock.patch("requests.get")
    def test_get_app(self, get):
        cl = client.Client("target", "abc123")
        cl.apps.get("appname")
        get.assert_called_with("target/apps/appname", headers=self.headers)

    @mock.patch("requests.delete")
    def test_remove_app(self, delete):
        cl = client.Client("target", "abc123")
        cl.apps.remove("appname")
        delete.assert_called_with("target/apps/appname", headers=self.headers)

    @mock.patch("requests.post")
    def test_create_app(self, post):
        cl = client.Client("target", "abc123")
        data = {
            "name": "appname",
            "framework": "framework",
        }
        cl.apps.create(**data)
        post.assert_called_with("target/apps", data=json.dumps(data), headers=self.headers)
