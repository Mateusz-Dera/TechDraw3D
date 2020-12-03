# Mateusz Dera

import os.path
from os import path
import pymesh

def make_path(p):
    p = os.path.expanduser(p)
    p = os.path.normpath(p)
    p = os.path.realpath(p)
    p = os.path.abspath(p)
    return p

path = './tmp'
save_path = "./export"
print("Files path: " + str(path))

names = ('top', 'bottom', 'left', 'right', 'front', 'bottom')

top = None
bottom = None
right = None
left = None
front = None
back = None

for x in range(0,5):
    try:
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-" + names[x] + "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        f = make_path(path + '/' + names[x] + '.obj')
        mesh = pymesh.load_mesh(f)

        if x == 0:
            top = mesh
        elif x == 1:
            bottom = mesh
        elif x == 2:
            right = mesh
        elif x == 3:
            left = mesh
        elif x == 4:
            front = mesh
        elif x == 5:
            back = mesh
    except:
        print("File is missing") 

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

a, info = pymesh.remove_isolated_vertices(a)
b, info = pymesh.remove_isolated_vertices(b)
c, info = pymesh.remove_isolated_vertices(c)

a, info = pymesh.remove_duplicated_faces(a)
b, info = pymesh.remove_duplicated_faces(b)
c, info = pymesh.remove_duplicated_faces(c)

if a == None and b == None and c == None:
    print('No mesh to convert')
    exit()

elif a != None and b != None and c != None:
    a = pymesh.boolean(a, c, operation="intersection")
   # a = pymesh.boolean(b, a, operation="intersection")

elif a != None and b != None and c == None:
    a = pymesh.boolean(a, b, operation="intersection")

elif a != None and b == None and c != None:
    a = pymesh.boolean(a, c, operation="intersection")

if a == None and b != None and c != None:
    a = pymesh.boolean(b, c, operation="intersection")

pymesh.save_mesh(save_path + "/mesh.obj", a, ascii=True);

print('Koniec')