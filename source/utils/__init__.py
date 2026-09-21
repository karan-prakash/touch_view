from . import keymaps
from .overlay import Overlay

ov = Overlay()


def register():
    keymaps.register()
    ov.draw_ui()


def unregister():
    ov.clear_overlays()
    keymaps.unregister()
