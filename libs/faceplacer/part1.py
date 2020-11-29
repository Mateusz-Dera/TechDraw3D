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

faces_path = ('./assets/obj/temp/faces/top.obj','./assets/obj/temp/faces/bottom.obj','./assets/obj/temp/faces/left.obj','./assets/obj/temp/faces/right.obj','./assets/obj/temp/faces/front.obj','./assets/obj/temp/faces/back.obj')
faces_exist = (path.exists(faces_path[0]), path.exists(faces_path[1]), path.exists(faces_path[2]), path.exists(faces_path[3]), path.exists(faces_path[4]), path.exists(faces_path[5]))

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

# Import ścian
for i in range(0,6):
    if faces_exist[i] == True:
        bpy.ops.import_scene.obj(filepath=faces_path[i])
        for obj in bpy.context.selected_objects:
            obj.name = "face" + str(i)
            obj.data.name = "face" + str(i)
    print("face" + str(i))

#Rotacja ścian / Kalkulacja głębokości ścian

len_x = [0,0,0,0]
len_y = [0,0,0,0]
len_z = [0,0,0,0]

# Top
#bpy.data.objects["face0"].rotation_euler = (0, 0, 0)\
if faces_exist[0]:
    len_x[0] = bpy.data.objects["face0"].dimensions.x
    len_y[0] = bpy.data.objects["face0"].dimensions.z

# Bottom
#bpy.data.objects["face1"].rotation_euler = (0, 0, 0)
if faces_exist[1]:
    len_x[1] = bpy.data.objects["face1"].dimensions.x
    len_y[1] = bpy.data.objects["face1"].dimensions.z

# Left
if faces_exist[2]:
    bpy.data.objects["face2"].rotation_euler = (0, radians(90), 0)
    len_x[2] = bpy.data.objects["face2"].dimensions.x
    len_z[3] = bpy.data.objects["face2"].dimensions.z

# Right
if faces_exist[3]:
    bpy.data.objects["face3"].rotation_euler = (0, radians(90), 0)
    len_x[3] = bpy.data.objects["face3"].dimensions.x
    len_z[2] = bpy.data.objects["face3"].dimensions.z

# Front
if faces_exist[4]:
    bpy.data.objects["face4"].rotation_euler = (0, 0, radians(90))
    len_y[2] = bpy.data.objects["face4"].dimensions.z
    len_z[0] = bpy.data.objects["face4"].dimensions.x

# Back
if faces_exist[5]:
    bpy.data.objects["face5"].rotation_euler = (0, 0, radians(90))
    len_y[3] = bpy.data.objects["face5"].dimensions.z
    len_z[1] = bpy.data.objects["face5"].dimensions.x

print('Koniec obracania')

val_x = max(len_x)
val_y = max(len_y)
val_z = max(len_z)

# Objętość
V = val_x * val_y * val_z

