import json

from invoke import Collection
from invoke import task

from tasks.config import config
from tasks.core.context import Context


root = 'tasks'
component_name = 'consumer'

ctxt = Context()
ctxt.load(root, component_name)


@task
def rc(ctx):
    ''' shows invoke kong-cli run configuration
    '''

    config_json = json.dumps({**config._asdict()})
    print(config_json)


namespace = Collection(*ctxt.tasks, rc)
