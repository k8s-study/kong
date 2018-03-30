import requests

from tasks.core.models import MethodSpec
from tasks import config


ENDPOINT = '/'

METHODS = {
    'information': MethodSpec(
        method=requests.get, endpoint_params=(),
        request_data_params={},
        doc_url=f'{config.apidoc_url}/#retrieve-node-information'),
}
