import os.path
from os import path
import pymesh

def make_path(p):
    p = os.path.expanduser(p)
    p = os.path.normpath(p)
    p = os.path.realpath(p)
    p = os.path.abspath(p)
    return p

path = './assets/obj/temp/meshes/'
save_path = "./assets/obj/temp/fixed1/"
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

output_mesh = None

if a != None and b != None and c != None:
    output_mesh = pymesh.boolean(a, c, operation="intersection")

if a != None and b != None and c == None:
    output_mesh = pymesh.boolean(a, b, operation="intersection")

if a != None and b == None and c != None:
    output_mesh = pymesh.boolean(a, c, operation="intersection")

if a == None and b != None and c != None:
    output_mesh = pymesh.boolean(b, c, operation="intersection")

print("OK")

pymesh.save_mesh("./assets/obj/export/export.obj", output_mesh, ascii=True);

with open('./assets/obj/export/export.obj', 'r') as original: data = original.read()
with open('./assets/obj/export/export.obj', 'w') as modified: modified.write("o Export\n" + data)

print('Koniec')