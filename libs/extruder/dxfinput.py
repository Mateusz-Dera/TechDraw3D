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

from sys import platform
import logging
import os.path
from dxf2svg.pycore import save_svg_from_dxf, extract_all
from libs.base import makepath

# My modules
from svgpathtools import svg2paths, svg2paths2, wsvg
import io

_logger = logging.getLogger(__name__)

class DXFInput():
    
    def dxf2svg_converter(self, name):
        dxffilepath = makepath.make_path(name)
        svgfilesize = 300

        svgfilepath_windows = makepath.make_path(".\\assets\\svg\\") + "\\" + os.path.basename(dxffilepath)[:-4] + ".svg"
        svgfilepath_linux = "./assets/svg/" + os.path.basename(dxffilepath)[:-4] + ".svg"

        if platform == "win32":
            print ("WINDOWS")
            print ("DXF file path:", dxffilepath)
            print ("SVG file path:", svgfilepath_windows)
            save_svg_from_dxf(dxffilepath, svgfilepath=svgfilepath_windows, frame_name=None, size=svgfilesize) 

        if platform == "linux":
            print ("LINUX")
            print ("DXF file path:", dxffilepath)
            print ("SVG file path:", svgfilepath_linux)

            if not os.path.exists(os.path.dirname(svgfilepath_linux)):
                os.mkdir(os.path.dirname(svgfilepath_linux))

            if not os.path.exists(svgfilepath_linux):
                io.open(svgfilepath_linux, mode='x', encoding='utf-8').close()

            save_svg_from_dxf(dxffilepath, svgfilepath=svgfilepath_linux, frame_name=None, size=svgfilesize)
