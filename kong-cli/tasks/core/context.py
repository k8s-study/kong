import importlib

from invoke import task

from tasks.core.api_call_task import ApiCallTask
from tasks.core.proxy_definition import ProxyDefinition

CTX_NS_PROXY_STORE_NAME = '__proxy_store'
INVOKE_CTX_ARG_NAME = 'ctx'


class Context(object):
    # invoke tasks
    tasks = []

    _config = None

    # exec() namespace
    _namespace = {
        CTX_NS_PROXY_STORE_NAME: {}
    }

    def __init__(self, config):
        self._config = config

    def load(self, root, component_name):
        task_module = importlib.import_module(f'{root}.{component_name}')

        endpoint = getattr(task_module, 'ENDPOINT')
        methods = getattr(task_module, 'METHODS')
        arg_help = getattr(task_module, 'ARGUMENT_HELP', {})

        for method, spec in methods.items():
            invoke_task_name = f'{component_name}-{method}'
            origin_fn_name = f'_origin_{component_name}_{method}'
            proxy_fn_name = f'_proxy_{component_name}_{method}'

            self._namespace[origin_fn_name] = ApiCallTask(
                kong_admin_url=self._config.kong_admin_url,
                name=invoke_task_name, requests_method=spec.method,
                doc=spec.doc_url, endpoint=endpoint,
                endpoint_params=spec.endpoint_params)

            proxy_fn = ProxyDefinition(
                store_name=CTX_NS_PROXY_STORE_NAME,
                origin_fn_name=origin_fn_name,
                fn_name=proxy_fn_name,
                fn_args=[INVOKE_CTX_ARG_NAME, *spec.endpoint_params],
                fn_kwargs=spec.request_data_params)

            # execute define proxy function and bind to invoke task's body.
            exec(proxy_fn.as_string, self._namespace)
            invoke_task = task(
                self._namespace[origin_fn_name], help=arg_help)

            # set proxy function signature as task.body.
            invoke_task.body = self._namespace[proxy_fn_name]
            self.tasks.append(invoke_task)
