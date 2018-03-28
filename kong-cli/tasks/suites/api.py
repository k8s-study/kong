import requests

from tasks.core.models import MethodSpec
from tasks import config


ENDPOINT = '/apis/{0}'  # 0: username or id

ARGUMENT_HELP = {
    'name': 'api name or id',
    'data': (
        'json string(e.g \'{"key": "value"}\') '
        'or json payload file path (e.g @payload.json)'
    )
}

METHODS = {
    'list': MethodSpec(
        method=requests.get, endpoint_params=(),
        request_data_params={},
        doc_url=f'{config.apidoc_url}/#list-apis'),

    'retrieve': MethodSpec(
        method=requests.get, endpoint_params=('name', ),
        request_data_params={},
        doc_url=f'{config.apidoc_url}/#retrieve-api'),

    'create': MethodSpec(
        method=requests.post, endpoint_params=(),
        request_data_params={'data': ''},
        doc_url=f'{config.apidoc_url}/#add-api'),

    'delete': MethodSpec(
        method=requests.delete, endpoint_params=('name', ),
        request_data_params={},
        doc_url=f'{config.apidoc_url}/#delete-api'),
}
