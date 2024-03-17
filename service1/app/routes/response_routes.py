from flask import Blueprint, request, jsonify
from app.models.response_model import ResponseModel
# from app.utils.auth import authenticate

response_bp = Blueprint('response', __name__)


@response_bp.route('/responses', methods=['GET'])
# @authenticate
def get_responses():
    '''
    Get all responses.
    '''
    args = request.args.to_dict()
    response_model = ResponseModel()
    documents = response_model.find_all(args)
    return jsonify(documents)


@response_bp.route('/responses', methods=['POST'])
# @authenticate
def create_response():
    '''
    Create a new response.
    '''
    data = request.json
    response_model = ResponseModel()
    response_id = response_model.insert(data)
    return {'id': response_id}, 201
