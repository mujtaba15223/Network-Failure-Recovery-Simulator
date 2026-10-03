import unittest

from app import app


class NetworkApiContractTests(unittest.TestCase):
    def test_network_route_includes_links(self):
        client = app.test_client()
        response = client.get("/api/network")

        self.assertEqual(response.status_code, 200)

        payload = response.get_json()
        self.assertIn("links", payload)
        self.assertIsInstance(payload["links"], dict)
        self.assertTrue(payload["links"])


if __name__ == "__main__":
    unittest.main()
