from functools import wraps

import jwt
from jwt import ExpiredSignatureError
from werkzeug.security import safe_str_cmp
from configuration import conf_properties, sso_properties

from auth import User


def authenticate(username, password) -> User:
    if username is conf_properties.get_user() and safe_str_cmp(password.encode('utf-8'), conf_properties.get_password().encode('utf-8')):
        return User(1, username, password)


def identity(payload) -> User:
    return User(1, payload['username'], None)


def login_required(f):
    @wraps(f)
    def jwt_socket_login(namespace_object, message):
        try:
            data = jwt.decode(message['token'], sso_properties.get_secret_key())
            if data[conf_properties.get_claim()] == conf_properties.get_user():
                return f(namespace_object, message)
        except ExpiredSignatureError:
            raise ConnectionRefusedError('authentication failed')

    return jwt_socket_login
