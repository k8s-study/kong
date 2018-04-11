import requests

from tasks.core.models import MethodSpec
from tasks import config


# name: username or id
# plugin: plugin id
ENDPOINT = '/plugins/enabled'

ARGUMENT_HELP = {}

METHODS = {
    'list': MethodSpec(
        method=requests.get, endpoint_params=(),
        request_data_params={},
        doc_url=f'{config.apidoc_url}/#retrieve-enabled-plugins'),
}
