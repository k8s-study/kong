from tasks.core.models import Config


config = Config(
    kong_admin_url='http://apigw-admin.pong.com',
    apidoc_url='https://getkong.org/docs/0.12.x/admin-api',
    suites_root='tasks.suites',
    components=[
        'status',
        'consumer',
        'api'
    ]
)
