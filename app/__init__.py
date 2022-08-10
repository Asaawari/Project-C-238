# line 3 to 7 - importing all required libraries

import os
from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# line 11 to 12 - instantiate the extensions

db = SQLAlchemy()
migrate = Migrate()

# line 16 - creating a function called 'create_app' 

def create_app(script_info=None):

    # line 20 to 21 - instantiate the app

    app = Flask(__name__)
    cors = CORS(app)

    # line 25 to 27 - set config

    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
    app.config['CORS_HEADERS'] = 'Content-Type'

    # iine 31 to 32 - set up extensions

    db.init_app(app)
    migrate.init_app(app, db)

    # line 36 to 40 - register blueprints

    from .views.views import views
    from .api.api import api

    app.register_blueprint(views)
    app.register_blueprint(api)

    # line 44 to 49 - handling error 400

    @app.errorhandler(400)
    def bad_request(e):
        return jsonify({
            "status":"error",
            "error":e.description
        }), 400

    # line 53 to 58 - handling error 404

    @app.errorhandler(404)
    def not_found_error(e):
        return jsonify({
            "status":"error",
            "error":e.description
        }), 404

    # line 62 to 67 - handling error 500

    @app.errorhandler(500)
    def server_error(e):
        return jsonify({
            "status":"error",
            "error":"this wasn't suppose to happen"
        })

    # line 71 to 74 - shell context for flask cli

    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}
    return app