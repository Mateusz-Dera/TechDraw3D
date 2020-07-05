# Libs
import logging
import runpy
import subprocess

# My modules
from libs.extruder.svg import SVG
from libs.extruder.dwginput import DWGInput
from libs.extruder.dxfinput import DXFInput
from libs.base import logger, args, argparser
from libs.base.argparser import *

_logger = logging.getLogger(__name__)


if __name__ == '__main__':
    logger.configure_logging(args.paramArgsSimple())
    
    _logger.info("Start program")


    # Uruchomienie parsera argumentów.
    parser = argparser.make_parser()
    args = parser.parse_args()
    
    if not args.dwg2svg and not args.dwg2dxf and not args.viewobj and not args.dxf2svg and not args.makeobj:
        print("No arguments.")
        exit(1)

    if args.dwg2svg:
        dwg = DWGInput()
        dwg.dwg2svg_converter(args.dwg2svg.name)

    if args.dwg2dxf:
        dwg = DWGInput()
        dwg.dwg2dxf_converter(args.dwg2dxf.name)      

    if args.dxf2svg:
        dxf = DXFInput()
        dxf.dxf2svg_converter(args.dxf2svg.name)

    if args.makeobj:
        subprocess.call([r'.\testrun.bat'])

    if args.viewobj:
        runpy.run_path(path_name='./libs/base/obj_viewer.py')

    # Obsługa SVG

    # svgObj = SVG()
    # res = svgObj.create_svg_object("assets/svg/iw.svg", kwargs={'logger': _logger})
    # a, b, c = svgObj.parse_svg_dict(res)

