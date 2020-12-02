import bpy
import sys
import os

print("Start")

path = str(sys.argv[3])[:-7] + "tmp/"
export_path = str(sys.argv[3])[:-7] + "export/"

print("Import path: " + path)
print("Export path: " + export_path)

for filename in os.listdir(path):
    if filename.endswith(".svg"):
        print('\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n' + str(path) + '\n' + str(filename) + '\n')

        objs = bpy.data.objects
        for ob in objs:
            objs.remove(objs[ob.name], do_unlink=True)

        # Import
        bpy.ops.import_curve.svg(filepath=str(path) + str(filename))
        
        # Select all curves (lines)
        for o in bpy.data.objects:
            o.select_set(True)
            bpy.context.view_layer.objects.active = o

        # Scale * 100
        bpy.ops.transform.resize(value=(100, 100, 100), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

        # Join all curves (lines) 
        bpy.ops.object.join()

        # Select all curves (lines)
        for o in bpy.data.objects:
            o.select_set(True)
            bpy.context.view_layer.objects.active = o

        # Convert curve to outline mesh
        bpy.ops.object.convert(target='MESH')

        # Select outline mesh
        for o in bpy.data.objects:
            o.select_set(True)
            bpy.context.view_layer.objects.active = o

        # Switch to edit mode
        bpy.ops.object.editmode_toggle()

        # Select all edges
        bpy.ops.mesh.select_all(action='SELECT')

        # Remove doubles 
        bpy.ops.mesh.remove_doubles()

        # Select all edges
        bpy.ops.mesh.select_all(action='SELECT')
        
        # Create faces
        #for i in range (0,100):
        #    bpy.ops.mesh.fill()
        bpy.ops.mesh.edge_face_add()

        # Select all edges
        bpy.ops.mesh.select_all(action='SELECT')

        # Move mesh to center
        bpy.ops.object.origin_set(type="GEOMETRY_ORIGIN")

        # Debug print list of objects
        for ob in objs:
            print(ob.name)

        # Export
        bpy.ops.export_scene.obj(filepath=export_path + filename[:-4] + ".obj", check_existing=False, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl", use_selection=True, use_animation=False, use_mesh_modifiers=True, use_edges=True, use_smooth_groups=False, use_smooth_groups_bitflags=False, use_normals=True, use_uvs=True, use_materials=True, use_triangles=False, use_nurbs=False, use_vertex_groups=False, use_blen_objects=True, group_by_object=False, group_by_material=False, keep_vertex_order=False, global_scale=1, path_mode='AUTO')


        
