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

    def test_remove(self):
        url = "http://target/iaas/templates/mytemplate"
        httpretty.register_uri(
            httpretty.DELETE,
            url,
            status=200
        )

        cl = client.Client("http://target", "token")
        cl.templates.remove("mytemplate")

        self.assertEqual("bearer token", httpretty.last_request().headers["authorization"])

    def test_create(self):
        url = "http://target/iaas/templates"
        httpretty.register_uri(
            httpretty.POST,
            url,
            status=201
        )

        cl = client.Client("http://target", "token")
        cl.templates.create("mytemplate", "myiaas", key="value", another_key="val")

        self.assertEqual("bearer token", httpretty.last_request().headers["authorization"])

        result = httpretty.last_request().body.decode('utf-8')
        expected = "another_key=val&IaaSName=myiaas&Name=mytemplate&key=value"
        self.assertEqual(expected, result)
