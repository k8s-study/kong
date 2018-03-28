class ProxyDefinition(object):
    def __init__(self, store_name, origin_fn_name,
                 fn_name, fn_args, fn_kwargs):
        self._store_name = store_name
        self._origin_fn_name = origin_fn_name
        self._name = fn_name
        self._fn_args = fn_args
        self._fn_kwargs = fn_kwargs

    @property
    def _definition_arguments(self):
        return ', '.join([
            *self._fn_args,
            *(f'{kwarg}=""' for kwarg in self._fn_kwargs)
        ])

    @property
    def _passing_arguments(self):
        return ', '.join([
            *self._fn_args,
            *(f'{kwarg}={kwarg}' for kwarg in self._fn_kwargs)
        ])

    @property
    def as_string(self):
        exec_routine = (
            # set origin function to proxy_store
            f'{self._store_name}["{self._origin_fn_name}"] = {self._origin_fn_name}\n'

            # define proxy function which calls stored origin function
            f'def {self._name}({self._definition_arguments}):'
            f'return {self._store_name}["{self._origin_fn_name}"]({self._passing_arguments})'
        )

        return exec_routine
