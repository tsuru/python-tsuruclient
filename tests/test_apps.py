from tsuruclient import client

import mock
import unittest


class AppsTestCase(unittest.TestCase):
    @mock.patch("requests.get")
    def test_list_apps(self, get):
        cl = client.Client()
        cl.apps.list()
        get.assert_called_with("/apps")
