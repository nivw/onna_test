import requests
import json
from config import config
from auth_code import get_auth_code


def get_token():
    auth_code = get_auth_code()
    data = {
           "grant_type": "user",
           "code": auth_code,
           "username": config.auth.username,
           "password": config.auth.password,
           "scopes": ["qatest"],
           "client_id": "userdashboard"
           }
    response = requests.post(config.auth.auth_url,
                             data=json.dumps(data),
                             headers=config.headers)
    return response.content.decode("utf-8")


def get_login_token():
    return {'authorization': ' '.join(('Bearer', get_token()))}
