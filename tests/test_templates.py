from tsuruclient import client

import json
import unittest
import httpretty


class TemplatesTestCase(unittest.TestCase):
    def setUp(self):
        httpretty.enable()

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_list(self):
        template_data = []
        url = "http://target/iaas/templates"
        httpretty.register_uri(
            httpretty.GET,
            url,
            body=json.dumps(template_data),
            status=200
        )

        cl = client.Client("http://target", "token")
        result = cl.templates.list()

        self.assertListEqual(result, template_data)
        self.assertEqual("bearer token", httpretty.last_request().headers["authorization"])
