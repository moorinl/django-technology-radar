import importlib


ALPHABETICALLY_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                             'u', 'v', 'w', 'x', 'y', 'z']


def import_class(name):
    module_name, class_name = name.rsplit('.', 1)
    return getattr(importlib.import_module(module_name), class_name)


def get_alphabetically_sorted_list(items, attribute='name'):
    return items
