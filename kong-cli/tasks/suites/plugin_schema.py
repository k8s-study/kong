import requests

from tasks.core.models import MethodSpec
from tasks import config


ENDPOINT = '/plugins/schema/{name}'

ARGUMENT_HELP = {
    'name': 'plugin name'
}

METHODS = {
    'retrieve': MethodSpec(
        method=requests.get, endpoint_params=('name', ),
        request_data_params={},
        doc_url=f'{config.apidoc_url}/#retrieve-plugin-schema'),
}
