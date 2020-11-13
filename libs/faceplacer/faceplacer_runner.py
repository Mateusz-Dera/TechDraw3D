import subprocess

def _get_blender():
    pass

def run_faceplacer():
    blender_path = _get_blender()


    process = subprocess.Popen(["blender", "-b", "--python",  "/home/jschwarz/Projekty/Prywatne/TechDraw3D/libs/faceplacer/part0.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    
    process = subprocess.Popen(["blender", "-b", "--python",  "/home/jschwarz/Projekty/Prywatne/TechDraw3D/libs/faceplacer/part1.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    
    process = subprocess.Popen(["blender", "-b", "--python",  "/home/jschwarz/Projekty/Prywatne/TechDraw3D/libs/faceplacer/part1.5.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()

    import os.path
    from os import path
    import pymesh

    meshes_path = ('./assets/obj/temp/meshes/top.obj','./assets/obj/temp/meshes/bottom.obj','./assets/obj/temp/meshes/left.obj','./assets/obj/temp/meshes/right.obj','./assets/obj/temp/meshes/front.obj','./assets/obj/temp/meshes/back.obj')
    meshes_exist = (path.exists(meshes_path[0]), path.exists(meshes_path[1]), path.exists(meshes_path[2]), path.exists(meshes_path[3]), path.exists(meshes_path[4]), path.exists(meshes_path[5]))

    if meshes_exist[0] == True:
        top = pymesh.load_mesh(meshes_path[0])
        print("top")

    if meshes_exist[1] == True:
        bottom = pymesh.load_mesh(meshes_path[1])
        print("bottom")

    if meshes_exist[2] == True:
        left = pymesh.load_mesh(meshes_path[2])
        print("left")

    if meshes_exist[3] == True:
        right = pymesh.load_mesh(meshes_path[3])
        print("right")

    if meshes_exist[4] == True:
        front = pymesh.load_mesh(meshes_path[4])
        print("front")

    if meshes_exist[5] == True:
        back = pymesh.load_mesh(meshes_path[5])
        print("front")

    a = None
    b = None
    c = None

    if meshes_exist[0]:
        a = top
    elif meshes_exist[1]:
        a = bottom

    if meshes_exist[2]:
        b = left
    elif meshes_exist[3]:
        b = right

    if meshes_exist[4]:
        c = front
    elif meshes_exist[5]:
        c = back

    output_mesh = None

    if a != None and b != None and c != None:
        #x = pymesh.boolean(b, c, operation="intersection")
        output_mesh = pymesh.boolean(a, c, operation="intersection")

    if a != None and b != None and c == None:
        output_mesh = pymesh.boolean(a, b, operation="intersection")

    if a != None and b == None and c != None:
        output_mesh = pymesh.boolean(a, c, operation="intersection")

    if a == None and b != None and c != None:
        output_mesh = pymesh.boolean(b, c, operation="intersection")

    import pdb; pdb.set_trace()

    pymesh.save_mesh("./assets/obj/export/export.obj", output_mesh, ascii=True);

    with open('./assets/obj/export/export.obj', 'r') as original: data = original.read()
    with open('./assets/obj/export/export.obj', 'w') as modified: modified.write("o Export\n" + data)

if __name__ == '__main__':
    run_faceplacer()