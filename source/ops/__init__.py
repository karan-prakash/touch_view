from . import actions, gizmo, touch

_registered = []


def register():
    for module in (actions, touch, gizmo):
        module.register()
        _registered.append(module)


def unregister():
    while _registered:
        _registered.pop().unregister()
