from invoke import Collection
from invoke import task

from tasks import consumer
from tasks.config import config


@task
def rc(ctx):
    ''' shows invoke kong-cli run configuration
    '''

    print(config)


namespace = Collection(consumer, rc)
