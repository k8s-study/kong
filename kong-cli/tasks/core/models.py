from collections import namedtuple


MethodSpec = namedtuple('MethodSpec', (
    'method', 'doc_url', 'endpoint_params', 'request_data_params'
))

Config = namedtuple('Config', [
    'kong_admin_url', 'apidoc_url', 'suites_root', 'components'
])
