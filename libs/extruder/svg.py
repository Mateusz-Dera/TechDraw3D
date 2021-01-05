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
import logging

# My modules
from svgpathtools import svg2paths, svg2paths2, wsvg, paths2svg


_logger = logging.getLogger(__name__)


class SVG():
    # Metody dostępne wewnątrz klasy
    def __init__(self, svg):
        # TODO: docstring classy
        # TODO: Obsługa pliku wczytywanego z systemu jak i np STRINGIO (imitacja pliku jako bufora IO)

        self.paths, self.attributes = svg2paths(svg)
        self.svg_xy_center = {"x": 0, "y": 0}

        # Pola przechowujące poszczególne rzuty rysunku technicznego
        self.svg_front = []
        self.svg_right = []
        self.svg_top = []
        self.svg_3d = []

    def _format_float(self, f):
        return '{:f}'.format(f).rstrip('0').rstrip('.')

    def _center_viewport(self, paths):
        (xmin, xmax, ymin, ymax) = paths2svg.big_bounding_box(paths)
        width = xmax - xmin
        height = ymax - ymin

        svg_attributes = {}
        svg_attributes['viewBox'] = ' '.join(map(self._format_float, (xmin, ymin, width, height)))

        return svg_attributes

    def split_svg(self):
        # Kopia listy wektorów do pracy lokalnej
        paths2 = self.paths

        # Znalezienie środka układu współrzędnych 
        paths2.sort(key=lambda x: x.start.real, reverse=True)

        min_x = paths2[-1].start.real
        max_x = paths2[0].start.real

        paths2.sort(key=lambda x: x.start.imag, reverse=True)

        min_y = paths2[-1].start.imag
        max_y = paths2[0].start.imag

        # Zapisanie środka
        self.svg_xy_center = {'x': (abs(min_x)+abs(max_x))/2, 'y': (abs(min_y)+abs(max_y))/2}

        # Przypisanie wektorów do odpowiednich przedziałów układu współrzędnych
        
        for path in self.paths:
            if path.start.real < self.svg_xy_center['x'] and path.start.imag > self.svg_xy_center['y']:
                self.svg_top.append(path)
            elif path.start.real > self.svg_xy_center['x'] and path.start.imag > self.svg_xy_center['y']:
                self.svg_3d.append(path)
            elif path.start.real > self.svg_xy_center['x'] and path.start.imag < self.svg_xy_center['y']:
                self.svg_right.append(path)
            elif path.start.real < self.svg_xy_center['x'] and path.start.imag < self.svg_xy_center['y']:
                self.svg_front.append(path)

    def save_walls(self):
        wsvg(paths=self.svg_front, svg_attributes=self._center_viewport(self.svg_front), filename="./libs/mesher/face/tmp/front.svg")
        wsvg(paths=self.svg_right, svg_attributes=self._center_viewport(self.svg_right), filename="./libs/mesher/face/tmp/right.svg")
        wsvg(paths=self.svg_top, svg_attributes=self._center_viewport(self.svg_top), filename="./libs/mesher/face/tmp/top.svg")
        #wsvg(paths=self.svg_3d, svg_attributes=self._center_viewport(self.svg_3d), filename="./libs/mesher/face/tmp/svg3d.svg")

    # def __create_svg_dict(self, paths, attributes, context = None, **kwargs):
    #     # ctx = {'file': file, 'type': type }

    #     res = {}
    #     res['ctx'] = context
    #     res['paths'] = paths
    #     res['attributes'] = attributes

    #     _logger.info("Creating dict from SVG file!")
    #     _logger.debug('\n' + str(res))

    #     return res

    # # Metody publiczne
    # def create_svg_object(self, file, type="string", mode = "with_svg_attrib", **kwargs):
    #     """Przerabia obiekt podany w argumencie resource na obiekt svg
    #     resource to na tą chwilę tekst z pliku
    #     type ma umożliwić obsługę większej ilości źródeł
    #     type = string
    #     """
    #     paths, attributes, svg_attributes = [], [], []

    #     #TODO: Obsługa kwargs

    #     #TODO: try expect dla wczytywania pliku
    #     if mode == "with_svg_attrib":
    #         paths, attributes, svg_attributes = svg2paths2(file)
    #     else:
    #         paths, attributes = svg2paths(file)
    #         svg_attributes = None
        
    #     _logger.debug('\n' + str(paths))
    #     _logger.debug('\n' + str(attributes))
    #     _logger.debug('\n' + str(svg_attributes))
        

    #     svg_dict = self.__create_svg_dict(paths, attributes, {'file': file, 'type': type, 'svg_attributes': svg_attributes})

    #     _logger.info("Succesfully loaded SVG image and parse it into dict!")

    #     return svg_dict


    # def parse_svg_dict(self, res, split_context = False):
    #     paths = res.get('paths')
    #     attributes = res.get('attributes')
    #     context = res.get('context')
    #     #NOTE: Może będzie trzeba jeszcze wydobyć context


    #     _logger.info("Succesfully splitted svg dict into three list!")
    #     return paths, attributes, context


    # def parse(self, file):
    #     pass