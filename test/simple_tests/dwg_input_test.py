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
from test import tools

from svgpathtools import svg2paths
from sys import platform
from filecmp import cmp, clear_cache
import pytest
import os


class TestDWGInput():
    paths_dwg = tools.get_specified_paths(tools.assets_type("simple"), '.dwg')
    paths_dxf = tools.get_specified_paths(tools.assets_type("simple"), '.dxf')
    paths_svg = tools.get_specified_paths(tools.assets_type("simple"), '.svg')

    @pytest.fixture()
    def dwg_input(self):
        return DWGInput()
    
    @pytest.fixture()
    def dxf_input(self):
        return DXFInput()

    @pytest.mark.parametrize('path', paths_dwg + paths_svg)
    def test_valid_dwg(self, path):
        """
        Walidacja danych
        """

        if not isinstance(path, str):
            raise TypeError('Wrong type')
        if os.path.exists(path) is False:
            raise "Path not exist"
        if os.path.isfile(path) is False:
            raise "File is not file"

    @pytest.mark.parametrize('dwg_path, svg_path', [(paths_dwg, paths_svg)])
    def test_convertdwg(self, dwg_input, dxf_input, dwg_path, svg_path):
        if platform == "win32":
            for dwg in dwg_path:
                svg = "./assets/svg/" + os.path.basename(dwg)[:-4] + ".svg"

                dwg_input.dwg2svg_converter(dwg)
                
                clear_cache()
                assert cmp(svg, './test/assets/simple/' + os.path.basename(dwg)[:-4] + ".svg")
        if platform == "linux":                
            for dwg in dwg_path:
                dxf = "./assets/dxf/" + os.path.basename(dwg)[:-4] + ".dxf"
                svg = "./assets/svg/" + os.path.basename(dwg)[:-4] + ".svg"

                dwg_input.dwg2dxf_converter(dwg)
                # dxf_input.dxf2svg_converter(dxf)
                
                clear_cache()
                assert cmp(dxf, './test/assets/simple/' + os.path.basename(dwg)[:-4] + ".dxf")

    @pytest.mark.parametrize('dwg_path, dxf_path', [(paths_dwg, paths_dxf)])
    def test_convert_dwg2svg(self, dwg_input, dwg_path, dxf_path):
        for dwg in dwg_path:
            dxf = "./assets/dxf/" + os.path.basename(dwg)[:-4] + ".dxf"
            dwg_input.dwg2dxf_converter(dwg)
            
            clear_cache()
            assert cmp(dxf, './test/assets/simple/' + os.path.basename(dwg)[:-4] + ".dxf", shallow=True)
            