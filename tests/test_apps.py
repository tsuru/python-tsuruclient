from tsuruclient import client

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
