import unittest
import sys
from io import StringIO

import requests
import requests_mock

from tasks.core.api_call_task import ApiCallTask
from tasks.core.models import Config


class TestApiCallTask(unittest.TestCase):
    def setUp(self):
        self.config = Config(
            kong_admin_url='mock://unittest.kong.com',
            apidoc_url='',
            suites_root='',
            components=[]
        )

        self.session = requests.Session()
        self.adapter = requests_mock.Adapter()
        self.session.mount('mock', self.adapter)


    def _create_call_task(self):
        return ApiCallTask(
            kong_admin_url=self.config.kong_admin_url,
            name='test_call_task',
            doc='call_task_documentation',
            endpoint='/endpoint/{0}/test/{1}',
            endpoint_params=('arg_a', 'arg_b'),
            requests_method=self.session.get)

    def test_task_should_be_created(self):
        task = self._create_call_task()

        self.assertEqual(
            task.full_api_url,
            'mock://unittest.kong.com/endpoint/{0}/test/{1}')

    def test_task_should_be_callable(self):
        task = self._create_call_task()
        self.assertTrue(callable(task))

        self.adapter.register_uri(
            'GET', 'mock://unittest.kong.com/endpoint/1/test/2',
            text='this_is_unittest')

        invoke_ctx = {}
        invoke_task_args = {'arg_a': 1, 'arg_b': 2}
        out = sys.stdout = StringIO()
        task(invoke_ctx, *invoke_task_args.values())
        output = out.getvalue().strip()
        self.assertEqual(output, 'this_is_unittest')

