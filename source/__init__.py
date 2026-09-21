from . import ops, ui, utils

_registered = []


def register():
    for module in (ops, ui, utils):
        module.register()
        _registered.append(module)


def unregister():
    while _registered:
        _registered.pop().unregister()
