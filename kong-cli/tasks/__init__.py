import json

from invoke import Collection
from invoke import task

from tasks.config import config
from tasks.core.context import Context


ctxt = Context(config)

for component in config.components:
    ctxt.load(config.suites_root, component)


@task
def rc(ctx):
    ''' shows invoke kong-cli run configuration
    '''

    config_json = json.dumps({**config._asdict()})
    print(config_json)


namespace = Collection(*ctxt.tasks, rc)
