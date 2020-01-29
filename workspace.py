import requests
from config import config
from auth import get_login_token
import json


def get_id(name):
    return name.replace('_', '').lower()


def create_workspace(name):
    data = {
        "@type":"Group",
        "title": name,
        "group_app_type":"web",
        "id": get_id(name)
        }

    headers = config.headers
    headers.referer = 'https://enterprise.onna.com/qatest/user/dashboard/workspace/list'
    headers.update(get_login_token())
    response = requests.post(config.workspace.create_url, data=json.dumps(data), headers=headers)
    #print(headers)
    return response
"""
curl 'https://enterprise.onna.com/api/qatest/qatest/groups'
-H 'authority: enterprise.onna.com'
-H 'accept: application/json'
-H 'dnt: 1'
-H 'authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODAzMzMzMjAsImV4cCI6MTU4MDkzODEyMCwidG9rZW4iOiI1ZDVjNzM4N2E4ZGU0ZWUzYjA3ZmJiNTA5YTNiZTU1ZSIsImxvZ2luIjoicWF0ZWFtLm9ubmFAZGVzdGlub2FsZ3VtLmNvbS5iciIsIm5hbWUiOiJxYSIsInN1cGVydXNlciI6ZmFsc2V9.p0T7VQTvVrqnbjuojvL_EB2yiw2WyqJwlelfLOwR30Q'
-H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
-H 'content-type: application/json'
-H 'origin: https://enterprise.onna.com'
-H 'sec-fetch-site: same-origin'
-H 'sec-fetch-mode: cors'
-H 'referer: https://enterprise.onna.com/qatest/user/dashboard/workspace/list'
-H 'accept-encoding: gzip, deflate, br'
-H 'accept-language: en-US,en;q=0.9,he-IL;q=0.8,he;q=0.7'
-H 'cookie: __stripe_mid=78fa550b-126b-41ff-ab7b-331cc3bfb30d; _ga=GA1.2.273277141.1580333244; _gid=GA1.2.1839527386.1580333244; __stripe_sid=72d430b2-ab1e-4849-a384-132021e1e71f'

--data-binary '{"@type":"Group","title":"New_fabulous","group_app_type":"web","id":"newfabulous"}' --compressed
"""
