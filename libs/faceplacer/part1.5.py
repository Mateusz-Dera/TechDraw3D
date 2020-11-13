# Mateusz Dera
# 1.0 (Blender 2.82)
# - dodaje głębię do ścian tworząc z nich obiekt 3D
# - sprawdza czy istnieją co najmniej 2 rzuty z różnych perspektyw 
# cd C:\TechDraw3D\face_to_mesh\
# 'C:\Program Files\Blender Foundation\Blender 2.82\blender.exe' -b --python part1.py

import bpy
import os.path
from os import path
from math import radians

faces_path = ('./assets/obj/temp/meshes/top.obj','./assets/obj/temp/meshes/bottom.obj','./assets/obj/temp/meshes/left.obj','./assets/obj/temp/meshes/right.obj','./assets/obj/temp/meshes/front.obj','./assets/obj/temp/meshes/back.obj')
faces_exist = (path.exists(faces_path[0]), path.exists(faces_path[1]), path.exists(faces_path[2]), path.exists(faces_path[3]), path.exists(faces_path[4]), path.exists(faces_path[5]))

# Czyszczenie sceny ze wszystkich domyślnie ładowanych obiektów
bpy.ops.wm.read_factory_settings(use_empty=True)

for i in range(0,6):
    if faces_exist[i] == True:
        bpy.ops.import_scene.obj(filepath=faces_path[i])
        for obj in bpy.context.selected_objects:
            obj.name = "face" + str(i)
            obj.data.name = "face" + str(i)
    print("face" + str(i))

