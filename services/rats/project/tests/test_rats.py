import json
import unittest
from project import db
from project.api.models import Rat
from project.tests.base import BaseTestCase


def add_rat(color, weight):
    rat = Rat(color=color, weight=weight)
    db.session.add(rat)
    db.session.commit()
    return rat


class TestRatsService(BaseTestCase):
    """Tests for the Rats Service."""

    def test_rats(self):
        """Ensure the /ping route behaves correctly."""
        response = self.client.get('/rats/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn('success', data['status'])

    def test_add_rat(self):
        """Ensure a new rat can be added to the database."""
        with self.client:
            response = self.client.post(
                '/rats',
                data=json.dumps({
                    'color': 'white',
                    'weight': '300'
                }),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('white was added!', data['message'])
            self.assertIn('success', data['status'])

    def test_add_rat_invalid_json(self):
        """Ensure error is thrown if the JSON object is empty."""
        with self.client:
            response = self.client.post(
                '/rats',
                data=json.dumps({}),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload.', data['message'])
            self.assertIn('fail', data['status'])

    def test_add_rat_invalid_json_keys(self):
        """
        Ensure error is thrown if the JSON object does not have a weight key.
        """
        with self.client:
            response = self.client.post(
                '/rats',
                data=json.dumps({'color': 'white'}),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload.', data['message'])
            self.assertIn('fail', data['status'])

    def test_single_rat(self):
        """Ensure get single rat behaves correctly."""
        rat = add_rat('white', 350)
        with self.client:
            response = self.client.get(f'/rats/{rat.id}')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn('white', data['data']['color'])
            self.assertEqual(350, data['data']['weight'])
            self.assertIn('success', data['status'])

    def test_single_rat_no_id(self):
        """Ensure error is thrown if an id is not provided."""
        with self.client:
            response = self.client.get('/rats/blah')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('Rat does not exist', data['message'])
            self.assertIn('fail', data['status'])

    def test_single_rat_incorrect_id(self):
        """Ensure error is thrown if the id does not exist."""
        with self.client:
            response = self.client.get('/rats/999')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('Rat does not exist', data['message'])
            self.assertIn('fail', data['status'])

    def test_all_rats(self):
        """Ensure get all rats behaves correctly."""
        add_rat('brown', 100)
        add_rat('black', 200)
        with self.client:
            response = self.client.get('/rats')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data['data']['rats']), 2)
            self.assertIn('brown', data['data']['rats'][0]['color'])
            self.assertEqual(
                100, data['data']['rats'][0]['weight'])
            self.assertIn('black', data['data']['rats'][1]['color'])
            self.assertEqual(
                200, data['data']['rats'][1]['weight'])
            self.assertIn('success', data['status'])

    def test_main_no_rats(self):
        """Ensure the main route behaves correctly when no rats have been
        added to the database."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'All Rats', response.data)
        self.assertIn(b'<p>No rats!</p>', response.data)

    def test_main_with_rats(self):
        """Ensure the main route behaves correctly when rats have been
        added to the database."""
        add_rat('brown', 100)
        add_rat('black', 200)
        with self.client:
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'All Rats', response.data)
            self.assertNotIn(b'<p>No rats!</p>', response.data)
            self.assertIn(b'brown', response.data)
            self.assertIn(b'black', response.data)

    def test_main_add_user(self):
        """Ensure a new rat can be added to the database."""
        with self.client:
            response = self.client.post(
                '/',
                data=dict(color='white', weight=300),
                follow_redirects=True
            )
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'All Rats', response.data)
            self.assertNotIn(b'<p>No rats!</p>', response.data)
            self.assertIn(b'white', response.data)


if __name__ == '__main__':
    unittest.main()
