from controllers.profile_controller import create_profile, fetch_own_profile
from flask import Blueprint, request, Response, make_response, jsonify
from flask_cors import cross_origin

profile_blueprint = Blueprint('profile_blueprint', __name__, url_prefix='/api/v1/profile')


@profile_blueprint.route('/create', methods=['POST'])
@cross_origin(supports_credentials=True)
def create():
    content = request.get_json(silent=True)
    res = create_profile(body=content)
    return res


@profile_blueprint.route('/me', methods=['GET'])
@cross_origin(supports_credentials=True)
def fetch_me():
    content = request.get_json(silent=True)
    res = fetch_own_profile(data=content)
    return res


@profile_blueprint.route('/check', methods=['GET'])
def api_check():
    return make_response(jsonify({'success': True, 'data': "API is working"}), 200)
