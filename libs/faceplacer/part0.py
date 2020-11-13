# Mateusz Dera
# 1.0 (Blender 2.82)
# "C:\Program Files\Blender Foundation\Blender 2.82\blender.exe" -b --python part0.py

import bpy
import os.path
from os import path
bpy.ops.wm.read_factory_settings(use_empty=True)

def make_path(p):
    p = os.path.expanduser(p)
    p = os.path.normpath(p)
    p = os.path.realpath(p)
    p = os.path.abspath(p)
    return p

top_path = make_path(".\\assets\\svg\\temp\\walls\\top.svg")
bottom_path = make_path(".\\assets\\svg\\temp\\walls\\bottom.svg")
left_path = make_path(".\\assets\\svg\\temp\\walls\\left.svg")
right_path = make_path(".\\assets\\svg\\temp\\walls\\right.svg")
front_path = make_path(".\\assets\\svg\\temp\\walls\\front.svg")
back_path = make_path(".\\assets\\svg\\temp\\walls\\back.svg")

top = None
bottom = None
left = None
right = None
front = None
back = None

if path.exists(top_path) == True:
    bpy.ops.import_curve.svg(filepath=top_path)
    bpy.ops.object.select_all(action='SELECT')
    for o in bpy.data.objects:
        o.select_set(True)
        bpy.context.view_layer.objects.active = o
    bpy.ops.object.join()
    bpy.ops.object.convert(target='MESH')
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.remove_doubles()
    bpy.ops.mesh.edge_face_add()
    bpy.ops.object.origin_set(type="GEOMETRY_ORIGIN")
    bpy.ops.export_scene.obj(filepath="./assets/obj/temp/faces/top.obj", check_existing=False, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl", use_selection=True, use_animation=False, use_mesh_modifiers=True, use_edges=True, use_smooth_groups=False, use_smooth_groups_bitflags=False, use_normals=True, use_uvs=True, use_materials=True, use_triangles=False, use_nurbs=False, use_vertex_groups=False, use_blen_objects=True, group_by_object=False, group_by_material=False, keep_vertex_order=False, global_scale=1, path_mode='AUTO')
    for item in bpy.data.meshes:
        bpy.data.meshes.remove(item)

if path.exists(bottom_path) == True:
    bpy.ops.import_curve.svg(filepath=top_path)
    bpy.ops.object.select_all(action='SELECT')
    for o in bpy.data.objects:
        o.select_set(True)
        bpy.context.view_layer.objects.active = o
    bpy.ops.object.join()
    bpy.ops.object.convert(target='MESH')
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.remove_doubles()
    bpy.ops.mesh.edge_face_add()
    bpy.ops.object.origin_set(type="GEOMETRY_ORIGIN")
    bpy.ops.export_scene.obj(filepath="./assets/obj/temp/faces/bottom.obj", check_existing=False, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl", use_selection=True, use_animation=False, use_mesh_modifiers=True, use_edges=True, use_smooth_groups=False, use_smooth_groups_bitflags=False, use_normals=True, use_uvs=True, use_materials=True, use_triangles=False, use_nurbs=False, use_vertex_groups=False, use_blen_objects=True, group_by_object=False, group_by_material=False, keep_vertex_order=False, global_scale=1, path_mode='AUTO')
    for item in bpy.data.meshes:
        bpy.data.meshes.remove(item)

if path.exists(left_path) == True:
    left = bpy.ops.import_curve.svg(filepath=left_path)
    for o in bpy.data.objects:
        o.select_set(True)
        bpy.context.view_layer.objects.active = o
    bpy.ops.object.join()
    bpy.ops.object.convert(target='MESH')
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.remove_doubles()
    bpy.ops.mesh.edge_face_add()
    bpy.ops.object.origin_set(type="GEOMETRY_ORIGIN")
    bpy.ops.export_scene.obj(filepath="./assets/obj/temp/faces/left.obj", check_existing=False, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl", use_selection=True, use_animation=False, use_mesh_modifiers=True, use_edges=True, use_smooth_groups=False, use_smooth_groups_bitflags=False, use_normals=True, use_uvs=True, use_materials=True, use_triangles=False, use_nurbs=False, use_vertex_groups=False, use_blen_objects=True, group_by_object=False, group_by_material=False, keep_vertex_order=False, global_scale=1, path_mode='AUTO')
    for item in bpy.data.meshes:
        bpy.data.meshes.remove(item)

if path.exists(right_path) == True:
    right = bpy.ops.import_curve.svg(filepath=right_path)
    for o in bpy.data.objects:
        o.select_set(True)
        bpy.context.view_layer.objects.active = o
    bpy.ops.object.join()
    bpy.ops.object.convert(target='MESH')
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.remove_doubles()
    bpy.ops.mesh.edge_face_add()
    bpy.ops.object.origin_set(type="GEOMETRY_ORIGIN")
    bpy.ops.export_scene.obj(filepath="./assets/obj/temp/faces/right.obj", check_existing=False, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl", use_selection=True, use_animation=False, use_mesh_modifiers=True, use_edges=True, use_smooth_groups=False, use_smooth_groups_bitflags=False, use_normals=True, use_uvs=True, use_materials=True, use_triangles=False, use_nurbs=False, use_vertex_groups=False, use_blen_objects=True, group_by_object=False, group_by_material=False, keep_vertex_order=False, global_scale=1, path_mode='AUTO')
    for item in bpy.data.meshes:
        bpy.data.meshes.remove(item)


if path.exists(front_path) == True:
    front = bpy.ops.import_curve.svg(filepath=front_path)
    for o in bpy.data.objects:
        o.select_set(True)
        bpy.context.view_layer.objects.active = o
    bpy.ops.object.join()
    bpy.ops.object.convert(target='MESH')
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.remove_doubles()
    bpy.ops.mesh.edge_face_add()
    bpy.ops.object.origin_set(type="GEOMETRY_ORIGIN")
    bpy.ops.export_scene.obj(filepath="./assets/obj/temp/faces/front.obj", check_existing=False, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl", use_selection=True, use_animation=False, use_mesh_modifiers=True, use_edges=True, use_smooth_groups=False, use_smooth_groups_bitflags=False, use_normals=True, use_uvs=True, use_materials=True, use_triangles=False, use_nurbs=False, use_vertex_groups=False, use_blen_objects=True, group_by_object=False, group_by_material=False, keep_vertex_order=False, global_scale=1, path_mode='AUTO')
    for item in bpy.data.meshes:
        bpy.data.meshes.remove(item)

if path.exists(back_path) == True:
    back = bpy.ops.import_curve.svg(filepath=back_path)
    for o in bpy.data.objects:
        o.select_set(True)
        bpy.context.view_layer.objects.active = o
    bpy.ops.object.join()
    bpy.ops.object.convert(target='MESH')
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.remove_doubles()
    bpy.ops.mesh.edge_face_add()
    bpy.ops.object.origin_set(type="GEOMETRY_ORIGIN")
    bpy.ops.export_scene.obj(filepath="./assets/obj/temp/faces/back.obj", check_existing=False, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl", use_selection=True, use_animation=False, use_mesh_modifiers=True, use_edges=True, use_smooth_groups=False, use_smooth_groups_bitflags=False, use_normals=True, use_uvs=True, use_materials=True, use_triangles=False, use_nurbs=False, use_vertex_groups=False, use_blen_objects=True, group_by_object=False, group_by_material=False, keep_vertex_order=False, global_scale=1, path_mode='AUTO')
    for item in bpy.data.meshes:
        bpy.data.meshes.remove(item)