from tsuruclient import client

import json
import httpretty
import unittest


class PlansTestCase(unittest.TestCase):
    def setUp(self):
        httpretty.enable()

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_list_plans(self):
        plans_data = []
        url = "http://target/plans"
        httpretty.register_uri(
            httpretty.GET,
            url,
            body=json.dumps(plans_data),
            status=200
        )

        cl = client.Client("http://target", "abc123")
        result = cl.plans.list()

        self.assertListEqual([], result)
        self.assertEqual("bearer abc123", httpretty.last_request().headers["authorization"])

    def test_list_plans_handle_no_content(self):
        plans_data = []
        url = "http://target/plans"
        httpretty.register_uri(
            httpretty.GET,
            url,
            body=json.dumps(plans_data),
            status=204
        )

        cl = client.Client("http://target", "abc123")
        response = cl.plans.list()

        self.assertListEqual([], response)
        self.assertEqual("bearer abc123", httpretty.last_request().headers["authorization"])

    def test_remove_plan(self):
        url = "http://target/plans/planname"
        httpretty.register_uri(
            httpretty.DELETE,
            url,
            status=200
        )

        cl = client.Client("http://target", "abc123")
        cl.plans.remove("planname")

        self.assertEqual("bearer abc123", httpretty.last_request().headers["authorization"])

    def test_create_plan(self):
        plan_data = {}
        url = "http://target/plans"
        httpretty.register_uri(
            httpretty.POST,
            url,
            body=json.dumps(plan_data),
            status=200
        )

        cl = client.Client("http://target", "abc123")
        data = {
            "name": "myplan",
            "memory": "123",
            "swap": "456",
            "cpu": "789",
            "router": "myrouter"
        }
        cl.plans.create(**data)

        self.assertEqual("bearer abc123", httpretty.last_request().headers["authorization"])
        self.assertEqual(data["name"], httpretty.last_request().parsed_body["name"][0])
        self.assertEqual(data["memory"], httpretty.last_request().parsed_body["memory"][0])
        self.assertEqual(data["swap"], httpretty.last_request().parsed_body["swap"][0])
        self.assertEqual(data["cpu"], httpretty.last_request().parsed_body["cpu"][0])
        self.assertEqual(data["router"], httpretty.last_request().parsed_body["router"][0])
