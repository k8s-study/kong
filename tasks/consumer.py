from invoke import task
import requests

from tasks.config import config


@task
def get(ctx, name=''):
    response = requests.get(
        f'{config.kong_admin_url}/consumers/{name}')

    print(response.content.decode())


@task
def create(ctx, name=''):
    response = requests.post(
        f'{config.kong_admin_url}/consumers/',
        data={'username': name})

    print(response.content.decode())


@task
def delete(ctx, name=''):
    response = requests.delete(
        f'{config.kong_admin_url}/consumers/{name}')

    print(response.content.decode())
