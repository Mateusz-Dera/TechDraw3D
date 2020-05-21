#Mateusz Dera
#'C:\Program Files\Blender Foundation\Blender 2.82\blender.exe' -b --python main.py

import bpy
import os.path
from os import path
from math import radians

faces_path = ('./faces/top.obj','./faces/bottom.obj','./faces/left.obj','./faces/right.obj','./faces/front.obj','./faces/back.obj')
faces_exist = (path.exists(faces_path[0]), path.exists(faces_path[1]), path.exists(faces_path[2]), path.exists(faces_path[3]), path.exists(faces_path[4]), path.exists(faces_path[5]))

print('Detected faces:')
print ('(Top, Bottom, Left, Right, Front, Back)')
print (str(faces_exist))

#Czyszczenie sceny ze wszystkich domyślnie ładowanych obiektów
bpy.ops.wm.read_factory_settings(use_empty=True)

#Sprawdzenie czy istnieją co najmniej 2 rzuty z różnych perspektyw
x = int(faces_exist[0]) + int(faces_exist[1])
y = int(faces_exist[2]) + int(faces_exist[3])
z = int(faces_exist[4]) + int(faces_exist[5])

# print("X faces:" + str(x))
# print("Y faces:" + str(y))
# print("Z faces:" + str(z))

if x > 0:
   x = 1

if y > 0:
   y = 1

if z > 0:
   z = 1

if x + y + z < 2:
   print("Missing dimensions!")
   exit()

#Import ściany
for i in range(0,6):
   if faces_exist[i] == True:
      bpy.ops.import_scene.obj(filepath=faces_path[i])
      for obj in bpy.context.selected_objects:
         obj.name = "face" + str(i)
         obj.data.name = "face" + str(i)

      print("face" + str(i))

#Rotacja ścian

#Top
#bpy.data.objects["face0"].rotation_euler = (0, 0, 0)\

#Bottom
#bpy.data.objects["face1"].rotation_euler = (0, 0, 0)

#Left
if faces_exist[2]:
   bpy.data.objects["face2"].rotation_euler = (0, radians(90), 0)
#Right
if faces_exist[3]:
   bpy.data.objects["face3"].rotation_euler = (0, radians(90), 0)
#Front
if faces_exist[4]:
   bpy.data.objects["face4"].rotation_euler = (0, 0, radians(90))
#Back
if faces_exist[5]:
   bpy.data.objects["face5"].rotation_euler = (0, 0, radians(-90))

#Przesunięcie ścian

len_x = [0,0,0,0]
len_y = [0,0,0,0]
len_z = [0,0,0,0]

len_x[0] = bpy.data.objects["face0"].dimensions.x
len_x[1] = bpy.data.objects["face1"].dimensions.x
len_x[2] = bpy.data.objects["face2"].dimensions.x
len_x[3] = bpy.data.objects["face3"].dimensions.x


len_y[0] = bpy.data.objects["face0"].dimensions.z
len_y[1] = bpy.data.objects["face1"].dimensions.z
len_y[2] = bpy.data.objects["face4"].dimensions.z
len_y[3] = bpy.data.objects["face5"].dimensions.z

len_z[0] = bpy.data.objects["face4"].dimensions.x
len_z[1] = bpy.data.objects["face5"].dimensions.x
len_z[2] = bpy.data.objects["face1"].dimensions.z
len_z[3] = bpy.data.objects["face2"].dimensions.z

val_x = max(len_x)
val_y = max(len_y)
val_z = max(len_z)

# print(str(val_x))
# print(str(val_y))
# print(str(val_z))

print('V=' + str(val_x * val_y * val_z))

#

bpy.data.objects['face0'].location.z += z
bpy.data.objects['face1'].location.z -= z

bpy.data.objects['face2'].location.y += y
bpy.data.objects['face3'].location.y -= y

bpy.data.objects['face4'].location.x += x
bpy.data.objects['face5'].location.x -= x
#Export obiektu
bpy.ops.export_scene.obj(filepath='./export.obj')
