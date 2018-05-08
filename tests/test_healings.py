from tsuruclient import client

import json
import unittest
import httpretty


class HealingsTestCase(unittest.TestCase):

    cl = client.Client("http://target", "abc123")

    def setUp(self):
        httpretty.enable()

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_list(self):
        url = "http://target/1.2/healing/node"
        data = [{}]
        httpretty.register_uri(
            httpretty.GET,
            url,
            body=json.dumps(data),
            status=200
        )
        self.cl.healings.list()
        self.assertEqual("bearer abc123", httpretty.last_request().headers["authorization"])

    def test_remove(self):
        url = "http://target/1.2/healing/node"
        httpretty.register_uri(
            httpretty.DELETE,
            url,
            status=200
        )
        self.cl.healings.remove(pool="abc")
        self.assertEqual("bearer abc123", httpretty.last_request().headers["authorization"])

    def test_update(self):
        url = "http://target/1.2/healing/node"
        httpretty.register_uri(
            httpretty.POST,
            url,
            status=200,
            forcing_headers={'X-Empty': 'True'}
        )
        self.cl.healings.update(**{"pool": "abc"})
        self.assertEqual("bearer abc123", httpretty.last_request().headers["authorization"])
