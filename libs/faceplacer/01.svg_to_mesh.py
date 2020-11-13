import bpy 
import os
import sys
from os import path

def make_path(p):
    p = os.path.expanduser(p)
    p = os.path.normpath(p)
    p = os.path.realpath(p)
    p = os.path.abspath(p)
    return p

top_path = make_path("assets/svg/temp/walls/top.svg")
bottom_path = make_path("assets/svg/temp/walls/bottom.svg")
left_path = make_path("assets/svg/temp/walls/left.svg")
right_path = make_path("assets/svg/temp/walls/right.svg")
front_path = make_path("assets/svg/temp/walls/front.svg")
back_path = make_path("assets/svg/temp/walls/back.svg")

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False, confirm=False)

export_path = back_path = make_path('assets/obj/temp/faces/')
if path.exists(export_path):
    print('Export path is correct')
else:
    print('Missing export path ' + export_path)
    exit()

end = '\n\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n'
print(end)

def footer(n,p):
    print('Converting SVG ' + str(n) + ' face to MESH\n' + str(p) + end)

if path.isfile(top_path) == True:
    name = 'top'
    footer(name, top_path)
    bpy.ops.import_curve.svg(filepath=top_path)
    bpy.ops.object.select_all(action='SELECT')
    
    for o in bpy.data.objects:
        o.select_set(True)
        bpy.context.view_layer.objects.active = o
    
    bpy.ops.object.join()

    bpy.ops.object.select_all(action='SELECT')

    bpy.ops.object.convert(target='MESH')

    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.remove_doubles()
    bpy.ops.mesh.edge_face_add()

    #bpy.ops.object.origin_set(type="GEOMETRY_ORIGIN")
    bpy.ops.export_scene.obj(filepath=export_path+"/" + name + ".obj", check_existing=False, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl", use_selection=True, use_animation=False, use_mesh_modifiers=True, use_edges=True, use_smooth_groups=False, use_smooth_groups_bitflags=False, use_normals=True, use_uvs=True, use_materials=True, use_triangles=False, use_nurbs=False, use_vertex_groups=False, use_blen_objects=True, group_by_object=False, group_by_material=False, keep_vertex_order=False, global_scale=1, path_mode='AUTO')
    for item in bpy.data.meshes:
        bpy.data.meshes.remove(item)

if path.isfile(bottom_path) == True:
    name = 'bottom'
    footer(name, bottom_path)
    bpy.ops.import_curve.svg(filepath=bottom_path)
    bpy.ops.object.select_all(action='SELECT')
    
    for o in bpy.data.objects:
        o.select_set(True)
        bpy.context.view_layer.objects.active = o
    
    bpy.ops.object.join()

    bpy.ops.object.select_all(action='SELECT')

    bpy.ops.object.convert(target='MESH')

    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.remove_doubles()
    bpy.ops.mesh.edge_face_add()

    #bpy.ops.object.origin_set(type="GEOMETRY_ORIGIN")
    bpy.ops.export_scene.obj(filepath=export_path+"/" + name + ".obj", check_existing=False, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl", use_selection=True, use_animation=False, use_mesh_modifiers=True, use_edges=True, use_smooth_groups=False, use_smooth_groups_bitflags=False, use_normals=True, use_uvs=True, use_materials=True, use_triangles=False, use_nurbs=False, use_vertex_groups=False, use_blen_objects=True, group_by_object=False, group_by_material=False, keep_vertex_order=False, global_scale=1, path_mode='AUTO')
    for item in bpy.data.meshes:
        bpy.data.meshes.remove(item)

if path.isfile(left_path) == True:
    name = 'left'
    footer(name, left_path)
    bpy.ops.import_curve.svg(filepath=left_path)
    bpy.ops.object.select_all(action='SELECT')
    
    for o in bpy.data.objects:
        o.select_set(True)
        bpy.context.view_layer.objects.active = o
    
    bpy.ops.object.join()

    bpy.ops.object.select_all(action='SELECT')

    bpy.ops.object.convert(target='MESH')

    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.remove_doubles()
    bpy.ops.mesh.edge_face_add()

    #bpy.ops.object.origin_set(type="GEOMETRY_ORIGIN")
    bpy.ops.export_scene.obj(filepath=export_path+"/" + name + ".obj", check_existing=False, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl", use_selection=True, use_animation=False, use_mesh_modifiers=True, use_edges=True, use_smooth_groups=False, use_smooth_groups_bitflags=False, use_normals=True, use_uvs=True, use_materials=True, use_triangles=False, use_nurbs=False, use_vertex_groups=False, use_blen_objects=True, group_by_object=False, group_by_material=False, keep_vertex_order=False, global_scale=1, path_mode='AUTO')
    for item in bpy.data.meshes:
        bpy.data.meshes.remove(item)

if path.isfile(right_path) == True:
    name = 'right'
    footer(name, right_path)
    bpy.ops.import_curve.svg(filepath=right_path)
    bpy.ops.object.select_all(action='SELECT')
    
    for o in bpy.data.objects:
        o.select_set(True)
        bpy.context.view_layer.objects.active = o
    
    bpy.ops.object.join()

    bpy.ops.object.select_all(action='SELECT')

    bpy.ops.object.convert(target='MESH')

    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.remove_doubles()
    bpy.ops.mesh.edge_face_add()

    #bpy.ops.object.origin_set(type="GEOMETRY_ORIGIN")
    bpy.ops.export_scene.obj(filepath=export_path+"/" + name + ".obj", check_existing=False, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl", use_selection=True, use_animation=False, use_mesh_modifiers=True, use_edges=True, use_smooth_groups=False, use_smooth_groups_bitflags=False, use_normals=True, use_uvs=True, use_materials=True, use_triangles=False, use_nurbs=False, use_vertex_groups=False, use_blen_objects=True, group_by_object=False, group_by_material=False, keep_vertex_order=False, global_scale=1, path_mode='AUTO')
    for item in bpy.data.meshes:
        bpy.data.meshes.remove(item)

if path.isfile(front_path) == True:
    name = 'front'
    footer(name, front_path)
    bpy.ops.import_curve.svg(filepath=front_path)
    bpy.ops.object.select_all(action='SELECT')
    
    for o in bpy.data.objects:
        o.select_set(True)
        bpy.context.view_layer.objects.active = o
    
    bpy.ops.object.join()

    bpy.ops.object.select_all(action='SELECT')

    bpy.ops.object.convert(target='MESH')

    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.remove_doubles()
    bpy.ops.mesh.edge_face_add()

    #bpy.ops.object.origin_set(type="GEOMETRY_ORIGIN")
    bpy.ops.export_scene.obj(filepath=export_path+"/" + name + ".obj", check_existing=False, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl", use_selection=True, use_animation=False, use_mesh_modifiers=True, use_edges=True, use_smooth_groups=False, use_smooth_groups_bitflags=False, use_normals=True, use_uvs=True, use_materials=True, use_triangles=False, use_nurbs=False, use_vertex_groups=False, use_blen_objects=True, group_by_object=False, group_by_material=False, keep_vertex_order=False, global_scale=1, path_mode='AUTO')
    for item in bpy.data.meshes:
        bpy.data.meshes.remove(item)

if path.isfile(back_path) == True:
    name = 'back'
    footer(name, back_path)
    bpy.ops.import_curve.svg(filepath=back_path)
    bpy.ops.object.select_all(action='SELECT')
    
    for o in bpy.data.objects:
        o.select_set(True)
        bpy.context.view_layer.objects.active = o
    
    bpy.ops.object.join()

    bpy.ops.object.select_all(action='SELECT')

    bpy.ops.object.convert(target='MESH')

    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.remove_doubles()
    bpy.ops.mesh.edge_face_add()

    #bpy.ops.object.origin_set(type="GEOMETRY_ORIGIN")
    bpy.ops.export_scene.obj(filepath=export_path+"/" + name + ".obj", check_existing=False, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl", use_selection=True, use_animation=False, use_mesh_modifiers=True, use_edges=True, use_smooth_groups=False, use_smooth_groups_bitflags=False, use_normals=True, use_uvs=True, use_materials=True, use_triangles=False, use_nurbs=False, use_vertex_groups=False, use_blen_objects=True, group_by_object=False, group_by_material=False, keep_vertex_order=False, global_scale=1, path_mode='AUTO')
    for item in bpy.data.meshes:
        bpy.data.meshes.remove(item)

print('End of SVG2MESH')