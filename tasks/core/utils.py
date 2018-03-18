import json


DATA_PARAM_HELP = {
    'data': (
        'json string(e.g \'{"username": "john.doe"}\') '
        'or json payload file path (e.g @payload.json)'
    )
}


def get_payload(data_or_path):
    if data_or_path:
        if data_or_path.startswith('@'):
            with open(data_or_path[1:]) as file:
                content = ''.join(file.readlines())
                payload = json.loads(content)
        else:
            payload = json.loads(data_or_path)

    else:
        payload = {}

    return payload


def request_and_print_response(kong_admin_url, requests_method,
                               endpoint, data=None):
    response = requests_method(kong_admin_url + endpoint, data=data)
    print(response.content.decode())
