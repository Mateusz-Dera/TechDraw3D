# TechDraw3D
# Copyright © 2020-2021 Tomasz Nowak, Mateusz Dera, Jakub Schwarz

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

from os import listdir
from os.path import isfile, join

from svgpathtools import Path

def assets_type(type="simple"):
    """ Return a path to assets folder

    Keyword arguments:
    type -- string argument (accespted arguments: simple, advanced)

    Return:
    list of files path
    """
    paths = [
        "./test/assets/simple/",
        "./test/assets/advanced/"
    ]

    if type == "simple":
        onlyfiles = [f for f in listdir(paths[0]) if isfile(join(paths[0], f))]

    if len(onlyfiles)>0:
        onlyfiles = [join(paths[0], elem) for elem in onlyfiles]

    return onlyfiles

def get_specified_paths(paths, extension='.svg'):
    """ Return a path to assets folder

    Keyword arguments:
    paths -- list of files paths
    extension -- string argument, specified a filter extension

    Return:
    list of filtered files path
    """
    return [k for k in paths if extension in k]

def svg_compare_path(example_paths, tested_paths):
    for path in example_paths:
        tested_path = [tested_path for tested_path in tested_paths if tested_path.start == path.start and tested_path.end == path.end]

        if len(tested_path) != 1:
            raise AssertionError("SVG walls is not equal")

def get_assets_from_directory(path):
    """ Return a list of assets from directory 
    Keyword arguments:
    path -- assets directory

    Return 
    list of assets in path directory
    """

    return [join(path, elem) for elem in [f for f in listdir(path) if isfile(join(path, f))]]