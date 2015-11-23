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

        data = {"address": "127.0.0.3:4243", "pool": "tsuru2"}
        result = cl.nodes.create(**data)

        self.assertDictEqual(result, node_data)
        self.assertEqual("bearer abc123", httpretty.last_request().headers["authorization"])
        self.assertEqual("false", httpretty.last_request().querystring["register"][0])

        result = cl.nodes.create(register=False, **data)

        self.assertDictEqual(result, node_data)
        self.assertEqual("bearer abc123", httpretty.last_request().headers["authorization"])
        self.assertEqual("false", httpretty.last_request().querystring["register"][0])

        result = cl.nodes.create(register=True, **data)

        self.assertDictEqual(result, node_data)
        self.assertEqual("bearer abc123", httpretty.last_request().headers["authorization"])
        self.assertEqual("true", httpretty.last_request().querystring["register"][0])

        result = cl.nodes.create(register="invalid", **data)

        self.assertDictEqual(result, node_data)
        self.assertEqual("bearer abc123", httpretty.last_request().headers["authorization"])
        self.assertEqual("false", httpretty.last_request().querystring["register"][0])
