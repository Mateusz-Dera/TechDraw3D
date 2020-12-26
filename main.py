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
from sys import platform
import logging
import runpy
import subprocess

# My modules
from libs.extruder.svg import SVG
from libs.extruder.dwginput import DWGInput
from libs.extruder.dxfinput import DXFInput
from libs.base import logger, args, argparser


_logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.configure_logging(args.paramArgsSimple())
    
    _logger.info("Start program")


    # Uruchomienie parsera argumentów.
    # NOTE: Dla linuxa aby skonwertować DWG na SVG trzeba dokonać następujących konswersji: DWG->DXF->SVG
    parser = argparser.make_parser()
    args = parser.parse_args()
    
    if not args.dwg2svg and not args.dwg2dxf and not args.viewobj and not args.dxf2svg and not args.make_walls and not args.makeobj and not args.do_all:
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

    if args.make_walls:
        svg = SVG(args.make_walls.name)
        svg.split_svg()
        svg.save_walls()

    if args.makeobj:
        if platform == "win32":
            # subprocess.call([r'.\faceplacer.bat'])
            pass
        if platform == "linux":
            process = subprocess.Popen(['sh', "./libs/mesher/face/run.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = process.communicate()

            process = subprocess.Popen(['sh', "./libs/mesher/extrude/run.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = process.communicate()

            process = subprocess.Popen(['sh', "./libs/mesher/boolean/run.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = process.communicate()

    if args.viewobj:
        runpy.run_path(path_name='./libs/base/display.py')

    if args.do_all:
        if platform == "win32":
            # subprocess.call([r'.\faceplacer.bat'])
            pass
        if platform == "linux":
            dwg = DWGInput()
            dxf = DXFInput()
            dwg.dwg2dxf_converter(args.do_all.name)
            dxf.dxf2svg_converter(args.do_all.name.replace("dwg", "dxf"))

            svg = SVG(args.do_all.name.replace("dwg", "svg"))
            svg.split_svg()
            svg.save_walls()

            process = subprocess.Popen(['sh', "./libs/mesher/face/run.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = process.communicate()

            process = subprocess.Popen(['sh', "./libs/mesher/extrude/run.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = process.communicate()

            process = subprocess.Popen(['sh', "./libs/mesher/boolean/run.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = process.communicate()
            

    # Obsługa SVG

    # svgObj = SVG()
    # res = svgObj.create_svg_object("assets/svg/iw.svg", kwargs={'logger': _logger})
    # a, b, c = svgObj.parse_svg_dict(res)

