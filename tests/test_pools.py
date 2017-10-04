from tsuruclient import client

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
            body="",
            status=200
        )

        cl = client.Client("http://target", "abc123")
        cl.pools.rebalance("dev")

        result = httpretty.last_request().body.decode('utf-8')
        expected = "MetadataFilter.pool=dev"
        self.assertEqual(expected, result)
