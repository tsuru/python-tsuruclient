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

    def test_list_apps_by_query_string(self):
        apps_data = []
        url = "http://target/apps"
        httpretty.register_uri(
            httpretty.GET,
            url,
            body=json.dumps(apps_data),
            status=200
        )

        cl = client.Client("http://target", "abc123")
        cl.apps.list(name="appname", pool="testpool")

        self.assertEqual({'name': ['appname'], 'pool': ['testpool']}, httpretty.last_request().querystring)
        self.assertEqual("bearer abc123", httpretty.last_request().headers["authorization"])

    def test_list_apps_handle_no_content(self):
        apps_data = []
        url = "http://target/apps"
        httpretty.register_uri(
            httpretty.GET,
            url,
            body=json.dumps(apps_data),
            status=204
        )

        cl = client.Client("http://target", "abc123")
        response = cl.apps.list()

        self.assertListEqual([], response)
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
            "name": "myapp",
            "platform": "python",
            "pool": "deadpool",
            "tag": ["tag 1", "tag 2"],
        }
        cl.apps.create(**data)

        self.assertEqual("bearer abc123", httpretty.last_request().headers["authorization"])
        self.assertEqual(data["name"], httpretty.last_request().parsed_body["name"][0])
        self.assertEqual(data["platform"], httpretty.last_request().parsed_body["platform"][0])
        self.assertEqual(data["pool"], httpretty.last_request().parsed_body["pool"][0])
        self.assertEqual(data["tag"], httpretty.last_request().parsed_body["tag"])

    def test_update_app(self):
        app_data = {}
        url = "http://target/apps/appname"
        httpretty.register_uri(
            httpretty.PUT,
            url,
            body=json.dumps(app_data),
            status=200
        )

        cl = client.Client("http://target", "abc123")
        data = {
            "pool": "mypool",
            "plan": "myplan",
            "router": "myrouter"
        }
        cl.apps.update("appname", **data)

        self.assertEqual("bearer abc123", httpretty.last_request().headers["authorization"])
        self.assertEqual(data["pool"], httpretty.last_request().parsed_body["pool"][0])
        self.assertEqual(data["plan"], httpretty.last_request().parsed_body["plan"][0])
        self.assertEqual(data["router"], httpretty.last_request().parsed_body["router"][0])
