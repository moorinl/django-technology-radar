import importlib


ALPHABETICALLY_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                             'u', 'v', 'w', 'x', 'y', 'z']


def convert_queryset_to_alphabetically_dict(qs):
    context = {}
    for char in ALPHABETICALLY_CHARACTERS:
        context[char] = [
            obj for obj in qs if obj.name.lower().startswith(char)]
    return context


def import_class(name):
    module_name, class_name = name.rsplit('.', 1)
    return getattr(importlib.import_module(module_name), class_name)
