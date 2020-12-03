import bpy
import os.path
from os import path
from math import radians
import sys

path = str(sys.argv[3])[:-7] + "tmp/"
export_path = str(sys.argv[3])[:-7] + "export/"

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

a = None
b = None
c = None 

# Top
if faces_exist[0]:
    a = bpy.data.objects[names[0]]
# Bottom
elif faces_exist[1]:
    
    a = bpy.data.objects[names[1]]

# Left
if faces_exist[2]:
    b = bpy.data.objects[names[2]]
# Right
elif faces_exist[3]:
    b = bpy.data.objects[names[3]]

# Front
if faces_exist[4]:
    c = bpy.data.objects[names[4]]
# Back
elif faces_exist[5]:
    c = bpy.data.objects[names[5]]

if a != None:
    print(a.name)

if b != None:
    print(b)

if c != None:
    print(c)

