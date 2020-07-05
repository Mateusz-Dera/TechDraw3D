# Libs
import logging
import runpy

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
    
    if not args.dwg2svg and not args.dwg2dxf and not args.viewobj:
        print("No arguments.")
        exit(1)

    if args.dwg2svg:
        dwg = DWGInput()
        dwg.dwg2svg_converter(args.dwg2svg.name)

    if args.dwg2dxf:
        dwg = DWGInput()
        dwg.dwg2dxf_converter(args.dwg2dxf.name)      

    if args.viewobj:
        runpy.run_path(path_name='obj_viewer.py')

    # Obsługa SVG

    # svgObj = SVG()
    # res = svgObj.create_svg_object("assets/svg/iw.svg", kwargs={'logger': _logger})
    # a, b, c = svgObj.parse_svg_dict(res)