# Zapisywanie meshy
if faces_exist[0]:
    object = bpy.data.objects['face0']
    bpy.context.view_layer.objects.active = object
    bpy.ops.object.select_all(action='DESELECT')
    object.select_set(True)
    modifier = object.modifiers.new(name="Remesh", type='REMESH')
    bpy.ops.object.modifier_apply(modifier="Remesh")
    modifier = object.modifiers.new(name="Triangulate", type='TRIANGULATE')
    bpy.ops.object.modifier_apply(modifier="Triangulate")
    bpy.ops.transform.resize(value=(100, 100, 100), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
    bpy.ops.object.origin_set(type="GEOMETRY_ORIGIN")
    bpy.ops.export_scene.obj(filepath="./assets/obj/temp/meshes/top.obj", check_existing=False, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl", use_selection=True, use_animation=False, use_mesh_modifiers=True, use_edges=True, use_smooth_groups=False, use_smooth_groups_bitflags=False, use_normals=True, use_uvs=True, use_materials=True, use_triangles=False, use_nurbs=False, use_vertex_groups=False, use_blen_objects=True, group_by_object=False, group_by_material=False, keep_vertex_order=False, global_scale=1, path_mode='AUTO')

if faces_exist[1]:
    object = bpy.data.objects['face1']
    bpy.context.view_layer.objects.active = object
    bpy.ops.object.select_all(action='DESELECT')
    object.select_set(True)
    modifier = object.modifiers.new(name="Remesh", type='REMESH')
    bpy.ops.object.modifier_apply(modifier="Remesh")
    modifier = object.modifiers.new(name="Triangulate", type='TRIANGULATE')
    bpy.ops.object.modifier_apply(modifier="Triangulate")
    bpy.ops.transform.resize(value=(100, 100, 100), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
    bpy.ops.object.origin_set(type="GEOMETRY_ORIGIN")
    bpy.ops.export_scene.obj(filepath="./assets/obj/temp/meshes/bottom.obj", check_existing=False, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl", use_selection=True, use_animation=False, use_mesh_modifiers=True, use_edges=True, use_smooth_groups=False, use_smooth_groups_bitflags=False, use_normals=True, use_uvs=True, use_materials=True, use_triangles=False, use_nurbs=False, use_vertex_groups=False, use_blen_objects=True, group_by_object=False, group_by_material=False, keep_vertex_order=False, global_scale=1, path_mode='AUTO')

if faces_exist[2]:
    object = bpy.data.objects['face2']
    bpy.context.view_layer.objects.active = object
    bpy.ops.object.select_all(action='DESELECT')
    object.select_set(True)
    modifier = object.modifiers.new(name="Remesh", type='REMESH')
    bpy.ops.object.modifier_apply(modifier="Remesh")
    modifier = object.modifiers.new(name="Triangulate", type='TRIANGULATE')
    bpy.ops.object.modifier_apply(modifier="Triangulate")
    bpy.ops.transform.resize(value=(100, 100, 100), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
    bpy.ops.object.origin_set(type="GEOMETRY_ORIGIN")
    bpy.ops.export_scene.obj(filepath="./assets/obj/temp/meshes/left.obj", check_existing=False, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl", use_selection=True, use_animation=False, use_mesh_modifiers=True, use_edges=True, use_smooth_groups=False, use_smooth_groups_bitflags=False, use_normals=True, use_uvs=True, use_materials=True, use_triangles=False, use_nurbs=False, use_vertex_groups=False, use_blen_objects=True, group_by_object=False, group_by_material=False, keep_vertex_order=False, global_scale=1, path_mode='AUTO')

if faces_exist[3]:
    object = bpy.data.objects['face3']
    bpy.context.view_layer.objects.active = object
    bpy.ops.object.select_all(action='DESELECT')
    object.select_set(True)
    modifier = object.modifiers.new(name="Remesh", type='REMESH')
    bpy.ops.object.modifier_apply(modifier="Remesh")
    modifier = object.modifiers.new(name="Triangulate", type='TRIANGULATE')
    bpy.ops.object.modifier_apply(modifier="Triangulate")
    bpy.ops.transform.resize(value=(100, 100, 100), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
    bpy.ops.object.origin_set(type="GEOMETRY_ORIGIN")
    bpy.ops.export_scene.obj(filepath="./assets/obj/temp/meshes/right.obj", check_existing=False, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl", use_selection=True, use_animation=False, use_mesh_modifiers=True, use_edges=True, use_smooth_groups=False, use_smooth_groups_bitflags=False, use_normals=True, use_uvs=True, use_materials=True, use_triangles=False, use_nurbs=False, use_vertex_groups=False, use_blen_objects=True, group_by_object=False, group_by_material=False, keep_vertex_order=False, global_scale=1, path_mode='AUTO')

if faces_exist[4]:
    object = bpy.data.objects['face4']
    bpy.context.view_layer.objects.active = object
    bpy.ops.object.select_all(action='DESELECT')
    object.select_set(True)
    modifier = object.modifiers.new(name="Remesh", type='REMESH')
    bpy.ops.object.modifier_apply(modifier="Remesh")
    modifier = object.modifiers.new(name="Triangulate", type='TRIANGULATE')
    bpy.ops.object.modifier_apply(modifier="Triangulate")
    bpy.ops.transform.resize(value=(100, 100, 100), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
    bpy.ops.object.origin_set(type="GEOMETRY_ORIGIN")
    bpy.ops.export_scene.obj(filepath="./assets/obj/temp/meshes/front.obj", check_existing=False, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl", use_selection=True, use_animation=False, use_mesh_modifiers=True, use_edges=True, use_smooth_groups=False, use_smooth_groups_bitflags=False, use_normals=True, use_uvs=True, use_materials=True, use_triangles=False, use_nurbs=False, use_vertex_groups=False, use_blen_objects=True, group_by_object=False, group_by_material=False, keep_vertex_order=False, global_scale=1, path_mode='AUTO')

if faces_exist[5]:
    object = bpy.data.objects['face5']
    bpy.context.view_layer.objects.active = object
    bpy.ops.object.select_all(action='DESELECT')
    object.select_set(True)
    modifier = object.modifiers.new(name="Remesh", type='REMESH')
    bpy.ops.object.modifier_apply(modifier="Remesh")
    modifier = object.modifiers.new(name="Triangulate", type='TRIANGULATE')
    bpy.ops.object.modifier_apply(modifier="Triangulate")
    bpy.ops.transform.resize(value=(100, 100, 100), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
    bpy.ops.object.origin_set(type="GEOMETRY_ORIGIN")
    bpy.ops.export_scene.obj(filepath="./assets/obj/temp/meshes/back.obj", check_existing=False, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl", use_selection=True, use_animation=False, use_mesh_modifiers=True, use_edges=True, use_smooth_groups=False, use_smooth_groups_bitflags=False, use_normals=True, use_uvs=True, use_materials=True, use_triangles=False, use_nurbs=False, use_vertex_groups=False, use_blen_objects=True, group_by_object=False, group_by_material=False, keep_vertex_order=False, global_scale=1, path_mode='AUTO')
