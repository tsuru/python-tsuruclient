from tsuruclient import client

import json
import httpretty
import unittest


class AppsTestCase(unittest.TestCase):
    def setUp(self):
        httpretty.enable()

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_list_apps(self):
        apps_data = []
        url = "http://target/apps"
        httpretty.register_uri(
            httpretty.GET,
            url,
            body=json.dumps(apps_data),
            status=200
        )

        cl = client.Client("http://target", "abc123")
        result = cl.apps.list()

        self.assertListEqual([], result)
        self.assertEqual("bearer abc123", httpretty.last_request().headers["authorization"])

    def test_get_app(self):
        app_data = {}
        url = "http://target/apps/appname"
        httpretty.register_uri(
            httpretty.GET,
            url,
            body=json.dumps(app_data),
            status=200
        )

        cl = client.Client("http://target", "abc123")
        result = cl.apps.get("appname")

        self.assertDictEqual({}, result)
        self.assertEqual("bearer abc123", httpretty.last_request().headers["authorization"])

    def test_remove_app(self):
        url = "http://target/apps/appname"
        httpretty.register_uri(
            httpretty.DELETE,
            url,
            status=200
        )

        cl = client.Client("http://target", "abc123")
        cl.apps.remove("appname")

        self.assertEqual("bearer abc123", httpretty.last_request().headers["authorization"])

    def test_create_app(self):
        app_data = {}
        url = "http://target/apps"
        httpretty.register_uri(
            httpretty.POST,
            url,
            body=json.dumps(app_data),
            status=200
        )

        cl = client.Client("http://target", "abc123")
        data = {
            "name": "appname",
            "framework": "framework",
        }
        cl.apps.create(**data)

        self.assertEqual("bearer abc123", httpretty.last_request().headers["authorization"])
