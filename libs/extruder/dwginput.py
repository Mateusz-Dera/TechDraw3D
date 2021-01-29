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

# Libs
from sys import platform
from svgpathtools import svg2paths, svg2paths2, wsvg
import logging
import subprocess
import os.path
import shutil
import io

# My modules
from libs.base import makepath


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

            if not os.path.exists(os.path.dirname(svgfilepath_linux)):
                os.mkdir(os.path.dirname(svgfilepath_linux))

            if not os.path.exists(svgfilepath_linux):
                io.open(os.path.basename(dwgfilepath)[:-4] + ".svg", mode='w', encoding='utf-8').close()

            subprocess.call([dwg2svg_linux + ' ' + parameters + ' ' + dwgfilepath + ' > ' + svgfilepath_linux], shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    
    def dwg2dxf_converter(self, input_file, output_file):
        dwg2dxf_windows = makepath.make_path(".\\tools\\LibreDWG\\dwg2dxf.exe")
        dwg2dxf_linux = "dwg2dxf"
        parameter1 = "-m -y"
        parameter2 = "-o"

        dwgfilepath = makepath.make_path(input_file)
        dxffilepath_windows = makepath.make_path(".\\assets\\dxf\\") + "\\" + os.path.basename(dwgfilepath)[:-4] + ".dxf"
        if not output_file:
            output_file = "./assets/dxf/" + os.path.basename(dwgfilepath)[:-4] + ".dxf"

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
            print ("DXF file path: ", output_file)

            if not os.path.exists(os.path.dirname(output_file)):
                os.mkdir(os.path.dirname(output_file))

            subprocess.call([dwg2dxf_linux + ' ' + parameter1 + ' ' + parameter2 + ' ' + output_file + ' ' + dwgfilepath], shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

            wait(10)
            return output_file