import os
from flask import Flask
from app.routes.__init__ import api_bp
from app.routes.task_routes import task_bp
from app.routes.response_routes import response_bp
from app.utils.db import get_db
from flask_cors import CORS
# import firebase_admin
# from firebase_admin import credentials, auth, initialize_app


def create_app():
    app = Flask(__name__)
    CORS(app)

    # Register blueprints
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(task_bp, url_prefix='/api/clasp-mobile/')
    app.register_blueprint(response_bp, url_prefix='/api/clasp-mobile/')

    return app


app = create_app()
