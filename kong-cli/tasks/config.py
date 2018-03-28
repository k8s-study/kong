from tasks.core.models import Config


config = Config(
    kong_admin_url='http://localhost:8001',
    apidoc_url='https://getkong.org/docs/0.12.x/admin-api',
    suites_root='tasks.suites',
    components=[
        'consumer'
    ]
)
