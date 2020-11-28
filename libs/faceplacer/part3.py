import os.path
from os import path
import pymesh

def make_path(p):
    p = os.path.expanduser(p)
    p = os.path.normpath(p)
    p = os.path.realpath(p)
    p = os.path.abspath(p)
    return p

path = './assets/obj/temp/fixed1/'
save_path = "./assets/obj/temp/fixed2/"
print("Files path: " + str(path))

names = ('top', 'bottom', 'left', 'right', 'front', 'bottom')

for x in range(0,5):
    try:
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-" + names[x] + "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        f = make_path(path + '/' + names[x] + '.obj')
        mesh = pymesh.load_mesh(f)
        print("Load ok")
        mesh, i = pymesh.remove_isolated_vertices(mesh)
        print("Remove isolated ok")
        mesh, i = pymesh.remove_duplicated_faces(mesh)
        print("Remove isolated ok")
        mesh, i = pymesh.remove_duplicated_vertices(mesh, 2)
        print("Remove duplicated ok")
        mesh = pymesh.subdivide(mesh, order=2, method="loop")
        print("Subdivide ok")

        s = make_path(save_path + '/' + names[x] + '.obj')
        print("Saving path: " + s)
        pymesh.save_mesh(s, mesh, ascii=True)
        with open(s, 'r') as original: data = original.read()
        with open(s, 'w') as modified: modified.write("o Export\n" + data)
    except:
        print("Missing file")