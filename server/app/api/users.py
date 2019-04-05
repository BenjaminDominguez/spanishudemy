from app.api import bp
from flask import jsonify, request
from app import db
from app.models import User
from app.schema import user_schema, users_schema
from marshmallow import exceptions

@bp.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    try:
        user = User.query.get(id)
    except IntegrityError:
        return jsonify(
            {
                'message': 'User could not be found'
            }
        ), 400

    user_result = user_schema.dump(user)

    return jsonify({'user': user_result})

@bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users_result = users_schema.dump(users)
    return jsonify({'users': users_result})

@bp.route('/users', methods=['POST'])
def new_user():
    json_data = {
        'username': request.form.get('username'), 
        'password': request.form.get('password')
        }
    if not json_data:
        return jsonify({'message': 'No input data provided'}), 400
    data = user_schema.load(json_data)

    username, password = data['username'], data['password']
    check_user_exists = User.query.filter_by(username=username).first()

    if check_user_exists is None:
        user = User(username=username)
        user.create_password_hash(password)
        db.session.add(user)
        db.session.commit()

        result = user_schema.dump(user)
        return jsonify(
            {
                'message': 'New user created',
                'user': result
            }
        )