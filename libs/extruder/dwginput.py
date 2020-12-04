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

# Libs
from sys import platform
import logging
import subprocess
import os.path
from libs.base import makepath

# My modules
from svgpathtools import svg2paths, svg2paths2, wsvg

_logger = logging.getLogger(__name__)

class DWGInput():
    DWG = ""

    # Wrapper do LibreDWG / dwg2SVG.
    def dwg2svg_converter(self, name):

        dwg2svg_windows = ".\\tools\\LibreDWG\\dwg2SVG.exe"
        dwg2svg_linux = "dwg2SVG"
        parameters = "--mspace"

        dwgfilepath = makepath.make_path(name)
        svgfilepath_windows = ".\\assets\\svg\\" + os.path.basename(dwgfilepath)[:-4] + ".svg"
        svgfilepath_linux = "./assets/svg/" + os.path.basename(dwgfilepath)[:-4] + ".svg"

        # Wybór platformy.
        if platform == "win32":
            print ("WINDOWS")
            print ("DWG file path:", dwgfilepath)
            print ("SVG file path:", svgfilepath_windows)
            subprocess.Popen([dwg2svg_windows, parameters, dwgfilepath, '>', svgfilepath_windows], shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

        if platform == "linux":
            print ("LINUX")
            print ("DWG file path: ", dwgfilepath)
            print ("SVG file path: ", svgfilepath_linux)
            subprocess.call([dwg2svg_linux + ' ' + parameters + ' ' + dwgfilepath + ' > ' + svgfilepath_linux], shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    
    # Wrapper do LibreDWG / dwg2dxf.

    # TODO: Zapisywanie do folderu assets/dxf!
    
    def dwg2dxf_converter(self, name):

        dwg2dxf_windows = makepath.make_path(".\\tools\\LibreDWG\\dwg2dxf.exe")
        dwg2dxf_linux = "dwg2dxf"
        parameter1 = "-m"
        parameter2 = "-o"

        dwgfilepath = makepath.make_path(name)
        dxffilepath_windows = makepath.make_path(".\\assets\\dxf\\") + "\\" + os.path.basename(dwgfilepath)[:-4] + ".dxf"
        dxffilepath_linux = "./assets/dxf/" + os.path.basename(dwgfilepath)[:-4] + ".dxf"

        # Wybór platformy.
        if platform == "win32":
            print ("WINDOWS")
            print ("DWG file path:", dwgfilepath)
            print ("DXF file path:", dxffilepath_windows)
            print (dwg2dxf_windows, parameter1, parameter2, dxffilepath_windows, dwgfilepath)
            subprocess.Popen([dwg2dxf_windows, parameter1, parameter2, dxffilepath_windows, dwgfilepath], shell=True)

        if platform == "linux":
            print ("LINUX")
            print ("DWG file path: ", dwgfilepath)
            print ("DXF file path: ", dxffilepath_linux)
            subprocess.call([dwg2dxf_linux + ' ' + parameter1 + ' ' + parameter2 + ' ' + dxffilepath_linux + ' ' + dwgfilepath], shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

    def returnSVG(self):
        f = open('data/returned/footer.svg', 'x')
        f.write(str(self.DWG))
        f.close()
        # return DWG