import inspect
import typing


def get_all_funcs_from_module(module) -> typing.Iterator[callable]:
    """ Returns all functions defined in `module`

    """