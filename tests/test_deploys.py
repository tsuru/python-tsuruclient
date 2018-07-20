from tsuruclient import client

import json
import unittest
import httpretty


class DeploysTestCase(unittest.TestCase):
    def setUp(self):
        httpretty.enable()

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_deploys_list(self):
        all_deploys = [
            {
                "ID": "1",
                "App": "just-another-app",
                "Image": "v1"
            },
            {
                "ID": "2",
                "App": "critical-app",
                "Image": "v1"
            }
        ]

        httpretty.register_uri(
            httpretty.GET,
            "http://api.tsuru.target/deploys",
            status=200,
            content_type='application/json',
            body=json.dumps(all_deploys)
        )

        client_instance = client.Client("http://api.tsuru.target", "tsuru_token")
        result = client_instance.deploys.list()

        self.assertEqual(all_deploys, result)

    def test_deploys_list_with_querystring_param(self):
        all_deploys = [
            {
                "ID": "791",
                "App": "critical-app",
                "Image": "v1",
            },
            {
                "ID": "1000",
                "App": "critical-app",
                "Image": "v2",
            }
        ]

        httpretty.register_uri(
            httpretty.GET,
            "http://api.tsuru.target/deploys?app=critical-app",
            status=200,
            content_type='application/json',
            body=json.dumps(all_deploys)
        )

        params = {
            "app": "critical-app"
        }

        client_instance = client.Client("http://api.tsuru.target", "tsuru_token")
        result = client_instance.deploys.list(**params)

        self.assertEqual(all_deploys, result)

        request = httpretty.last_request()

        expected = {"app": ["critical-app"]}
        self.assertEqual(expected, request.querystring)

    def test_deploys_list_when_has_no_deploys(self):

        httpretty.register_uri(
            httpretty.GET,
            "http://api.tsuru.target/deploys",
            status=204,
            content_type='application/json',
            body={}
        )

        client_instance = client.Client("http://api.tsuru.target", "tsuru_token")
        result = client_instance.deploys.list()

        self.assertEqual([], result)

    def test_deploys_list_with_deploy_id(self):
        deploy_data = {
            "ID": "1001",
            "App": "critical-app"
        }

        httpretty.register_uri(
            httpretty.GET,
            "http://api.tsuru.target/deploys/1001",
            status=200,
            content_type='application/json',
            body=json.dumps(deploy_data)
        )

        client_instance = client.Client("http://api.tsuru.target", "tsuru_token")
        result = client_instance.deploys.list(deploy_id="1001")

        self.assertEqual(deploy_data, result)
