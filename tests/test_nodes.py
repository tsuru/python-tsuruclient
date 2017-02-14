from tsuruclient import client

import json
import unittest
import httpretty


class NodesTestCase(unittest.TestCase):

    cl = client.Client("http://target", "abc123")

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
        url = "http://target/1.2/node"
        httpretty.register_uri(
            httpretty.POST,
            url,
            body=json.dumps(node_data),
            status=200
        )

        data = {"address": "127.0.0.3:4243", "pool": "tsuru2", "register": "false"}
        result = self.cl.nodes.create(**data)

        self.assertDictEqual(result, node_data)
        self.assertEqual("bearer abc123", httpretty.last_request().headers["authorization"])
        self.assertIn("register", httpretty.last_request().body.decode('utf-8'))
        self.assertIn("false", httpretty.last_request().body.decode('utf-8'))

        result = self.cl.nodes.create(**data)

        self.assertDictEqual(result, node_data)
        self.assertEqual("bearer abc123", httpretty.last_request().headers["authorization"])
        self.assertIn("register", httpretty.last_request().body.decode('utf-8'))
        self.assertIn("false", httpretty.last_request().body.decode('utf-8'))

        data = {"address": "127.0.0.3:4243", "pool": "tsuru2", "register": "true"}
        result = self.cl.nodes.create(**data)

        self.assertDictEqual(result, node_data)
        self.assertEqual("bearer abc123", httpretty.last_request().headers["authorization"])
        self.assertIn("register", httpretty.last_request().body.decode('utf-8'))
        self.assertIn("true", httpretty.last_request().body.decode('utf-8'))

        data = {"address": "127.0.0.3:4243", "pool": "tsuru2", "register": "invalid"}
        result = self.cl.nodes.create(**data)

        self.assertDictEqual(result, node_data)
        self.assertEqual("bearer abc123", httpretty.last_request().headers["authorization"])
        self.assertIn("register", httpretty.last_request().body.decode('utf-8'))
        self.assertIn("invalid", httpretty.last_request().body.decode('utf-8'))

    def test_list(self):
        data = {
            "nodes": [
                {
                    "Status": "ready",
                    "Metadata": {
                        "pool": "tsuru2",
                        "iaas": "ec2",
                        "LastSuccess": "2015-11-16T18:44:36-02:00",
                    },
                    "Address": "http://127.0.0.3:4243"
                }
            ]
        }
        url = "http://target/1.2/node"
        httpretty.register_uri(
            httpretty.GET,
            url,
            body=json.dumps(data),
            status=200
        )

        result = self.cl.nodes.list()
        self.assertDictEqual(result, data)
        self.assertEqual("bearer abc123", httpretty.last_request().headers["authorization"])

    def test_remove(self):
        url = "http://target/1.2/node/127.0.0.1:4243"
        httpretty.register_uri(
            httpretty.DELETE,
            url,
            status=200
        )

        data = {"no-rebalance": "true"}
        self.cl.nodes.remove(address="127.0.0.1:4243", **data)
        self.assertEqual("bearer abc123", httpretty.last_request().headers["authorization"])

    def test_update(self):
        url = "http://target/1.2/node"
        httpretty.register_uri(
            httpretty.PUT,
            url,
            status=200
        )

        data = {"enable": "true"}
        self.cl.nodes.update(address="127.0.0.1:4243", **data)
        self.assertEqual("bearer abc123", httpretty.last_request().headers["authorization"])
