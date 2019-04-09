import requests

API_KEY = 'CC2AA1384BF4FE43CBDA81DF4D992B37'
BASE_URL = 'http://Api.steampowered.com'
RETRIES = 10

def build_url(path):
    return BASE_URL + '/' + path

def do_get(path, params):
    return do_get_retry(path, params, RETRIES)

def do_get_retry(path, params, retries_remaining):
    if retries_remaining > 0:
        url = build_url(path)
        print(url)
        params['key'] = API_KEY
        try:
            response = requests.get(url=url, params=params).json()
        except:
            response = do_get_retry(path, params, (retries_remaining - 1))
        return response