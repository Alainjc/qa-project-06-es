import configuration
import requests
import data


def post_new_user(body):
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                             json=body,
                             headers=data.headers)
    return response

def user_token():
    user_token = post_new_user(data.user_body)
    response = user_token.json()
    return response['authToken']


def new_kit(body):
    autorization_header = data.headers.copy()
    token = user_token()
    autorization_header['Authorization'] = f"Bearer {token}"

    response = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                             json=body,
                             headers=autorization_header)
    return response





