from svgpathtools import svg2paths, wsvg


class SVG():
    # Metody dostępne wewnątrz klasy
    
    def __create_svg_dict(self, paths, attributes, context = None, **kwargs):
        # ctx = {'file': file, 'type': type }

        res = {}
        res['ctx'] = context
        res['paths'] = paths
        res['attributes'] = attributes

        return res

    # Metody publiczne
    def create_svg_object(self, file, type="string"):
        """Przerabia obiekt podany w argumencie resource na obiekt svg
        resource to na tą chwilę tekst z pliku
        type ma umożliwić obsługę większej ilości źródeł
        type = string
        """

        #NOTE: try expect dla wczytywania pliku
        paths, attributes = svg2paths(file)
        
        svg_dict = self.__create_svg_dict(paths, attributes, {'file': file, 'type': type })
        
        return svg_dict


    def parse_svg_dict(self, res, split_context = False):
        paths = res.get('paths')
        attributes = res.get('attributes')
        context = res.get('context')
        #NOTE: Może będzie trzeba jeszcze wydobyć context

        return paths, attributes, context


    def parse(self, file):
        pass