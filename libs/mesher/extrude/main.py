# TechDraw3D
# Copyright © 2020 Tomasz Nowak, Mateusz Dera, Jakub Schwarz

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
from math import radians
import sys

path = str(sys.argv[3])[:-7] + "tmp/"
export_path = str(sys.argv[3])[:-7] + "../boolean/tmp/"

print("Import path: " + path)
print("Export path: " + export_path)

names = ['top', 'bottom', 'left', 'right', 'front', 'back']

faces_path =  ['top', 'bottom', 'left', 'right', 'front', 'back']

for q in range(0,len(names)):
    faces_path[q] = str(path) + str(names[q]) + '.obj'

faces_exist = (os.path.isfile(faces_path[0]), os.path.isfile(faces_path[1]), os.path.isfile(faces_path[2]), os.path.isfile(faces_path[3]), os.path.isfile(faces_path[4]), os.path.isfile(faces_path[5]))

# Czyszczenie sceny ze wszystkich domyślnie ładowanych obiektów
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False, confirm=False)

# Sprawdzenie czy istnieją co najmniej 2 rzuty z różnych perspektyw
x = int(faces_exist[0]) + int(faces_exist[1])
y = int(faces_exist[2]) + int(faces_exist[3])
z = int(faces_exist[4]) + int(faces_exist[5])

if x > 0:
    x = 1

if y > 0:
    y = 1

if z > 0:
    z = 1

if x + y + z < 2:
    print("Missing dimensions!")
    exit()
else:
    print('ok')

# Import ścian
for i in range(0,len(names)):
    if faces_exist[i] == True:
        bpy.ops.import_scene.obj(filepath=faces_path[i])
        for obj in bpy.context.selected_objects:
            obj.name = names[i]
            obj.data.name = names[i]
        print(names[i])

#Rotacja ścian / Kalkulacja głębokości ścian

len_x = [0,0,0,0]
len_y = [0,0,0,0]
len_z = [0,0,0,0]

# Top
if faces_exist[0]:
    len_x[0] = bpy.data.objects[names[0]].dimensions.x
    len_y[0] = bpy.data.objects[names[0]].dimensions.z

# Bottom
if faces_exist[1]:
    len_x[1] = bpy.data.objects[names[1]].dimensions.x
    len_y[1] = bpy.data.objects[names[1]].dimensions.z

