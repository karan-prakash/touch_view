# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


bl_info = {
    "name": "Touch Viewport",
    "description": "Creates active touch zones over View 2D and 3D areas for easier viewport navigation with touch screens and pen tablets.",
    "author": "NENDO, Karan @b3dhub",
    "blender": (3, 3, 0),
    "version": (4, 2, 2),
    "category": "3D View",
    "location": "View3D > Tools > NENDO",
    "warning": "",
    "doc_url": "https://github.com/b3dhub/touch_view",
    "tracker_url": "https://github.com/b3dhub/touch_view/issues",
}


import bpy

from . import preferences, source


def register():
    try:
        source.register()
        preferences.register()
        bpy.context.preferences.addons[__package__].preferences.load()  # type: ignore
        preferences.update_header_toggle_position(bpy.context)
    except Exception:
        unregister()
        raise


def unregister():
    addon = bpy.context.preferences.addons.get(__package__)
    if addon is not None:
        try:
            addon.preferences.save()
        except Exception:
            pass
    try:
        source.unregister()
    except Exception:
        pass
    try:
        preferences.unregister()
    except Exception:
        pass