# Zapisywanie meshy
if faces_exist[0]:
    object = bpy.data.objects['face0']
    bpy.context.view_layer.objects.active = object
    bpy.ops.object.select_all(action='DESELECT')
    object.select_set(True)
    modifier = object.modifiers.new(name="Solidify", type='SOLIDIFY')
    modifier.thickness = val_x/2
    bpy.ops.object.modifier_apply(modifier="Solidify")

    modifier = object.modifiers.new(name="Mirror", type='MIRROR')
    modifier.use_axis[0] = False
    modifier.use_axis[1] = True
    bpy.ops.object.modifier_apply(modifier="Mirror")

    modifier = object.modifiers.new(name="Triangulate", type='TRIANGULATE')
    bpy.ops.object.modifier_apply(modifier="Triangulate")

    #object.location.z += val_x/2
    bpy.ops.export_scene.obj(filepath="./assets/obj/temp/meshes/top.obj", check_existing=False, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl", use_selection=True, use_animation=False, use_mesh_modifiers=True, use_edges=True, use_smooth_groups=False, use_smooth_groups_bitflags=False, use_normals=True, use_uvs=True, use_materials=True, use_triangles=False, use_nurbs=False, use_vertex_groups=False, use_blen_objects=True, group_by_object=False, group_by_material=False, keep_vertex_order=False, global_scale=1, path_mode='AUTO')

if faces_exist[1]:
    object = bpy.data.objects['face1']
    bpy.context.view_layer.objects.active = object
    bpy.ops.object.select_all(action='DESELECT')
    object.select_set(True)
    modifier = object.modifiers.new(name="Solidify", type='SOLIDIFY')
    modifier.thickness = val_x/2
    bpy.ops.object.modifier_apply(modifier="Solidify")

    modifier = object.modifiers.new(name="Mirror", type='MIRROR')
    modifier.use_axis[0] = False
    modifier.use_axis[1] = True
    bpy.ops.object.modifier_apply(modifier="Mirror")

    modifier = object.modifiers.new(name="Triangulate", type='TRIANGULATE')
    bpy.ops.object.modifier_apply(modifier="Triangulate")
    #object.location.z += val_x/2
    bpy.ops.export_scene.obj(filepath="./assets/obj/temp/meshes/bottom.obj", check_existing=False, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl", use_selection=True, use_animation=False, use_mesh_modifiers=True, use_edges=True, use_smooth_groups=False, use_smooth_groups_bitflags=False, use_normals=True, use_uvs=True, use_materials=True, use_triangles=False, use_nurbs=False, use_vertex_groups=False, use_blen_objects=True, group_by_object=False, group_by_material=False, keep_vertex_order=False, global_scale=1, path_mode='AUTO')

if faces_exist[2]:
    object = bpy.data.objects['face2']
    bpy.context.view_layer.objects.active = object
    bpy.ops.object.select_all(action='DESELECT')
    object.select_set(True)
    modifier = object.modifiers.new(name="Solidify", type='SOLIDIFY')
    modifier.thickness = val_x/2
    bpy.ops.object.modifier_apply(modifier="Solidify")

    modifier = object.modifiers.new(name="Mirror", type='MIRROR')
    modifier.use_axis[0] = False
    modifier.use_axis[1] = True
    bpy.ops.object.modifier_apply(modifier="Mirror")

    modifier = object.modifiers.new(name="Triangulate", type='TRIANGULATE')
    bpy.ops.object.modifier_apply(modifier="Triangulate")
    #object.location.y += val_y/2
    bpy.ops.export_scene.obj(filepath="./assets/obj/temp/meshes/left.obj", check_existing=False, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl", use_selection=True, use_animation=False, use_mesh_modifiers=True, use_edges=True, use_smooth_groups=False, use_smooth_groups_bitflags=False, use_normals=True, use_uvs=True, use_materials=True, use_triangles=False, use_nurbs=False, use_vertex_groups=False, use_blen_objects=True, group_by_object=False, group_by_material=False, keep_vertex_order=False, global_scale=1, path_mode='AUTO')

if faces_exist[3]:
    object = bpy.data.objects['face3']
    bpy.context.view_layer.objects.active = object
    bpy.ops.object.select_all(action='DESELECT')
    object.select_set(True)
    modifier = object.modifiers.new(name="Solidify", type='SOLIDIFY')
    modifier.thickness = val_x/2
    bpy.ops.object.modifier_apply(modifier="Solidify")

    modifier = object.modifiers.new(name="Mirror", type='MIRROR')
    modifier.use_axis[0] = False
    modifier.use_axis[1] = True
    bpy.ops.object.modifier_apply(modifier="Mirror")

    modifier = object.modifiers.new(name="Triangulate", type='TRIANGULATE')
    bpy.ops.object.modifier_apply(modifier="Triangulate")
    #object.location.y += val_y/2
    bpy.ops.export_scene.obj(filepath="./assets/obj/temp/meshes/right.obj", check_existing=False, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl", use_selection=True, use_animation=False, use_mesh_modifiers=True, use_edges=True, use_smooth_groups=False, use_smooth_groups_bitflags=False, use_normals=True, use_uvs=True, use_materials=True, use_triangles=False, use_nurbs=False, use_vertex_groups=False, use_blen_objects=True, group_by_object=False, group_by_material=False, keep_vertex_order=False, global_scale=1, path_mode='AUTO')

if faces_exist[4]:
    object = bpy.data.objects['face4']
    bpy.context.view_layer.objects.active = object
    bpy.ops.object.select_all(action='DESELECT')
    object.select_set(True)
    modifier = object.modifiers.new(name="Solidify", type='SOLIDIFY')
    modifier.thickness = val_x/2
    bpy.ops.object.modifier_apply(modifier="Solidify")
    
    modifier = object.modifiers.new(name="Mirror", type='MIRROR')
    modifier.use_axis[0] = False
    modifier.use_axis[1] = True
    bpy.ops.object.modifier_apply(modifier="Mirror")
    
    modifier = object.modifiers.new(name="Triangulate", type='TRIANGULATE')
    bpy.ops.object.modifier_apply(modifier="Triangulate")
    #object.location.x -= val_x/2
    bpy.ops.export_scene.obj(filepath="./assets/obj/temp/meshes/front.obj", check_existing=False, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl", use_selection=True, use_animation=False, use_mesh_modifiers=True, use_edges=True, use_smooth_groups=False, use_smooth_groups_bitflags=False, use_normals=True, use_uvs=True, use_materials=True, use_triangles=False, use_nurbs=False, use_vertex_groups=False, use_blen_objects=True, group_by_object=False, group_by_material=False, keep_vertex_order=False, global_scale=1, path_mode='AUTO')
    
if faces_exist[5]:
    object = bpy.data.objects['face5']
    bpy.context.view_layer.objects.active = object
    bpy.ops.object.select_all(action='DESELECT')
    object.select_set(True)
    modifier = object.modifiers.new(name="Solidify", type='SOLIDIFY')
    modifier.thickness = val_x/2
    bpy.ops.object.modifier_apply(modifier="Solidify")
    
    modifier = object.modifiers.new(name="Mirror", type='MIRROR')
    modifier.use_axis[0] = False
    modifier.use_axis[1] = True
    bpy.ops.object.modifier_apply(modifier="Mirror")
    
    modifier = object.modifiers.new(name="Triangulate", type='TRIANGULATE')
    bpy.ops.object.modifier_apply(modifier="Triangulate")
    #object.location.x -= val_x/2
    bpy.ops.export_scene.obj(filepath="./assets/obj/temp/meshes/back.obj", check_existing=False, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl", use_selection=True, use_animation=False, use_mesh_modifiers=True, use_edges=True, use_smooth_groups=False, use_smooth_groups_bitflags=False, use_normals=True, use_uvs=True, use_materials=True, use_triangles=False, use_nurbs=False, use_vertex_groups=False, use_blen_objects=True, group_by_object=False, group_by_material=False, keep_vertex_order=False, global_scale=1, path_mode='AUTO')
    