###
# Gizmo structure update
#
# Refactor the gizmo structure to be more modular and easier to maintain.
# Gizmo context (UI, space, etc), state (2-mode, 3-mode, etc),
# layout (vertical, horizontal, etc)
# to be managed through inheritance.
###
from . import gizmo_group_2d, panel

_registered = []


def register():
    for module in (gizmo_group_2d, panel):
        module.register()
        _registered.append(module)


def unregister():
    while _registered:
        _registered.pop().unregister()
