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
from ...libs.extruder.svg import SVG
from . import file_loader

import pytest
import os


class TestSVG:
    """{"x": 0, "y": 0}
    """
    paths = [k for k in file_loader.assets_type("simple") if '.svg' in k]

    @pytest.mark.parametrize('path', paths)
    def test_valid(self, path):
        """
        Walidacja danych
        """
        
        if not isinstance(path, str):
            raise TypeError('Wrong type')
        if os.path.exists(path) is False:
            assert "Path not exist"
        if os.path.isfile(path) is False:
            assert "File is not file"

    @pytest.mark.parametrize('path', paths)
    def test_init_svg(self, path):
        obj = SVG(path)

        if not isinstance(obj, SVG):
            raise TypeError('Wrong type')
        
        assert obj.svg_xy_center == {"x": 0, "y": 0}

    @pytest.mark.parametrize('path', paths)
    def test_split_svg(self, path):
        obj = SVG(path)

        obj.split_svg()

        assert obj.svg_front
        assert obj.svg_right
        assert obj.svg_top
        assert obj.svg_3d

        assert isinstance(obj.svg_front, list)
        assert isinstance(obj.svg_right, list)
        assert isinstance(obj.svg_top, list)
        assert isinstance(obj.svg_3d, list)