# Left
if faces_exist[2]:
    bpy.ops.transform.rotate(value=-1.5708, orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
    len_x[2] = bpy.data.objects[names[2]].dimensions.x
    len_z[3] = bpy.data.objects[names[2]].dimensions.z

# Right
if faces_exist[3]:
    bpy.ops.transform.rotate(value=-1.5708, orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
    len_x[3] = bpy.data.objects[names[3]].dimensions.x
    len_z[2] = bpy.data.objects[names[3]].dimensions.z

# Front
if faces_exist[4]:
    bpy.ops.transform.rotate(value=1.5708, orient_axis='Y', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
    len_y[2] = bpy.data.objects[names[4]].dimensions.z
    len_z[0] = bpy.data.objects[names[4]].dimensions.x

# Back
if faces_exist[5]:
    bpy.ops.transform.rotate(value=1.5708, orient_axis='Y', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
    len_y[3] = bpy.data.objects[names[5]].dimensions.z
    len_z[1] = bpy.data.objects[names[5]].dimensions.x

print('Koniec obracania\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

val_x = max(len_x)
val_y = max(len_y)
val_z = max(len_z)

print(len_x)
print(len_y)
print(len_z)

# Objętość
V = val_x * val_y * val_z

# Zapisywanie meshy
if faces_exist[0]:
    object = bpy.data.objects[names[0]]
    bpy.context.view_layer.objects.active = object
    bpy.ops.object.select_all(action='DESELECT')
    object.select_set(True)
    modifier = object.modifiers.new(name="Solidify", type='SOLIDIFY')
    modifier.thickness = val_x
    bpy.ops.object.modifier_apply(modifier="Solidify")

    # modifier = object.modifiers.new(name="Mirror", type='MIRROR')
    # modifier.use_axis[0] = False
    # modifier.use_axis[1] = True
    # bpy.ops.object.modifier_apply(modifier="Mirror")

    modifier = object.modifiers.new(name="Triangulate", type='TRIANGULATE')
    bpy.ops.object.modifier_apply(modifier="Triangulate")

    # Switch to edit mode
    bpy.ops.object.editmode_toggle()

    # Select all edges
    bpy.ops.mesh.select_all(action='SELECT')

    # Move mesh to center
    bpy.ops.object.origin_set(type="GEOMETRY_ORIGIN")

    #object.location.z += val_x/2
    bpy.ops.export_scene.obj(filepath=str(export_path) + str(names[0]) + '.obj', check_existing=False, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl", use_selection=True, use_animation=False, use_mesh_modifiers=True, use_edges=True, use_smooth_groups=False, use_smooth_groups_bitflags=False, use_normals=True, use_uvs=True, use_materials=True, use_triangles=False, use_nurbs=False, use_vertex_groups=False, use_blen_objects=True, group_by_object=False, group_by_material=False, keep_vertex_order=False, global_scale=1, path_mode='AUTO')

if faces_exist[1]:
    object = bpy.data.objects[names[1]]
    bpy.context.view_layer.objects.active = object
    bpy.ops.object.select_all(action='DESELECT')
    object.select_set(True)
    modifier = object.modifiers.new(name="Solidify", type='SOLIDIFY')
    modifier.thickness = val_x
    bpy.ops.object.modifier_apply(modifier="Solidify")

    # modifier = object.modifiers.new(name="Mirror", type='MIRROR')
    # modifier.use_axis[0] = False
    # modifier.use_axis[1] = True
    # bpy.ops.object.modifier_apply(modifier="Mirror")

    modifier = object.modifiers.new(name="Triangulate", type='TRIANGULATE')
    bpy.ops.object.modifier_apply(modifier="Triangulate")

    # Switch to edit mode
    bpy.ops.object.editmode_toggle()

    # Select all edges
    bpy.ops.mesh.select_all(action='SELECT')

    # Move mesh to center
    bpy.ops.object.origin_set(type="GEOMETRY_ORIGIN")

    #object.location.z += val_x/2
    bpy.ops.export_scene.obj(filepath=str(export_path) + str(names[1]) + '.obj', check_existing=False, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl", use_selection=True, use_animation=False, use_mesh_modifiers=True, use_edges=True, use_smooth_groups=False, use_smooth_groups_bitflags=False, use_normals=True, use_uvs=True, use_materials=True, use_triangles=False, use_nurbs=False, use_vertex_groups=False, use_blen_objects=True, group_by_object=False, group_by_material=False, keep_vertex_order=False, global_scale=1, path_mode='AUTO')

if faces_exist[2]:
    object = bpy.data.objects[names[2]]
    bpy.context.view_layer.objects.active = object
    bpy.ops.object.select_all(action='DESELECT')
    object.select_set(True)
    modifier = object.modifiers.new(name="Solidify", type='SOLIDIFY')
    modifier.thickness = val_x
    bpy.ops.object.modifier_apply(modifier="Solidify")

    # modifier = object.modifiers.new(name="Mirror", type='MIRROR')
    # modifier.use_axis[0] = False
    # modifier.use_axis[1] = True
    # bpy.ops.object.modifier_apply(modifier="Mirror")

    modifier = object.modifiers.new(name="Triangulate", type='TRIANGULATE')
    bpy.ops.object.modifier_apply(modifier="Triangulate")
    
    # Switch to edit mode
    bpy.ops.object.editmode_toggle()

    # Select all edges
    bpy.ops.mesh.select_all(action='SELECT')

    # Move mesh to center
    bpy.ops.object.origin_set(type="GEOMETRY_ORIGIN")

    #object.location.y += val_y/2
    bpy.ops.export_scene.obj(filepath=str(export_path) + str(names[2]) + '.obj', check_existing=False, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl", use_selection=True, use_animation=False, use_mesh_modifiers=True, use_edges=True, use_smooth_groups=False, use_smooth_groups_bitflags=False, use_normals=True, use_uvs=True, use_materials=True, use_triangles=False, use_nurbs=False, use_vertex_groups=False, use_blen_objects=True, group_by_object=False, group_by_material=False, keep_vertex_order=False, global_scale=1, path_mode='AUTO')

if faces_exist[3]:
    object = bpy.data.objects[names[3]]
    bpy.context.view_layer.objects.active = object
    bpy.ops.object.select_all(action='DESELECT')
    object.select_set(True)
    modifier = object.modifiers.new(name="Solidify", type='SOLIDIFY')
    modifier.thickness = val_x
    bpy.ops.object.modifier_apply(modifier="Solidify")

    # modifier = object.modifiers.new(name="Mirror", type='MIRROR')
    # modifier.use_axis[0] = False
    # modifier.use_axis[1] = True
    # bpy.ops.object.modifier_apply(modifier="Mirror")

    modifier = object.modifiers.new(name="Triangulate", type='TRIANGULATE')
    bpy.ops.object.modifier_apply(modifier="Triangulate")
    
    # Switch to edit mode
    bpy.ops.object.editmode_toggle()

    # Select all edges
    bpy.ops.mesh.select_all(action='SELECT')

    # Move mesh to center
    bpy.ops.object.origin_set(type="GEOMETRY_ORIGIN")

    #object.location.y += val_y/2
    bpy.ops.export_scene.obj(filepath=str(export_path) + str(names[3]) + '.obj', check_existing=False, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl", use_selection=True, use_animation=False, use_mesh_modifiers=True, use_edges=True, use_smooth_groups=False, use_smooth_groups_bitflags=False, use_normals=True, use_uvs=True, use_materials=True, use_triangles=False, use_nurbs=False, use_vertex_groups=False, use_blen_objects=True, group_by_object=False, group_by_material=False, keep_vertex_order=False, global_scale=1, path_mode='AUTO')

if faces_exist[4]:
    object = bpy.data.objects[names[4]]
    bpy.context.view_layer.objects.active = object
    bpy.ops.object.select_all(action='DESELECT')
    object.select_set(True)
    modifier = object.modifiers.new(name="Solidify", type='SOLIDIFY')
    modifier.thickness = val_x
    bpy.ops.object.modifier_apply(modifier="Solidify")
    
    # modifier = object.modifiers.new(name="Mirror", type='MIRROR')
    # modifier.use_axis[0] = False
    # modifier.use_axis[1] = True
    # bpy.ops.object.modifier_apply(modifier="Mirror")
    
    modifier = object.modifiers.new(name="Triangulate", type='TRIANGULATE')
    bpy.ops.object.modifier_apply(modifier="Triangulate")
    
    # Switch to edit mode
    bpy.ops.object.editmode_toggle()

    # Select all edges
    bpy.ops.mesh.select_all(action='SELECT')

    # Move mesh to center
    bpy.ops.object.origin_set(type="GEOMETRY_ORIGIN")

    #object.location.x -= val_x/2
    bpy.ops.export_scene.obj(filepath=str(export_path) + str(names[4]) + '.obj', check_existing=False, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl", use_selection=True, use_animation=False, use_mesh_modifiers=True, use_edges=True, use_smooth_groups=False, use_smooth_groups_bitflags=False, use_normals=True, use_uvs=True, use_materials=True, use_triangles=False, use_nurbs=False, use_vertex_groups=False, use_blen_objects=True, group_by_object=False, group_by_material=False, keep_vertex_order=False, global_scale=1, path_mode='AUTO')
    
if faces_exist[5]:
    object = bpy.data.objects[names[5]]
    bpy.context.view_layer.objects.active = object
    bpy.ops.object.select_all(action='DESELECT')
    object.select_set(True)
    modifier = object.modifiers.new(name="Solidify", type='SOLIDIFY')
    modifier.thickness = val_x
    bpy.ops.object.modifier_apply(modifier="Solidify")
    
    # modifier = object.modifiers.new(name="Mirror", type='MIRROR')
    # modifier.use_axis[0] = False
    # modifier.use_axis[1] = True
    # bpy.ops.object.modifier_apply(modifier="Mirror")
    
    modifier = object.modifiers.new(name="Triangulate", type='TRIANGULATE')
    bpy.ops.object.modifier_apply(modifier="Triangulate")
    
    # Switch to edit mode
    bpy.ops.object.editmode_toggle()

    # Select all edges
    bpy.ops.mesh.select_all(action='SELECT')

    # Move mesh to center
    bpy.ops.object.origin_set(type="GEOMETRY_ORIGIN")
    
    #object.location.x -= val_x/2
    bpy.ops.export_scene.obj(filepath=str(export_path) + str(names[5]) + '.obj', check_existing=False, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl", use_selection=True, use_animation=False, use_mesh_modifiers=True, use_edges=True, use_smooth_groups=False, use_smooth_groups_bitflags=False, use_normals=True, use_uvs=True, use_materials=True, use_triangles=False, use_nurbs=False, use_vertex_groups=False, use_blen_objects=True, group_by_object=False, group_by_material=False, keep_vertex_order=False, global_scale=1, path_mode='AUTO')