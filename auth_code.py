import requests
from config import config


def get_auth_code():
    response = requests.get(config.oauth_url, headers=config.headers)
    return response.json()['auth_code']
