# Libs
import logging

# My modules
from libs.extruder.svg import SVG
from libs.extruder.dwginput import DWGInput
from libs.base import logger, args
from libs.base.argparser import *

_logger = logging.getLogger(__name__)


if __name__ == '__main__':
    logger.configure_logging(args.paramArgsSimple())
    
    _logger.info("Start program")

    # svgObj = SVG()
    # res = svgObj.create_svg_object("data/iw.svg", kwargs={'logger': _logger})

    parser = make_parser()
    args = parser.parse_args()
    print(args)
    dwg = DWGInput()
    dwg.dwg2svg_converter(args.file.name)

    #print(dwg.DWG)

    #dwg.returnSVG()

    # a, b, c = svgObj.parse_svg_dict(res)

