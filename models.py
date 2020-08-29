from sqlalchemy import Column, String, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

# database_path = os.environ['DATABASE_URL']
database_path = "postgres://xjrgdzeziyqdoa:47bfcd51346b75dfe1d2d33ebcedf7ccb6ee2643a910fdb1097455f65c76b412@ec2-34-236-215-156.compute-1.amazonaws.com:5432/d3i6kjjjiobs61"
db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


class Club(db.Model):
    # __tablename__ = 'Club'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    league = db.Column(db.String, nullable=False)
    players = db.relationship("Player", backref="team")

    def __init__(self, name, league, players=[]):
        self.name = name
        self.league = league
        self.players = players

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "id": self.id,
            "name": self.name,
            "league": self.league
        }


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    club = db.Column(db.Integer, db.ForeignKey("club.id"))

    def __init__(self, name, age, club):
        self.name = name
        self.age = age
        self.club = club

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "club": self.club
        }

    def no_club_format(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age
        }