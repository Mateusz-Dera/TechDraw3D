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

        dwg2svg_windows = ".\\TechDraw3D\\LibreDWG\\dwg2SVG.exe"
        dwg2svg_linux = "dwg2SVG"
        parameters = "--mspace"

        dwgfilepath = self.make_path(name)
        svgfilepath_windows = ".\\TechDraw3D\\data\\svg\\" + os.path.basename(dwgfilepath)[:-4] + ".svg"
        svgfilepath_linux = "./data/svg/" + os.path.basename(dwgfilepath)[:-4] + ".svg"

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

        #command = "dwg2SVG %s" % name  # the shell command
        #process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)

        #Launch the shell command:
        #self.DWG = process.communicate()

        # print (output[0])

        # a = subprocess.check_output(["/bin/bash", "pwd" ])
        # print(a)
        # DWG = subprocess.check_output(["/bin/sh", "dwg2svg %s" % name])
    
    def returnSVG(self):
        f = open('data/returned/footer.svg', 'x')
        f.write(str(self.DWG))
        f.close()
        # return DWG