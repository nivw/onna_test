import requests
import json
from config import config
from logbook import Logger, StreamHandler
import sys

StreamHandler(sys.stdout).push_application()
log = Logger('auth')


class Auth(object):
    def __init__(self):
        self.config = config
        self.auth_code = self.token =None

    def get_auth_code(self):
        if self.auth_code is not None:
            return self.auth_code
        response = requests.get(self.config.oauth_url, headers=self.config.headers)
        self.auth_code = response.json()['auth_code']
        log.info(f"Using auth_code: {self.auth_code}")
        return self.auth_code

    def get_token(self):
        if self.token is not None:
            return self.token
        data = self.config.auth.login_data_request
        data.update({"code": self.get_auth_code()})
        response = requests.post(config.auth.auth_url,
                                 data=json.dumps(data),
                                 headers=config.headers)
        self.token = response.content.decode("utf-8")
        return self.token

    def get_login_token(self):
        return {'authorization': ' '.join(('Bearer', self.get_token()))}
