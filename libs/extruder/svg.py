# Libs
import logging

# My modules
from svgpathtools import svg2paths, svg2paths2, wsvg


_logger = logging.getLogger(__name__)


class SVG():
    svg_front = []
    svg_right = []
    svg_top = []
    svg_3d = []

    svg_xy_center = {}

    # Metody dostępne wewnątrz klasy
    def __init__(self, svg):
        # TODO: docstring classy
        # TODO: Obsługa pliku wczytywanego z systemu jak i np STRINGIO (imitacja pliku jako bufora IO)

        self.paths, self.attributes = svg2paths('./assets/svg/P003.svg')
        self.svg_xy_center = {"x": 0, "y": 0}

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
                self.svg_top .append(path)
            elif path.start.real > self.svg_xy_center['x'] and path.start.imag > self.svg_xy_center['y']:
                self.svg_3d.append(path)
            elif path.start.real > self.svg_xy_center['x'] and path.start.imag < self.svg_xy_center['y']:
                self.svg_right.append(path)
            elif path.start.real < self.svg_xy_center['x'] and path.start.imag < self.svg_xy_center['y']:
                self.svg_front.append(path)

    def save_walls(self):
        wsvg(paths=self.svg_front, filename="./assets/svg/temp/walls/front.svg")
        wsvg(paths=self.svg_right, filename="./assets/svg/temp/walls/right.svg")
        wsvg(paths=self.svg_top, filename="./assets/svg/temp/walls/top.svg")
        wsvg(paths=self.svg_3d, filename="./assets/svg/temp/walls/svg3d.svg")


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