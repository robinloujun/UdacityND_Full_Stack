import os
from flask import Flask
from models import setup_db


def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    @app.route('/')
    def index():
        return "Welcome to the Capstone Car Booking Platform!"

    # Error Handling
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'bad request',
        }), 400

    @app.errorhandler(401)
    def method_not_allowed(error):
        return jsonify({
            'success': False,
            'error': 401,
            'message': 'method not allowed',
        }), 401

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'resource not found',
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': 'internal server error',
        }), 500

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
