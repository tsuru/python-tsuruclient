from tsuruclient import client

import json
import unittest
import httpretty


class ContainersTestCase(unittest.TestCase):
    def setUp(self):
        httpretty.enable()

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_move(self):
        url = "http://target/docker/containers/move"
        httpretty.register_uri(
            httpretty.POST,
            url,
            body=json.dumps("{}"),
            status=200,
            content_type='application/x-json-stream'
        )

        cl = client.Client("http://target", "abc123")
        cl.containers.move("node1", "node2")

        request = httpretty.last_request()
        expected = {"from": ["node1"], "to": ["node2"]}
        self.assertDictEqual(expected, request.querystring)
