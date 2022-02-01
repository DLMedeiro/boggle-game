from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle

# (venv) python -m unittest test_app.py


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_home(self):
        resp = self.client.get('/')
        html = resp.get_data(as_text = True)

        self.assertEqual(resp.status_code, 200)
        self.assertIn('<h1>Boggle Home Page</h1>', html)
        
    def test_play(self):
        with app.test_client() as client:
            resp = client.get("/play_game")
            html = resp.get_data(as_text = True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<p>Current Score: 0 </p>', html)

    def test_valid_word(self):
        """Test if word is valid by modifying the board in the session"""

        with self.client as client:
            with client.session_transaction() as sess:
                sess['board'] = [["C", "A", "T", "T", "T"], 
                                ["C", "A", "T", "T", "T"], 
                                ["C", "A", "T", "T", "T"], 
                                ["C", "A", "T", "T", "T"], 
                                ["C", "A", "T", "T", "T"]]
        response = self.client.get('/check-word?word=cat')
        self.assertEqual(response.json['result'], 'ok')

