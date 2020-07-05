from sys import platform
import logging
import os.path
from dxf2svg.pycore import save_svg_from_dxf, extract_all
from libs.base import makepath

# My modules
from svgpathtools import svg2paths, svg2paths2, wsvg

_logger = logging.getLogger(__name__)

class DXFInput():
    
    def dxf2svg_converter(self, name):
        dxffilepath = makepath.make_path(name)
        svgfilesize = 300

        svgfilepath_windows = makepath.make_path(".\\assets\\svg\\") + "\\" + os.path.basename(dxffilepath)[:-4] + ".svg"
        svgfilepath_linux = "./assets/svg/" + os.path.basename(dxffilepath)[:-4] + ".svg"

        if platform == "win32":
            print ("WINDOWS")
            print ("DXF file path:", dxffilepath)
            print ("SVG file path:", svgfilepath_windows)
            save_svg_from_dxf(dxffilepath, svgfilepath=svgfilepath_windows, frame_name=None, size=svgfilesize) 

        if platform == "linux":
            print ("LINUX")
            print ("DXF file path:", dxffilepath)
            print ("SVG file path:", svgfilepath_linux)
            save_svg_from_dxf(dxffilepath, svgfilepath=svgfilepath_linux, frame_name=None, size=svgfilesize)
