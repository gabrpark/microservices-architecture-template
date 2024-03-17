import os
from flask import Flask
from app.routes.task_routes import task_bp
from app.routes.response_routes import response_bp
# from app.utils.db import db
from flask_cors import CORS
# from firebase_admin import credentials, initialize_app


def create_app():
    app = Flask(__name__)
    CORS(app)

    # # Initialize Firebase Admin SDK
    # firebase_config = {
    # # Firebase configuration dictionary
    # }
    # cred = credentials.Certificate(firebase_config)
    # initialize_app(cred)

    # Register blueprints
    app.register_blueprint(task_bp, url_prefix='/api/clasp-mobile/')
    app.register_blueprint(response_bp, url_prefix='/api/clasp-mobile/')

    return app


app = create_app()
