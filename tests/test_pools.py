from tsuruclient import client

import json
import unittest
import httpretty


class PoolsTestCase(unittest.TestCase):
    def setUp(self):
        httpretty.enable()

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_rebalance(self):
        url = "http://target/docker/containers/rebalance"
        httpretty.register_uri(
            httpretty.POST,
            url,
            body=json.dumps("{}"),
            status=200
        )

        cl = client.Client("http://target", "abc123")
        cl.pools.rebalance("dev")

        result = json.loads(httpretty.last_request().body)
        expected = {"metadataFilter": {"pool": "dev"}}
        self.assertDictEqual(expected, result)
