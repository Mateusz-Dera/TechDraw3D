# TechDraw3D
# Copyright © 2020-2021 Tomasz Nowak, Mateusz Dera, Jakub Schwarz

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import bpy
import os.path
from os import path
import sys

path = str(sys.argv[3])[:-7] + "export/"
#export_path = str(sys.argv[3])[:-7] + "export/"
export_path = str(sys.argv[3])[:-7] + str(sys.argv[5])
mesh_path = str(path) + 'mesh.obj'

# Czyszczenie sceny ze wszystkich domyślnie ładowanych obiektów
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False, confirm=False)

# Import ścian
bpy.ops.import_scene.obj(filepath=mesh_path)
for obj in bpy.context.selected_objects:
    obj.name = "mesh"
    obj.data.name = "mesh"

# STL
typ = '-stl'
if str(sys.argv[4]) == typ:
    bpy.ops.export_mesh.stl(filepath=str(export_path), use_selection=True)
# FBX
typ = '-fbx'
if str(sys.argv[4]) == typ:
    bpy.ops.export_scene.fbx(filepath=str(export_path), use_selection = True)

# OBJ
typ = '-obj'
if str(sys.argv[4]) == typ:
    bpy.ops.export_scene.obj(filepath=str(export_path), check_existing=False, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl", use_selection=True, use_animation=False, use_mesh_modifiers=True, use_edges=True, use_smooth_groups=False, use_smooth_groups_bitflags=False, use_normals=True, use_uvs=True, use_materials=True, use_triangles=False, use_nurbs=False, use_vertex_groups=False, use_blen_objects=True, group_by_object=False, group_by_material=False, keep_vertex_order=False, global_scale=1, path_mode='AUTO')

os.remove(mesh_path)