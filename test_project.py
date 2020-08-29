import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Club, Player

coach_token = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ilh3czRDOENNSlhBd0dTQ3BDZXh6dyJ9.eyJpc3MiOiJodHRwczovL21hbHphaWQxLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZjQyNWNhN2ZlNDUyNzAwNmQ5M2I1ZjkiLCJhdWQiOiJjYXBzdG9uZXAiLCJpYXQiOjE1OTg2Mjg3MjQsImV4cCI6MTU5ODcxNTEyNCwiYXpwIjoiTFV1MnZKMndqOU1rNDV6YVJta2oybU5LZmNGVWNyaVAiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDpwbGF5ZXJzIl19.p4Ugmk0lpN86Tz6UBYASUQnxyH3XDb_7g9Mbkn--sgbf46uJO46nZXciT8XpizwuZ7McKFQS5hM7fd0akH5FnrHfDbBvbCgndOWzoGfOJFlREFIlnCEpjj8o-fycd6FPXDFq6CH0RB0n2ZfJ2rYoQs_FxVu3wu34t8klgVbIwbuBZpUnye6FByLVDlKWj0n3Pbc_674LVjTl1y6-9oim1Gn-wUQpyG_qJ88XOpcYursyM-sh45yRoJrecyVKwfYQubu9i_A4AHEBSJ5JWJOZAUzJW_mcM6EYJhX9ZHteR--IloSO6aYdBRGTZonsJad85vLAd0-30ovoZlSipdkE6w"
director_token = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ilh3czRDOENNSlhBd0dTQ3BDZXh6dyJ9.eyJpc3MiOiJodHRwczovL21hbHphaWQxLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZjQyNWQ0YTM4ZDFhMjAwNmQyMWM3NzMiLCJhdWQiOiJjYXBzdG9uZXAiLCJpYXQiOjE1OTg2MzAwODcsImV4cCI6MTU5ODcxNjQ4NywiYXpwIjoiTFV1MnZKMndqOU1rNDV6YVJta2oybU5LZmNGVWNyaVAiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpwbGF5ZXJzIiwiZ2V0OnBsYXllcnMiLCJwYXRjaDpwbGF5ZXJzIiwicG9zdDpjbHVicyIsInBvc3Q6cGxheWVycyJdfQ.viREQwCJ11hnTjZSoQh0lgBOKoW3rr43ANLpoRi0GWt48MPUUds_6zFN65O25hsZyqJpVxYQOFEZTzQMKx4Bm7kXR7hKs3lT2HQJwuC_Eowab5-LbdcZ7WoEQeTf9PeaGoaUtv-XBjeNDFqzUwUdDt2EF1QcQVaLrVzLXbvdeJl6p-X5cm4naO7jdtzpyjRqDBq8QAM4Uk9cGIT2Gfsg3-1jUQZZ1Whwkbf4laxIN8B97mLtL5dVM-s2BkZPGzgJHOZugpIbLMA0-VNxSMeRgEWJdm6neOw26GR3PtEz6se8mbqQpN7YYa467ovA4dAIIqQSx7NnTr_C0uk2A2HQ4g"


class FinalProjectTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        # self.database_name = "trivia_test"
        # self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        self.database_path = "postgres://postgres:1234@localhost:5432/final_project"
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    CLUBS
    """

    def test_get_clubs(self):
        res = self.client().get('/clubs')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['clubs'])

    def test_get_clubs_method_not_allowed(self):
        res = self.client().patch('/clubs')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')

    """
    PLAYERS
    """

    def test_get_players(self):
        res = self.client().get('/players', headers={"Authorization": coach_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['players'])

    def test_get_players_method_not_allowed(self):
        res = self.client().patch('/players', headers={"Authorization": coach_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')

    """
    GET QUESTIONS FROM CATEGORY
    """

    def test_get_players_by_club(self):
        res = self.client().get('/clubs/1/players', headers={"Authorization": coach_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['players'])

    def test_get_players_by_invalid_club(self):
        res = self.client().get('/clubs/NaN/players', headers={"Authorization": coach_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    """
    POST CLUB
    """

    def test_create_new_club(self):
        res = self.client().post('/clubs', json={'name': 'Real Madrid', 'league': 'Laliga'},
                                 headers={"Authorization": director_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['club'])

    def test_post_club_method_not_allowed(self):
        res = self.client().post('/clubs/1', json={'name': 'Real Madrid', 'league': 'Laliga'},
                                 headers={"Authorization": director_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    """
    POST PLAYER
    """

    def test_create_new_player(self):
        res = self.client().post('/players', json={'name': 'Ramos', 'age': 34, "club": 1},
                                 headers={"Authorization": director_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['player'])

    def test_post_player_method_not_allowed(self):
        res = self.client().post('/players/1', json={'name': 'Ramos', 'age': 34, "club": 1},
                                 headers={"Authorization": director_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')

    """
    POST PLAYER
    """

    def test_edit_player(self):
        res = self.client().patch('/players/7', json={'name': 'Ramos', 'age': 34, "club": 1},
                                  headers={"Authorization": director_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['player'])

    def test_patch_player_does_not_exist(self):
        res = self.client().post('/players/55555', json={'name': 'Ramos', 'age': 34, "club": 1},
                                 headers={"Authorization": director_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')

    """
    DELETE QUESTION
    """

    def test_delete_player(self):
        res = self.client().delete('/players/8', headers={"Authorization": director_token})
        data = json.loads(res.data)

        player = Player.query.filter(Player.id == 8).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['delete'], 8)
        self.assertTrue(data['delete'])
        self.assertEqual(player, None)

    def test_delete_player_does_not_exist(self):
        res = self.client().delete('/players/99999', headers={"Authorization": director_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
