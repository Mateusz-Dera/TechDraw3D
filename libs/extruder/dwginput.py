# Libs
from sys import platform
import logging
import subprocess
import os.path

# My modules
from svgpathtools import svg2paths, svg2paths2, wsvg

_logger = logging.getLogger(__name__)

class DWGInput():
    DWG = ""

    # Funkcja zwracająca ścieżkę absolutną.
    def make_path(self, p):
        p = os.path.expanduser(p)
        p = os.path.normpath(p)
        p = os.path.realpath(p)
        p = os.path.abspath(p)
        return p

    # Wrapper do LibreDWG / dwg2SVG.
    def dwg2svg_converter(self, name):

        dwg2svg_windows = ".\\tools\\LibreDWG\\dwg2SVG.exe"
        dwg2svg_linux = "dwg2SVG"
        parameters = "--mspace"

        dwgfilepath = self.make_path(name)
        svgfilepath_windows = ".\\assets\\svg\\" + os.path.basename(dwgfilepath)[:-4] + ".svg"
        svgfilepath_linux = "./assets/svg/" + os.path.basename(dwgfilepath)[:-4] + ".svg"

        # Wybór platformy.
        if platform == "win32":
            print ("WINDOWS")
            print ("DWG file path:", dwgfilepath)
            print ("SVG file path:", svgfilepath_windows)
            subprocess.Popen([dwg2svg_windows, parameters, dwgfilepath, '>', svgfilepath_windows], shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

        if platform == "linux":
            print ("LINUX")
            print ("DWG file path: ", dwgfilepath)
            print ("SVG file path: ", svgfilepath_linux)
            subprocess.call([dwg2svg_linux + ' ' + parameters + ' ' + dwgfilepath + ' > ' + svgfilepath_linux], shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    
    # Wrapper do LibreDWG / dwg2dxf.

    # TODO: Zapisywanie do folderu assets/dxf!
    
    def dwg2dxf_converter(self, name):

        dwg2dxf_windows = self.make_path(".\\tools\\LibreDWG\\dwg2dxf.exe")
        dwg2dxf_linux = "dwg2dxf"
        parameters = "-m"

        dwgfilepath = self.make_path(name)
        dxffilepath_windows = self.make_path(".\\assets\\dxf\\") + "\\" + os.path.basename(dwgfilepath)[:-4] + ".dxf"
        dxffilepath_linux = "./assets/dxf/" + os.path.basename(dwgfilepath)[:-4] + ".dxf"

        # Wybór platformy.
        if platform == "win32":
            print ("WINDOWS")
            print ("DWG file path:", dwgfilepath)
            print ("DXF file path:", dxffilepath_windows)
            print (dwg2dxf_windows, parameters, dwgfilepath)
            subprocess.Popen([dwg2dxf_windows, parameters, dwgfilepath], shell=True)

        if platform == "linux":
            print ("LINUX")
            print ("DWG file path: ", dwgfilepath)
            print ("DXF file path: ", dxffilepath_linux)
            subprocess.call([dwg2dxf_linux + ' ' + parameters + ' ' + dxffilepath_linux + ' ' + dwgfilepath], shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

    def returnSVG(self):
        f = open('data/returned/footer.svg', 'x')
        f.write(str(self.DWG))
        f.close()
        # return DWG