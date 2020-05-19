# Libs
import logging
import subprocess

# My modules
from svgpathtools import svg2paths, svg2paths2, wsvg


_logger = logging.getLogger(__name__)


class DWGInput():
    DWG = ""

    def openconvertDWGTEST(self, name):

        command = "dwg2SVG %s" % name  # the shell command
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)

        #Launch the shell command:
        self.DWG = process.communicate()

        # print (output[0])




        # a = subprocess.check_output(["/bin/bash", "pwd" ])
        # print(a)
        # DWG = subprocess.check_output(["/bin/sh", "dwg2svg %s" % name])
    
    def returnSVG(self):
        f = open('data/returned/footer.svg', 'x')
        f.write(str(self.DWG))
        f.close()
        # return DWG