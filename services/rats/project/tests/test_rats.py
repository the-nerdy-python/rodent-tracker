import json
import unittest

from project.tests.base import BaseTestCase


class TestRatsService(BaseTestCase):
    """Tests for the Rats Service."""

    def test_rats(self):
        """Ensure the /ping route behaves correctly."""
        response = self.client.get('/rats/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn('success', data['status'])


if __name__ == '__main__':
    unittest.main()