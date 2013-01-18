from tsuruclient import client

import json
import mock
import unittest


class AppsTestCase(unittest.TestCase):
    @mock.patch("requests.get")
    def test_list_apps(self, get):
        cl = client.Client("target")
        cl.apps.list()
        get.assert_called_with("target/apps")

    @mock.patch("requests.get")
    def test_get_app(self, get):
        cl = client.Client("target")
        cl.apps.get("appname")
        get.assert_called_with("target/apps/appname")

    @mock.patch("requests.delete")
    def test_remove_app(self, delete):
        cl = client.Client("target")
        cl.apps.remove("appname")
        delete.assert_called_with("target/apps/appname")

    @mock.patch("requests.post")
    def test_create_app(self, post):
        cl = client.Client("target")
        data = {
            "name": "appname",
            "framework": "framework",
        }
        cl.apps.create(**data)
        post.assert_called_with("target/apps", data=json.dumps(data))
