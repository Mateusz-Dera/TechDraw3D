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
from libs.extruder.svg import SVG
from test import tools

from svgpathtools import Path, Line
import pytest
import os


class TestBasicSVG:
    """{"x": 0, "y": 0}
    """
    paths = tools.get_specified_paths(tools.assets_type("simple"), '.svg')

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

    @pytest.mark.parametrize('ints, result', [
        (2,'2'),
        (2.0, '2'),
        (02.0, '2'),
        (2.01, '2.01'),
        (0, '0'),
        (0.0, '0'),
        (0.0001, '0.0001'),
        (0.0000001, '0'),
        (-10.0, '-10'),
        (-0, '0'),
        (2/2, '1'),
        (5/2, '2.5'),
        (1001.1001, '1001.1001')
    ])
    def test_format_float(self, ints, result):
        obj = SVG(self.paths[0])

        assert obj._format_float(ints) == result

class TestSplitting():
    paths = tools.get_specified_paths(tools.assets_type("simple"), '.svg')
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
            [   # FRONT
                Path(Line(start=(154.57669750254536+133.51494451379006j), end=(169.57669750254536+133.51494451379006j))), Path(Line(start=(154.57669750254536+98.51494451379007j), end=(154.57669750254536+133.51494451379006j))), Path(Line(start=(119.57669750254536+98.51494451379007j), end=(154.57669750254536+98.51494451379007j))), Path(Line(start=(169.57669750254536+83.51494451379007j), end=(169.57669750254536+133.51494451379006j))), Path(Line(start=(119.57669750254536+83.51494451379007j), end=(169.57669750254536+83.51494451379007j))), Path(Line(start=(119.57669750254536+83.51494451379007j), end=(119.57669750254536+98.51494451379007j)))
            ],
            [   # RIGHT
                Path(Line(start=(262.2949876205803+133.51494451379006j), end=(312.2949876205803+133.51494451379006j))), Path(Line(start=(312.2949876205803+98.51494451379007j), end=(312.2949876205803+133.51494451379006j))), Path(Line(start=(262.2949876205803+98.51494451379007j), end=(262.2949876205803+133.51494451379006j))), Path(Line(start=(262.2949876205694+98.51494451379007j), end=(312.2949876205694+98.51494451379007j))), Path(Line(start=(312.2949876205694+83.51494451379007j), end=(312.2949876205694+98.51494451379007j))), Path(Line(start=(262.2949876205694+83.51494451379007j), end=(262.2949876205694+98.51494451379007j))), Path(Line(start=(262.2949876205694+83.51494451379007j), end=(312.2949876205694+83.51494451379007j)))
            ],
            [   # TOP
                Path(Line(start=(169.57669750254718+253.47010943127862j), end=(154.57669750254718+253.47010943127862j))), Path(Line(start=(154.57669750254718+253.47010943127862j), end=(154.57669750254718+203.47010943127862j))), Path(Line(start=(154.57669750254718+253.47010943127862j), end=(119.57669750254718+253.47010943127862j))), Path(Line(start=(119.57669750254718+253.47010943127862j), end=(119.57669750254718+203.47010943127862j))), Path(Line(start=(169.57669750254718+203.47010943127862j), end=(169.57669750254718+253.47010943127862j))), Path(Line(start=(154.57669750254718+203.47010943127862j), end=(169.57669750254718+203.47010943127862j))), Path(Line(start=(119.57669750254718+203.47010943127862j), end=(154.57669750254718+203.47010943127862j)))
            ],
            [   # 3D
                Path(Line(start=(307.6563606346954+257.59640306416384j), end=(272.30102157537294+237.23661737454438j))), Path(Line(start=(318.26296235249356+251.48846735728j), end=(307.6563606346954+257.59640306416384j))), Path(Line(start=(272.30102157537294+237.23661737454438j), end=(282.9076232931711+231.12868166766054j))), Path(Line(start=(272.30102157537294+237.12616797052308j), end=(247.5522842338396+222.8743179877852j))), Path(Line(start=(282.9076232931711+231.12868166766054j), end=(318.26296235249356+251.48846735728j))), Path(Line(start=(247.5522842338396+222.8743179877852j), end=(272.30102157537294+208.62246800505548j))), Path(Line(start=(318.26296235249356+210.611111115153j), end=(318.26296235249356+251.48846735728j))), Path(Line(start=(247.5522842338396+210.61111111514708j), end=(282.9076232931711+190.25132542553354j))), Path(Line(start=(247.5522842338396+210.61111111514708j), end=(247.5522842338396+222.8743179877852j))), Path(Line(start=(272.30102157537294+208.62246800505548j), end=(272.30102157537294+237.23661737454438j))), Path(Line(start=(282.9076232931711+190.25132542553354j), end=(318.26296235249356+210.611111115153j))), Path(Line(start=(282.9076232931711+190.25132542553354j), end=(282.9076232931711+231.12868166766054j)))
            ]
        ],
        "P003.svg": [
            [   # FRONT
                Path(Line(start=(172.4155791352223+92.05079676928852j), end=(172.4155791352223+192.05079676928852j))), Path(Line(start=(122.41557913522229+92.05079676928852j), end=(172.4155791352223+92.05079676928852j))), Path(Line(start=(122.41557913522229+92.05079676928852j), end=(122.41557913522229+192.05079676928852j)))
            ],
            [   # RIGHT
                Path(Line(start=(329.9903577108471+92.05079676928852j), end=(329.9903577108471+192.05079676928852j))), Path(Line(start=(304.9903577108471+92.05079676928852j), end=(304.9903577108471+192.05079676928852j))), Path(Line(start=(304.9903577108471+92.05079676928852j), end=(329.9903577108471+92.05079676928852j)))
            ],
            [   # TOP
                Path(Line(start=(172.41557913522047+266.250983153428j), end=(172.41557913522047+241.25098315342802j))), Path(Line(start=(122.41557913522047+266.250983153428j), end=(172.41557913522047+266.250983153428j))), Path(Line(start=(172.41557913522047+241.25098315342802j), end=(122.41557913522047+241.25098315342802j))), Path(Line(start=(122.41557913522047+241.25098315342802j), end=(122.41557913522047+266.250983153428j))), Path(Line(start=(122.41557913522229+192.05079676928852j), end=(172.4155791352223+192.05079676928852j)))
            ],
            [   # 3D
                Path(Line(start=(304.9903577108471+192.05079676928852j), end=(329.9903577108471+192.05079676928852j)))
            ]
        ],
        "P004.svg": [
            [   # FRONT
                Path(Line(start=(141.672693399918+113.97012506875092j), end=(141.672693399918+98.97012506875092j))), Path(Line(start=(121.67269339991799+113.97012506875092j), end=(141.672693399918+113.97012506875092j))), Path(Line(start=(156.672693399918+98.97012506875092j), end=(156.672693399918+83.97012506875092j))), Path(Line(start=(141.672693399918+98.97012506875092j), end=(156.672693399918+98.97012506875092j))), Path(Line(start=(121.67269339991799+98.97012506875092j), end=(121.67269339991799+113.97012506875092j))), Path(Line(start=(106.67269339991799+98.97012506875092j), end=(121.67269339991799+98.97012506875092j))), Path(Line(start=(156.672693399918+83.97012506875092j), end=(106.67269339991799+83.97012506875092j))), Path(Line(start=(106.67269339991799+83.97012506875092j), end=(106.67269339991799+98.97012506875092j)))
            ],
            [   # RIGHT
                Path(Line(start=(325.7151484496271+113.97012506875092j), end=(275.7151484496271+113.97012506875092j))), Path(Line(start=(325.7151484496271+98.97012506875092j), end=(325.7151484496271+113.97012506875092j))), Path(Line(start=(325.7151484496226+98.97012506875092j), end=(275.7151484496226+98.97012506875092j))), Path(Line(start=(275.7151484496271+98.97012506875092j), end=(275.7151484496271+113.97012506875092j))), Path(Line(start=(325.7151484496226+83.97012506875092j), end=(325.7151484496226+98.97012506875092j))), Path(Line(start=(325.7151484496226+83.97012506875092j), end=(275.7151484496226+83.97012506875092j))), Path(Line(start=(275.7151484496226+83.97012506875092j), end=(275.7151484496226+98.97012506875092j)))
            ],
            [   # TOP
                Path(Line(start=(141.6726933999198+259.40337650581114j), end=(156.6726933999198+259.40337650581114j))), Path(Line(start=(121.67269339991981+259.40337650581114j), end=(141.6726933999198+259.40337650581114j))), Path(Line(start=(106.67269339991981+259.40337650581114j), end=(121.67269339991981+259.40337650581114j))), Path(Line(start=(156.6726933999198+209.40337650581114j), end=(156.6726933999198+259.40337650581114j))), Path(Line(start=(141.6726933999198+209.40337650581114j), end=(156.6726933999198+209.40337650581114j))), Path(Line(start=(141.6726933999198+209.40337650581114j), end=(141.6726933999198+259.40337650581114j))), Path(Line(start=(121.67269339991981+209.40337650581114j), end=(141.6726933999198+209.40337650581114j))), Path(Line(start=(121.67269339991981+209.40337650581114j), end=(121.67269339991981+259.40337650581114j))), Path(Line(start=(106.67269339991981+209.40337650581114j), end=(121.67269339991981+209.40337650581114j))), Path(Line(start=(106.67269339991981+209.40337650581114j), end=(106.67269339991981+259.40337650581114j)))
            ],
            [   # 3D
                Path(Line(start=(303.0378773621751+261.6287331511509j), end=(317.18001298590843+253.4848188753055j))), Path(Line(start=(317.18001298590843+253.4848188753055j), end=(317.18001298590843+241.22161200266743j))), Path(Line(start=(267.68253830285266+241.26894746153124j), end=(281.824673926586+233.12503318568582j))), Path(Line(start=(267.68253830285266+241.26894746153124j), end=(303.0378773621751+261.6287331511509j))), Path(Line(start=(317.18001298590843+241.22161200266743j), end=(327.78661470370844+235.11367629578336j))), Path(Line(start=(327.78661470370844+235.11367629578336j), end=(327.78661470370844+222.85046942314526j))), Path(Line(start=(257.07593658505266+235.11367629577745j), end=(267.68253830285266+229.00574058889316j))), Path(Line(start=(257.07593658505266+235.11367629577745j), end=(267.68253830285266+241.22161200266515j))), Path(Line(start=(281.824673926586+233.12503318568582j), end=(281.824673926586+220.86182631304774j))), Path(Line(start=(281.824673926586+233.12503318568582j), end=(317.18001298590843+253.4848188753055j))), Path(Line(start=(267.68253830285266+229.00574058889316j), end=(267.68253830285266+241.26894746153124j))), Path(Line(start=(257.07593658505266+222.85046942313934j), end=(257.07593658505266+235.11367629577745j))), Path(Line(start=(281.824673926586+220.86182631304774j), end=(292.431275644386+214.75389060616368j))), Path(Line(start=(281.824673926586+220.86182631304774j), end=(317.18001298590843+241.22161200266743j))), Path(Line(start=(292.431275644386+214.75389060616368j), end=(292.431275644386+202.49068373352557j))), Path(Line(start=(292.431275644386+214.75389060616368j), end=(327.78661470370844+235.11367629578336j))), Path(Line(start=(292.431275644386+202.49068373352557j), end=(327.78661470370844+222.85046942314526j))), Path(Line(start=(292.431275644386+202.49068373352557j), end=(257.07593658505266+222.85046942313934j)))
            ]
        ]
    }

    @pytest.mark.parametrize('path', paths)
    def test_split_svg_square(self, path):
        obj = SVG(path)
        obj.split_svg()

        f = [file for file in self.files if file in path]

        tools.svg_compare_path(self.svg_walls[f[0]][0], obj.svg_front)
        tools.svg_compare_path(self.svg_walls[f[0]][1], obj.svg_right)
        tools.svg_compare_path(self.svg_walls[f[0]][2], obj.svg_top)
        tools.svg_compare_path(self.svg_walls[f[0]][3], obj.svg_3d)

        assert obj.svg_xy_center != {"x": 0, "y": 0}