import os

from collections import namedtuple

Config = namedtuple('Config', [
    'kong_admin_url'
])

config = Config(
    kong_admin_url='http://localhost:8001'
)


