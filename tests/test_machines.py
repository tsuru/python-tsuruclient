from tsuruclient import client

import json
import unittest
import httpretty


class MachinesTestCase(unittest.TestCase):

    cl = client.Client("http://target", "abc123")

    def setUp(self):
        httpretty.enable()

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_list(self):
        url = "http://target/iaas/machines"
        data = [{}]
        httpretty.register_uri(
            httpretty.GET,
            url,
            body=json.dumps(data),
            status=200
        )
        self.cl.machines.list()
        self.assertEqual("bearer abc123", httpretty.last_request().headers["authorization"])

    def test_delete(self):
        url = "http://target/iaas/machines/12345"
        httpretty.register_uri(
            httpretty.DELETE,
            url,
            status=200
        )
        self.cl.machines.delete(machine_id=12345)
        self.assertEqual("bearer abc123", httpretty.last_request().headers["authorization"])
