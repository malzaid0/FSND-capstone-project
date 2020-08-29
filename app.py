import os
from flask import Flask, request, abort, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from auth import AuthError, requires_auth
from models import setup_db, Club, Player


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    # ROUTES
    '''
        GET /general-view
    '''

    @app.route('/clubs', methods=['GET'])
    def get_clubs():
        selection = Club.query.all()
        clubs = [club.format() for club in selection]

        return jsonify({
            'success': True,
            'clubs': clubs
        })

    '''
        GET /hr-view
    '''

    @app.route('/players', methods=['GET'])
    @requires_auth('get:players')
    def get_players(jwt):
        selection = Player.query.all()
        players = [player.format() for player in selection]

        return jsonify({
            'success': True,
            'players': players
        })

    '''
        GET /executive-view
    '''

    @app.route('/clubs/<int:club_id>/players', methods=['GET'])
    @requires_auth('get:players')
    def get_club_players(jwt, club_id):
        selection = Player.query.filter(Player.club == club_id).all()
        players = [player.no_club_format() for player in selection]

        return jsonify({
            'success': True,
            'players': players
        })

    '''
    POST /employee
    '''

    @app.route('/clubs', methods=['POST'])
    @requires_auth('post:clubs')
    def post_clubs(jwt):
        entered = request.get_json()
        new_name = entered['name']
        new_league = entered['league']

        try:
            new_club = Club(name=new_name, league=new_league)
            new_club.insert()

            return jsonify({
                'success': True,
                'club': new_club.format()
            })

        except:
            abort(422)

    @app.route('/players', methods=['POST'])
    @requires_auth('post:players')
    def post_players(jwt):
        entered = request.get_json()
        new_name = entered['name']
        new_age = entered['age']
        new_club = entered['club']

        try:
            new_player = Player(name=new_name, age=new_age, club=new_club)
            new_player.insert()

            return jsonify({
                'success': True,
                'player': new_player.format()
            })

        except:
            abort(422)

    '''
    PATCH /employees/<id>
    '''

    @app.route('/players/<int:player_id>', methods=['PATCH'])
    @requires_auth('patch:players')
    def patch_player(jwt, player_id):
        try:
            player = Player.query.get(player_id)
            entered = request.get_json()
            new_name = entered.get('name', None)
            new_age = entered.get('age', None)
            new_club = entered.get('club', None)

            if player is None:
                abort(404)
            if new_name is not None:
                player.name = new_name
            if new_age is not None:
                player.age = new_age
            if new_club is not None:
                player.club = new_club

            player.update()

            return jsonify({
                'success': True,
                'player': player.format()
            })

        except:
            abort(422)

    '''
        DELETE /employees/<id>
    '''

    @app.route('/players/<int:player_id>', methods=['DELETE'])
    @requires_auth('delete:players')
    def delete_employee(jwt, player_id):
        try:
            player = Player.query.get(player_id)

            if player is None:
                abort(404)

            player.delete()

            return jsonify({
                'success': True,
                'delete': player_id
            })

        except:
            abort(422)

    ## Error Handling

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(404)
    def not_found_handler(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'resource not found'
        }), 404

    @app.errorhandler(405)
    def not_found_handler(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': 'method not allowed'
        }), 405

    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            'success': False,
            'error': error.status_code,
            'message': error.error
        })

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
