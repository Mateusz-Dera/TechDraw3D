# Libs
import logging

# My modules
from libs.extruder.svg import SVG
from libs.extruder.dwginput import DWGInput
from libs.base import logger, args, argparser
from libs.base.argparser import *

_logger = logging.getLogger(__name__)


if __name__ == '__main__':
    logger.configure_logging(args.paramArgsSimple())
    
    _logger.info("Start program")


    # Uruchomienie parsera argumentów.
    parser = argparser.make_parser()
    args = parser.parse_args()
    
    # print(args)

    # Uruchomienie funkcji konwertującej dwg2svg.
    dwg = DWGInput()
    dwg.dwg2svg_converter(args.file.name)

    # Obsługa SVG

    svgObj = SVG()
    res = svgObj.create_svg_object("assets/svg/iw.svg", kwargs={'logger': _logger})
    a, b, c = svgObj.parse_svg_dict(res)

