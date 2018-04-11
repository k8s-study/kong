import requests

from tasks.core.models import MethodSpec
from tasks import config


ENDPOINT = '/consumers/{name}'  # 0: username or id

ARGUMENT_HELP = {
    'name': 'consumer username or id',
    'data': (
        'json string(e.g \'{"username": "john.doe"}\') '
        'or json payload file path (e.g @payload.json)'
    )
}

METHODS = {
    'list': MethodSpec(
        method=requests.get, endpoint_params=(),
        request_data_params={},
        doc_url=f'{config.apidoc_url}/#list-consumers'),

    'retrieve': MethodSpec(
        method=requests.get, endpoint_params=('name', ),
        request_data_params={},
        doc_url=f'{config.apidoc_url}/#retrieve-consumer'),

    'create': MethodSpec(
        method=requests.post, endpoint_params=(),
        request_data_params={'data': ''},
        doc_url=f'{config.apidoc_url}/#create-consumer'),

    'delete': MethodSpec(
        method=requests.delete, endpoint_params=('name', ),
        request_data_params={},
        doc_url=f'{config.apidoc_url}/#delete-consumer'),
}
