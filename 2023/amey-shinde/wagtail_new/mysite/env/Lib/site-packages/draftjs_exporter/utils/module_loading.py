from __future__ import absolute_import, unicode_literals

from importlib import import_module


def import_string(dotted_path):
    """
    Import a dotted module path and return the attribute/class designated by the
    last name in the path. Raise ImportError if the import failed.

    Taken from Django:
    https://github.com/django/django/blob/f6bd00131e687aedf2719ad31e84b097562ca5f2/django/utils/module_loading.py#L7-L24
    """
    try:
        module_path, class_name = dotted_path.rsplit('.', 1)
    except ValueError:
        raise ImportError("%s doesn't look like a module path" % dotted_path)

    module = import_module(module_path)

    try:
        return getattr(module, class_name)
    except AttributeError:
        raise ImportError('Module "%s" does not define a "%s" attribute/class' % (
            module_path, class_name)
        )
