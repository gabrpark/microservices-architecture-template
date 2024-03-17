from flask import Blueprint, request, jsonify
# from app.utils.auth import authenticate

api_bp = Blueprint('api', __name__)


@api_bp.route('/')
def index():
    return "API for ClaSP Mobile is running!"


# @api_bp.route('/protected')
# @authenticate
# def protected_route():
#     return {"message": "This is protected"}, 200
