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
from libs.extruder.dwginput import DWGInput
from libs.extruder.dxfinput import DXFInput
from libs.extruder.svg import SVG
from test import tools

from svgpathtools import svg2paths
from sys import platform
from filecmp import cmp, clear_cache
import pytest
import os
import subprocess
from os.path import isfile
from time import sleep


class TestMakeOBJ():
    dwg_objects = tools.get_assets_from_directory("./test/assets/advanced/")



    @pytest.mark.parametrize('dwg_path', dwg_objects)
    def test_make_obj(self, dwg_path):
        pass
        # input_file = dwg_path
        # output_file = "./test/assets/advanced_obj/" + os.path.basename(str(dwg_path))[:-4] + ".obj"
        
        # dwg = DWGInput()
        # input_file = dwg.dwg2dxf_converter(input_file, False)

        # dxf = DXFInput()
        # svg = SVG(dxf.dxf2svg_converter(input_file, False))
        # svg.split_svg()
        # svg.save_walls()

        # def make_obj():
        #     process = subprocess.Popen(['sh', "./libs/mesher/face/run.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #     out, err = process.communicate()
        #     process.wait()

        #     process = subprocess.Popen(['sh', "./libs/mesher/extrude/run.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #     out, err = process.communicate()
        #     process.wait()
        
        #     process = subprocess.Popen(['sh', "./libs/mesher/boolean/run.sh", '-obj', output_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #     out, err = process.communicate()
        #     process.wait()

        # make_obj()

        # assert isfile(output_file)