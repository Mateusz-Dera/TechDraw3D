# Mateusz Dera

import bpy
import os.path
from os import path
from math import radians

faces_path = ('./assets/obj/temp/fixed1/top.obj','./assets/obj/temp/fixed1/bottom.obj','./assets/obj/temp/fixed1/left.obj','./assets/obj/temp/fixed1/right.obj','./assets/obj/temp/fixed1/front.obj','./assets/obj/temp/fixed1/back.obj')
faces_exist = (path.exists(faces_path[0]), path.exists(faces_path[1]), path.exists(faces_path[2]), path.exists(faces_path[3]), path.exists(faces_path[4]), path.exists(faces_path[5]))

# Czyszczenie sceny ze wszystkich domyślnie ładowanych obiektów
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False, confirm=False)

for i in range(0,6):
    if faces_exist[i] == True:
        bpy.ops.import_scene.obj(filepath=faces_path[i])
        for obj in bpy.context.selected_objects:
            obj.name = "face" + str(i)
            obj.data.name = "face" + str(i)
    print("face" + str(i))

top = None
bottom = None
left = None
right = None
front = None
back = None

if faces_exist[0]:
    top = bpy.data.objects['face0']
    print('top')
    
if faces_exist[1]:
    bottom = bpy.data.objects['face1']
    print('bottom')

if faces_exist[2]:
    left = bpy.data.objects['face2']
    print('left')

if faces_exist[3]:
    right = bpy.data.objects['face3']
    print('right')

# if faces_exist[4]:
#     front = bpy.data.objects['face4']
#     print('front')

# if faces_exist[5]:
#     back = bpy.data.objects['face5']
#     print('back')


a = None
b = None
c = None

if top != None:
    a = top
elif bottom != None:
    a = bottom

if left != None:
    b = left
elif right != None:
    b = right

if front != None:
    c = front
elif back != None:
    c = back

if(a != None):
    print("A")

if(b != None):
    print("B")

if(c != None):
    print("C")

#if a != None:

bpy.context.view_layer.objects.active = a
bpy.ops.object.select_all(action='DESELECT')
a.select_set(True)

modifier = a.modifiers.new(name="Boolean", type='BOOLEAN')
modifier.operation = 'INTERSECT'
modifier.object = b
bpy.ops.object.modifier_apply(modifier="Boolean")

bpy.context.view_layer.objects.active = b
bpy.ops.object.select_all(action='DESELECT')
b.select_set(True)
bpy.ops.object.delete() 

bpy.context.view_layer.objects.active = a
bpy.ops.object.select_all(action='DESELECT')
a.select_set(True)

from pathlib import Path

context = bpy.context
scene = context.scene
viewlayer = context.view_layer


obs = [o for o in scene.objects if o.type == 'MESH']
bpy.ops.object.select_all(action='DESELECT')    

path = Path("/home/mdera/TechDraw3D/")
for ob in obs:
    viewlayer.objects.active = ob
    ob.select_set(True)
    stl_path = path / f"{ob.name}.stl"
    bpy.ops.export_mesh.stl(
            filepath=str(stl_path),
            use_selection=True)
    ob.select_set(False)