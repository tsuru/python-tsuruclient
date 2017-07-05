from tsuruclient import client

import json
import unittest
import httpretty


class UsersTestCase(unittest.TestCase):
    def setUp(self):
        httpretty.enable()

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_list(self):
        data = []
        url = "http://target/users"

        httpretty.register_uri(
            httpretty.GET,
            url,
            body=json.dumps(data),
            status=200
        )

        cl = client.Client("http://target", "token")
        result = cl.users.list()

        self.assertListEqual(result, data)
        self.assertEqual("bearer token", httpretty.last_request().headers["authorization"])

    def test_info(self):
        data = {}
        url = "http://target/users/info"
        httpretty.register_uri(
            httpretty.GET,
            url,
            body=json.dumps(data),
            status=200
        )

        cl = client.Client("http://target", "token")
        result = cl.users.info()

        self.assertDictEqual(result, data)
        self.assertEqual("bearer token", httpretty.last_request().headers["authorization"])
