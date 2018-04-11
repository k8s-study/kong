import requests

from tasks.core.models import MethodSpec
from tasks import config


# name: username or id
# plugin: plugin id
ENDPOINT = '/apis/{name}/plugins/{plugin}'

ARGUMENT_HELP = {
    'name': 'api name or id',
    'plugin': 'plugin_id',
    'data': (
        'json string(e.g \'{"key": "value"}\') '
        'or json payload file path (e.g @payload.json)'
    )
}

METHODS = {
    'list': MethodSpec(
        method=requests.get, endpoint_params=('name', ),
        request_data_params={},
        doc_url=f'{config.apidoc_url}/#list-plugins-per-api'),

    'create': MethodSpec(
        method=requests.post, endpoint_params=('name', ),
        request_data_params={'data': ''},
        doc_url=f'{config.apidoc_url}/#add-plugin'),

    'delete': MethodSpec(
        method=requests.delete, endpoint_params=('name', 'plugin'),
        request_data_params={},
        doc_url=f'{config.apidoc_url}/#delete-plugin'),
}
