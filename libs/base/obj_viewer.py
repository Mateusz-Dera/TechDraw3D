# TechDraw3D
# Copyright © 2020 Tomasz Nowak, Mateusz Dera, Jakub Schwarz

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import pyglet
from pyglet.window import key
import ratcave as rc
import sys 

if len(sys.argv) == 1:
    print("Brak argumentów. Podaj ścieżkę do pliku .obj.")
    exit(1)

filename = sys.argv[2]

# Wyszukiwanie "body name" pliku obj.
def get_body_name(file):
    with open(file) as search:
        for line in search:
            if line[0] == "o":
                return line[2:].rstrip()

# Ustawianie materiału - matowy szary.
def set_material(object):
    object.uniforms['diffuse'] = 0.5, 0.5, 0.5
    object.uniforms['ambient'] = 0.05, 0.05, 0.05
    object.uniforms['specular'] = 0.7, 0.7, 0.7

# Ładowanie pliku
def load_object(file):
    # Insert filename into WavefrontReader.
    file_reader = rc.WavefrontReader(file)
    # Create Mesh
    object = file_reader.get_mesh(get_body_name(file), position=(0, 0, 0), scale=1.0)
    set_material(object)
    return object
    
# Ustawienie pozycji kamery
def camera_position(x, y, z):
    scene.camera.position.x = x
    scene.camera.position.y = y
    scene.camera.position.z = z

# Wypisywanie pozycji camery.
def print_camera_position():
    print ("x: ", scene.camera.position.x)
    print ("y: ", scene.camera.position.y)
    print ("z: ", scene.camera.position.z)

# Reset pozycji obiektu.
def reset_meshes_rotation():
    object.rotation.x = 0
    object.rotation.y = 0
    object.rotation.z = 0

# Obracanie obiektu klawiszami.
def rotate_meshes(dt):
    rotation = 100
    if keys[key.W]:
        object.rotation.x -= rotation * dt 
    if keys[key.S]:
        object.rotation.x += rotation * dt 
    if keys[key.A]:
        object.rotation.y += rotation * dt 
    if keys[key.D]:
        object.rotation.y -= rotation * dt 
    if keys[key.Q]:
        object.rotation.z += rotation * dt 
    if keys[key.E]:
        object.rotation.z -= rotation * dt 
    if keys[key.R]:
        reset_meshes_rotation()

# Sterownie kamerą.
def move_camera(dt):
    camera_speed = 3
    if keys[key.LEFT]:
        scene.camera.position.x -= camera_speed * dt
        print_camera_position()
    if keys[key.RIGHT]:
        scene.camera.position.x += camera_speed * dt
        print_camera_position()
    if keys[key.UP]:
        scene.camera.position.y += camera_speed * dt
        print_camera_position()
    if keys[key.DOWN]:
        scene.camera.position.y -= camera_speed * dt
        print_camera_position()
    if keys[key.BRACKETLEFT]:
        scene.camera.position.z += camera_speed * dt
        print_camera_position()
    if keys[key.BRACKETRIGHT]:
        scene.camera.position.z -= camera_speed * dt
        print_camera_position()

window = pyglet.window.Window(resizable = True)
keys = key.KeyStateHandler()
window.set_caption("TechDraw3D")
window.push_handlers(keys)

object = load_object(filename)

scene = rc.Scene(meshes=[object])
scene.bgColor = 0.2, 0.2, 0.2
scene.light.position = 0, 0, 10
camera_position(0, 0, 1)

pyglet.clock.schedule(move_camera)
pyglet.clock.schedule(rotate_meshes)

@window.event
def on_draw():
    with rc.default_shader:
        scene.draw()

print_camera_position()
pyglet.app.run()