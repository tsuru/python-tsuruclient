from tsuruclient import client

import unittest
import httpretty


class EventsTestCase(unittest.TestCase):

    cl = client.Client("http://target", "abc123")

    def setUp(self):
        httpretty.enable()

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_list(self):
        url = "http://target/1.1/events"
        httpretty.register_uri(
            httpretty.GET,
            url,
            status=200
        )
        self.cl.events.list(kindname="node.create")
        self.assertEqual("/1.1/events?kindname=node.create",
                         httpretty.last_request().path)

    def test_list_kinds(self):
        url = "http://target/1.1/events/kinds"
        httpretty.register_uri(
            httpretty.GET,
            url,
            status=200
        )
        self.cl.events.list_kinds()
        self.assertEqual("/1.1/events/kinds", httpretty.last_request().path)

    def test_get(self):
        url = "http://target/1.1/events/123"
        httpretty.register_uri(
            httpretty.GET,
            url,
            status=200
        )
        self.cl.events.get(123)
        self.assertEqual("/1.1/events/123", httpretty.last_request().path)

    def test_cancel(self):
        url = "http://target/1.1/events/123/cancel"
        httpretty.register_uri(
            httpretty.POST,
            url,
            status=200
        )
        self.cl.events.cancel(123)
        self.assertEqual("/1.1/events/123/cancel", httpretty.last_request().path)
