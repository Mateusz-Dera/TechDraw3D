# Libs
import logging

# My modules
from libs.extruder.svg import SVG
from libs.extruder.dwginput import DWGInput
from libs.base import logger, args


_logger = logging.getLogger(__name__)


if __name__ == '__main__':
    logger.configure_logging(args.paramArgsSimple())
    
    _logger.info("Start program")

    # svgObj = SVG()
    # res = svgObj.create_svg_object("data/iw.svg", kwargs={'logger': _logger})

    dwg = DWGInput()
    dwg.openconvertDWGTEST('/home/jschwarz/Projekty/Prywatne/TechDraw3D/data/footer.DWG')

    print(dwg.DWG)

    dwg.returnSVG()

    # a, b, c = svgObj.parse_svg_dict(res)

