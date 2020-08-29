import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Club, Player

coach_token = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ilh3czRDOENNSlhBd0dTQ3BDZXh6dyJ9.eyJpc3MiOiJodHRwczovL21hbHphaWQxLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZjQyNWNhN2ZlNDUyNzAwNmQ5M2I1ZjkiLCJhdWQiOiJjYXBzdG9uZXAiLCJpYXQiOjE1OTg2NzA1MTIsImV4cCI6MTU5ODc1NjkxMiwiYXpwIjoiTFV1MnZKMndqOU1rNDV6YVJta2oybU5LZmNGVWNyaVAiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDpwbGF5ZXJzIl19.F7dBuJ7LlfyN66C_nY4o9PjMrzBEkpP2DPyPeoSVwfUYVCBLwNudiiAjfB3uFbuU4jzRFsZvy2RrnpdbDU9-tbKPhUVhoHA7aHQj7mGABKK5myTZYVfYL7mDGGFQqT7Y2sDzXe49e2rPP4Sz8OU5U3ytILLk-FQFasGBStGUviIu14oaQw3vuadY_sMS4zJI4p7UdNXTSceb01_sW7yCqa7WYxroEjJJl3esSIQ6549eyLDwqe0eM0hZrNTXSyF759iHxnUW1fljjHs47ZjKErRbojfTfKM2digCfJjw0fRg3iIQVCSvgLdniuoJC90-xB-5h_67QJa3VPUwhnzOtg"
director_token = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ilh3czRDOENNSlhBd0dTQ3BDZXh6dyJ9.eyJpc3MiOiJodHRwczovL21hbHphaWQxLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZjQyNWQ0YTM4ZDFhMjAwNmQyMWM3NzMiLCJhdWQiOiJjYXBzdG9uZXAiLCJpYXQiOjE1OTg2NzA3NDUsImV4cCI6MTU5ODc1NzE0NSwiYXpwIjoiTFV1MnZKMndqOU1rNDV6YVJta2oybU5LZmNGVWNyaVAiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpwbGF5ZXJzIiwiZ2V0OnBsYXllcnMiLCJwYXRjaDpwbGF5ZXJzIiwicG9zdDpjbHVicyIsInBvc3Q6cGxheWVycyJdfQ.MXsmwaCX38TQ7XyX1Blu72TLF3Yxx0qpM6R6tMopJUnJedVMjXIlpMtqCY5xQO7S-tA4goF1g0o1IOnKWigiYN9Raipja3PrevmMJexyjVvpX09J_pZGujq0YYTZKB_zHVI58pctmrqqvro-ZFQrclEfn_CpQVuw-Kqd9LTalbhO90fAWtWypcudaPOTzkS-n3Rgnij12yGBrOubQgClnCp8kCY4PtqhB2p9chFgI4NA8eihvRvipKuNcCFbjsRot5c1TY_XmkPnLJiJDWZYlQrQnu-6Lsa_3RtKMf8V9Ea4SEZxyuL67gxEfg7v0UtnpWqo88SkkBS3EhOQkcmOaA"


class FinalProjectTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(True)
        self.client = self.app.test_client
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
    GET PLAYERS BY CLUB
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
    PATCH PLAYER
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
