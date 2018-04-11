import requests

from tasks.core.models import MethodSpec
from tasks import config


# name: username or id
# plugin: plugin id
ENDPOINT = '/plugins/{id}'

ARGUMENT_HELP = {
    'id': 'plugin uuid'
}

METHODS = {
    'list': MethodSpec(
        method=requests.get, endpoint_params=(),
        request_data_params={},
        doc_url=f'{config.apidoc_url}/#list-all-plugins'),

    'retrieve': MethodSpec(
        method=requests.get, endpoint_params=('id', ),
        request_data_params={},
        doc_url=f'{config.apidoc_url}/#retrieve-plugin'),
}
