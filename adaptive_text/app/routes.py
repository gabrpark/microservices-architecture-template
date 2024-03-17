from flask import Blueprint, request, jsonify
from app.models import Text
# from app.utils.auth import authenticate

text_bp = Blueprint('text', __name__)


# @text_bp.route('/texts', methods=['POST'])
# # @authenticate
# def create_text():
#     data = request.json
#     text = Text(data['title'], data['content'], data['completed'])
#     result = text.save()
#     return jsonify({'id': str(result.inserted_id)}), 201


@text_bp.route('/texts', methods=['GET'])
# @authenticate
def get_texts():
    args = request.args.to_dict()
    texts = Text.get_all(args)
    return jsonify(texts), 200


# @text_bp.route('/texts/<text_id>', methods=['GET'])
# # @authenticate
# def get_text(text_id):
#     text = Text.get_by_id(text_id)
#     if text:
#         return jsonify(text), 200
#     else:
#         return jsonify({'error': 'text not found'}), 404


# @text_bp.route('/texts/<text_id>', methods=['PUT'])
# # @authenticate
# def update_text(text_id):
#     data = request.json
#     text = Text.get_by_id(text_id)
#     if text:
#         text.title = data['title']
#         text.content = data['content']
#         text.completed = data['completed']
#         text.update()
#         return jsonify(text), 200
#     else:
#         return jsonify({'error': 'text not found'}), 404


# @text_bp.route('/texts/<text_id>', methods=['DELETE'])
# @authenticate
# def delete_text(text_id):
#     result = text.delete_by_id(text_id)
#     if result.deleted_count > 0:
#         return '', 204
#     else:
#         return jsonify({'error': 'text not found'}), 404
