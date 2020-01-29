from munch import Munch

config = Munch()
config.base_url = 'https://enterprise.onna.com/'
config.auth = Munch()
config.auth.auth_url = config.base_url + 'auth/oauth/get_auth_token'
config.auth.username = "qateam.onna@destinoalgum.com.br"
config.auth.password = "Onna12345678!"

config.oauth_url = config.base_url + 'api/qatest/qatest/@oauthgetcode?client_id=userdashboard&scope=qatest'
config.headers = Munch({
    'authority': 'enterprise.onna.com',
    'accept': 'application/json, text/plain, */*',
    'content-type': 'application/json',
    'origin': 'https://enterprise.onna.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'referer': 'https://enterprise.onna.com/qatest/user/login',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,he-IL;q=0.8,he;q=0.7',
    'dnt': '1'
    })
config.workspace = Munch()
config.workspace.create_url = config.base_url + 'api/qatest/qatest/groups'
config.workspace.create_keys = [
    '@id',
    'id',
    '@name',
    '@type',
    '@uid',
    'group_app_type',
    'title',
    'owners',
    'editors',
    'contributors',
    'viewers',
    'creators',
    'description',
    'creation_date',
    'modification_date',
    'template',
    'tags'
]