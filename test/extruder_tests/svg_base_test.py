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

from svgpathtools import Path, Line
import pytest
import os


class TestBasicSVG:
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

class TestSplitting():
    paths = [k for k in file_loader.assets_type("simple") if '.svg' in k]
    files = [
        "P001.svg",
        "P002.svg",
        "P003.svg",
        "P004.svg",
    ]

    svg_walls = {
        "P001.svg": [
            [   # FRONT
                Path(Line(start=(108.12986448542324+133.14512365063447j), end=(158.12986448542324+133.14512365063447j))), Path(Line(start=(158.12986448542324+83.14512365063447j), end=(158.12986448542324+133.14512365063447j))), Path(Line(start=(108.12986448542324+83.14512365063447j), end=(158.12986448542324+83.14512365063447j))), Path(Line(start=(108.12986448542324+83.14512365063447j), end=(108.12986448542324+133.14512365063447j)))
            ],
            [   # RIGHT
                Path(Line(start=(235.4000719894011+133.14512365063447j), end=(285.4000719894011+133.14512365063447j))), Path(Line(start=(285.4000719894011+83.14512365063447j), end=(285.4000719894011+133.14512365063447j))), Path(Line(start=(235.4000719894011+83.14512365063447j), end=(235.4000719894011+133.14512365063447j))), Path(Line(start=(235.4000719894011+83.14512365063447j), end=(285.4000719894011+83.14512365063447j)))
            ],
            [   # TOP
                Path(Line(start=(158.12986461589935+239.5109570544555j), end=(158.12986461589935+189.5109570544555j))), Path(Line(start=(108.12986461589935+239.5109570544555j), end=(158.12986461589935+239.5109570544555j))), Path(Line(start=(158.12986461589935+189.5109570544555j), end=(108.12986461589935+189.5109570544555j))), Path(Line(start=(108.12986461589935+189.5109570544555j), end=(108.12986461589935+239.5109570544555j)))
            ],
            [   # 3D
                Path(Line(start=(255.8547035732845+257.18017672415164j), end=(220.49936451396206+236.82039103453172j))), Path(Line(start=(291.21004263261784+236.8203910345381j), end=(255.8547035732845+257.18017672415164j))), Path(Line(start=(220.49936451396206+236.82039103453172j), end=(255.8547035732954+216.46060534491818j))), Path(Line(start=(255.8547035732954+216.46060534491818j), end=(291.21004263261784+236.8203910345381j))), Path(Line(start=(291.21004263261784+195.94303479241108j), end=(291.21004263261784+236.8203910345381j))), Path(Line(start=(220.49936451396206+195.94303479240472j), end=(255.8547035732954+175.58324910279117j))), Path(Line(start=(220.49936451396206+195.94303479240472j), end=(220.49936451396206+236.82039103453172j))), Path(Line(start=(255.8547035732954+175.58324910279117j), end=(291.21004263261784+195.94303479241108j))), Path(Line(start=(255.8547035732954+175.58324910279117j), end=(255.8547035732954+216.46060534491818j)))
            ]
        ],
        "P002.svg": [
        ],
        "P003.svg": [
        ],
        "P004.svg": [
        ]
    }

    @pytest.mark.parametrize('path', paths)
    def test_split_svg_square(self, path):
        obj = SVG(path)
        obj.split_svg()

        # import pdb; pdb.set_trace()
        # f = [file for file in self.files if file in self.paths[0]]

        # import pdb; pdb.set_trace()
        obj.svg_front
        # assert  == self.svg_walls[f[0]][0].sort()

        # assert obj.svg_right == self.svg_walls[f[0]][1]

        # assert obj.svg_top == self.svg_walls[f[0]][2]

        # assert obj.svg_3d == self.svg_walls[f[0]][3]
        pass