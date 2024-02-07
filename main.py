import logging
import os
from functools import wraps
import firebase_admin
from firebase_admin import credentials, auth
from flask import Flask, request, jsonify
from flask_talisman import Talisman
from flask_cors import CORS
from flask_restful import Api, Resource
from pymongo import MongoClient
# from dotenv import load_dotenv

# load_dotenv()

app = Flask(__name__)  # Create Flask app
api = Api(app)  # Create API
CORS(app)  # Enable CORS
Talisman(app)  # Enable HTTPS
# client = MongoClient('mongodb://localhost:27017/')
# db = client['clasp']

firebase_config = {
    "type": os.getenv("FIREBASE_TYPE"),
    "project_id": os.getenv("FIREBASE_PROJECT_ID"),
    "private_key_id": os.getenv("FIREBASE_PRIVATE_KEY_ID"),
    "private_key": os.getenv("FIREBASE_PRIVATE_KEY").replace(r'\n', '\n'),
    "client_email": os.getenv("FIREBASE_CLIENT_EMAIL"),
    "client_id": os.getenv("FIREBASE_CLIENT_ID"),
    "auth_uri": os.getenv("FIREBASE_AUTH_URI"),
    "token_uri": os.getenv("FIREBASE_TOKEN_URI"),
    "auth_provider_x509_cert_url": os.getenv("FIREBASE_AUTH_PROVIDER_X509_CERT_URL"),
    "client_x509_cert_url": os.getenv("FIREBASE_CLIENT_X509_CERT_URL"),
    "universe_domain": os.getenv("FIREBASE_UNIVERSE_DOMAIN")
}

# Initialize Firebase Admin
cred = credentials.Certificate(firebase_config)
firebase_admin.initialize_app(cred)


def verify_firebase_token(token):
    try:
        decoded_token = auth.verify_id_token(token)
        return decoded_token
    except Exception as e:
        logging.error(f"Error verifying Firebase token: {e}")
        return None


# @app.route('/protected', methods=['GET'])
# def verify_token():
#     # id_token = request.json.get('idToken')
#     id_token = request.headers.get('Authorization')
#     try:
#         # Verify the ID token while checking if it's revoked
#         decoded_token = auth.verify_id_token(id_token, check_revoked=True)
#         uid = decoded_token['uid']
#         return {'status': 'success', 'uid': uid}, 200
#     except auth.RevokedIdTokenError:
#         # Token has been revoked. Inform the user to reauthenticate or signOut().
#         logging.error('Token has been revoked')
#         return {'status': 'error', 'message': 'Token has been revoked'}, 401
#     except auth.InvalidIdTokenError:
#         # Token is invalid
#         logging.error('Invalid token')
#         return {'status': 'error', 'message': 'Invalid token'}, 401

def authenticate(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        id_token = request.headers.get('Authorization')
        if not id_token:
            return {'status': 'error', 'message': 'Authorization token missing'}, 401

        try:
            decoded_token = auth.verify_id_token(id_token, check_revoked=True)
            request.user = decoded_token
            # return f(*args, **kwargs)
        except auth.RevokedIdTokenError:
            logging.error('Token revoked')
            return {'status': 'error', 'message': 'Token has been revoked'}, 401
        except auth.InvalidIdTokenError:
            logging.error('Invalid token')
            return {'status': 'error', 'message': 'Invalid token'}, 401
        except Exception as e:
            logging.error('Authentication error: %s', str(e))
            return {'status': 'error', 'message': 'Authentication error'}, 500

    return decorated_function


# class AuthenticatedResource(Resource):
#     def dispatch_request(self, *args, **kwargs):
#         auth_result = authenticate()
#         if auth_result:
#             return auth_result
#         return super(AuthenticatedResource, self).dispatch_request(*args, **kwargs)


class Status(Resource):
    @authenticate
    def get(self):
        try:
            return {'data': 'Api is Running'}
        except:
            return {'data': 'An Error Occurred during fetching Api'}


class MongoDBResource(Resource):
    @authenticate
    def __init__(self):
        self.db = MongoClient(os.environ.get("NGROK_MONGO_URL")).clasp
        super().__init__()

    @authenticate
    def get(self, collection_name):
        args = request.args.to_dict()
        collection = self.db[collection_name]
        documents = list(collection.find(args, {'_id': 0}))
        return jsonify(documents)

    @authenticate
    def post(self, collection_name):
        data = request.json
        collection = self.db[collection_name]
        result = collection.insert_one(data)
        return {'id': str(result.inserted_id)}


api.add_resource(Status, '/')
# api.add_resource(ProtectedAPI, '/protected')
api.add_resource(MongoDBResource, '/api/<collection_name>/')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
