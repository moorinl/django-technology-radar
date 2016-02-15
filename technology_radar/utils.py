import importlib


def import_class(name):
    module_name, class_name = name.rsplit('.', 1)
    return getattr(importlib.import_module(module_name), class_name)
