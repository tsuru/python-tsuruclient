from tsuruclient import client

import json
import unittest
import httpretty


class NodesTestCase(unittest.TestCase):
    def setUp(self):
        httpretty.enable()

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_create_node(self):
        node_data = {
            "Status": "ready",
            "Metadata": {
                "pool": "tsuru2",
                "iaas": "ec2",
                "LastSuccess": "2015-11-16T18:44:36-02:00",
            },
            "Address": "http://127.0.0.3:4243"
        }
        url = "http://target/docker/node"
        httpretty.register_uri(
            httpretty.POST,
            url,
            body=json.dumps(node_data),
            status=200
        )

        cl = client.Client("http://target", "abc123")

        data = {"address": "127.0.0.3:4243", "pool": "tsuru2", "register": "false"}
        result = cl.nodes.create(**data)

        self.assertDictEqual(result.json(), node_data)
        self.assertEqual("bearer abc123", httpretty.last_request().headers["authorization"])
        self.assertIn("register", httpretty.last_request().body)
        self.assertIn("false", httpretty.last_request().body)

        result = cl.nodes.create(**data)

        self.assertDictEqual(result.json(), node_data)
        self.assertEqual("bearer abc123", httpretty.last_request().headers["authorization"])
        self.assertIn("register", httpretty.last_request().body)
        self.assertIn("false", httpretty.last_request().body)

        data = {"address": "127.0.0.3:4243", "pool": "tsuru2", "register": "true"}
        result = cl.nodes.create(**data)

        self.assertDictEqual(result.json(), node_data)
        self.assertEqual("bearer abc123", httpretty.last_request().headers["authorization"])
        self.assertIn("register", httpretty.last_request().body)
        self.assertIn("true", httpretty.last_request().body)

        data = {"address": "127.0.0.3:4243", "pool": "tsuru2", "register": "invalid"}
        result = cl.nodes.create(**data)

        self.assertDictEqual(result.json(), node_data)
        self.assertEqual("bearer abc123", httpretty.last_request().headers["authorization"])
        self.assertIn("register", httpretty.last_request().body)
        self.assertIn("invalid", httpretty.last_request().body)
