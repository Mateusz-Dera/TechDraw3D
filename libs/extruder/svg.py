# Libs
import logging

# My modules
from svgpathtools import svg2paths, svg2paths2, wsvg


_logger = logging.getLogger(__name__)


class SVG():
    # Metody dostępne wewnątrz klasy
    
    def __create_svg_dict(self, paths, attributes, context = None, **kwargs):
        # ctx = {'file': file, 'type': type }

        res = {}
        res['ctx'] = context
        res['paths'] = paths
        res['attributes'] = attributes

        _logger.info("Creating dict from SVG file!")
        _logger.debug('\n' + str(res))

        return res

    # Metody publiczne
    def create_svg_object(self, file, type="string", mode = "with_svg_attrib", **kwargs):
        """Przerabia obiekt podany w argumencie resource na obiekt svg
        resource to na tą chwilę tekst z pliku
        type ma umożliwić obsługę większej ilości źródeł
        type = string
        """
        paths, attributes, svg_attributes = [], [], []

        #TODO: Obsługa kwargs

        #TODO: try expect dla wczytywania pliku
        if mode == "with_svg_attrib":
            paths, attributes, svg_attributes = svg2paths2(file)
        else:
            paths, attributes = svg2paths(file)
            svg_attributes = None
        
        _logger.debug('\n' + str(paths))
        _logger.debug('\n' + str(attributes))
        _logger.debug('\n' + str(svg_attributes))
        

        svg_dict = self.__create_svg_dict(paths, attributes, {'file': file, 'type': type, 'svg_attributes': svg_attributes})

        _logger.info("Succesfully loaded SVG image and parse it into dict!")

        return svg_dict


    def parse_svg_dict(self, res, split_context = False):
        paths = res.get('paths')
        attributes = res.get('attributes')
        context = res.get('context')
        #NOTE: Może będzie trzeba jeszcze wydobyć context


        _logger.info("Succesfully splitted svg dict into three list!")
        return paths, attributes, context


    def parse(self, file):
        pass