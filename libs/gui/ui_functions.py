# TechDraw3D
# Copyright © 2021 Tomasz Nowak, Mateusz Dera, Jakub Schwarz

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

from qtpy import QtCore, QtGui, QtWidgets
from qtpy.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from qtpy.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from qtpy.QtWidgets import *
import sys
import os
import subprocess
import pyvista
import pyvistaqt
import webbrowser

import time

from main import MainWindow
from libs.extruder.svg import SVG
from libs.extruder.dwginput import DWGInput
from libs.extruder.dxfinput import DXFInput


class UIFunctions(MainWindow):
    
    def browse_input_file(self):
        if sys.platform == "win32":
            homepath = os.environ["HOMEPATH"]
        if sys.platform == "linux":
            homepath = os.environ["HOME"]

        fname=QFileDialog.getOpenFileName(self, "Input file", homepath, "DWG / DXF file (*.dwg *.dxf)")
        self.ui.lineEdit_input_file.setText(fname[0])

    def browse_output_file(self):
        if sys.platform == "win32":
            homepath = os.environ["HOMEPATH"]
        if sys.platform == "linux":
            homepath = os.environ["HOME"]

        fname = QFileDialog.getSaveFileName(self, "Output file", homepath, "DXF file (*.dxf);; SVG file (*.svg);; OBJ file (*.obj);; STL file (*.stl)")
        self.ui.lineEdit_output_file.setText(fname[0])

    def view_obj(self):
        if sys.platform == "win32":
            homepath = os.environ["HOMEPATH"]
        if sys.platform == "linux":
            homepath = os.environ["HOME"]

        fname = QFileDialog.getOpenFileName(self, "Open file", homepath, "OBJ file (*.obj)")
        if fname[0]:
            mesh = pyvista.read(fname[0])
            plotter = pyvistaqt.BackgroundPlotter()
            plotter.add_mesh(mesh)

    def convert_dwg_to_dxf(self):
        if self.ui.lineEdit_dwg_file.text():
            dwg = DWGInput()
            file = self.ui.lineEdit_dwg_file.text()
            dwg.dwg2dxf_converter(file)

    def convert_dwg_to_svg(self):
        if self.ui.lineEdit_dwg_file.text():
            dwg = DWGInput()
            dxf = DXFInput()
            file = self.ui.lineEdit_dwg_file.text()
            dwg.dwg2dxf_converter(file)
            dxf.dxf2svg_converter(file.replace("dwg", "dxf"))

    def convert_dwg_to_obj(self):
        if self.ui.lineEdit_dwg_file.text():
            dwg = DWGInput()
            dxf = DXFInput()
            file = self.ui.lineEdit_dwg_file.text()
            dwg.dwg2dxf_converter(file)
            dxf.dxf2svg_converter(file.replace("dwg", "dxf"))

            svg = SVG(file.replace("dwg", "svg"))
            svg.split_svg()
            svg.save_walls()

            process = subprocess.Popen(['sh', "./libs/mesher/face/run.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = process.communicate()

            process = subprocess.Popen(['sh', "./libs/mesher/extrude/run.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = process.communicate()

            process = subprocess.Popen(['sh', "./libs/mesher/boolean/run.sh", "-obj"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = process.communicate()

    def convert_dwg_to_fbx(self):
        if self.ui.lineEdit_dwg_file.text():
            dwg = DWGInput()
            dxf = DXFInput()
            file = self.ui.lineEdit_dwg_file.text()
            dwg.dwg2dxf_converter(file)
            dxf.dxf2svg_converter(file.replace("dwg", "dxf"))

            svg = SVG(file.replace("dwg", "svg"))
            svg.split_svg()
            svg.save_walls()

            process = subprocess.Popen(['sh', "./libs/mesher/face/run.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = process.communicate()

            process = subprocess.Popen(['sh', "./libs/mesher/extrude/run.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = process.communicate()

            process = subprocess.Popen(['sh', "./libs/mesher/boolean/run.sh", "-fbx"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = process.communicate()

    def convert_dwg_to_stl(self):
        if self.ui.lineEdit_dwg_file.text():
            dwg = DWGInput()
            dxf = DXFInput()
            file = self.ui.lineEdit_dwg_file.text()
            dwg.dwg2dxf_converter(file)
            dxf.dxf2svg_converter(file.replace("dwg", "dxf"))

            svg = SVG(file.replace("dwg", "svg"))
            svg.split_svg()
            svg.save_walls()

            process = subprocess.Popen(['sh', "./libs/mesher/face/run.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = process.communicate()

            process = subprocess.Popen(['sh', "./libs/mesher/extrude/run.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = process.communicate()

            process = subprocess.Popen(['sh', "./libs/mesher/boolean/run.sh", "-stl"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = process.communicate()

    def convert_dxf_to_svg(self):
        if self.ui.lineEdit_dxf_file.text():
            dxf = DXFInput()
            file = self.ui.lineEdit_dxf_file.text()
            dxf.dxf2svg_converter(file)

    def start(self):
        if not self.ui.lineEdit_input_file.text():
            # TODO dialog "set input file"
            print ("set input file")
            return
        if not self.ui.lineEdit_output_file.text():
            # TODO dialog "set output file"
            print ("set output file")
            return

        input_format = self.ui.lineEdit_input_file.text()[-3:]
        output_format = self.ui.lineEdit_output_file.text()[-3:]

        if input_format == output_format:
            # TODO dialog "set different output format"
            print ("set different output format")
            return
        self.ui.button_start.setEnabled(False)
        QApplication.setOverrideCursor(Qt.WaitCursor)

        # te dwie linie muszą iść do funkcji
        QApplication.restoreOverrideCursor()
        self.ui.button_start.setEnabled(True)

        if input_format == "dxf":
            if output_format == "svg":
                # TODO konwersja dxf na svg
                return
            if output_format == "obj":
                # TODO konwersja dxf na obj
                return
            if output_format == "stl":
                # TODO konwersja dxf na stl
                return

        if input_format == "dwg":
            if output_format == "dxf":
                # TODO konwersja dwg na dxf
                return
            if output_format == "svg":
                # TODO konwersja dwg na svg
                return
            if output_format == "obj":
                # TODO konwersja dwg na obj
                return
            if output_format == "stl":
                # TODO konwersja dwg na stl
                return
        QApplication.restoreOverrideCursor()


    def ui_definitions(self):

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))

        self.ui.shadow_frame.setGraphicsEffect(self.shadow)

        self.ui.lineEdit_input_file.setEnabled(False)
        self.ui.lineEdit_output_file.setEnabled(False)

        self.ui.button_close.clicked.connect(lambda: self.close())
        self.ui.button_minimalize.clicked.connect(lambda: self.showMinimized())

        self.ui.button_choose_input_file.clicked.connect(lambda: UIFunctions.browse_input_file(self))
        self.ui.button_choose_output_file.clicked.connect(lambda: UIFunctions.browse_output_file(self))


       # self.ui.button_dxf.clicked.connect(lambda: UIFunctions.convert_dwg_to_dxf(self))
       # self.ui.button_svg.clicked.connect(lambda: UIFunctions.convert_dwg_to_svg(self))
       # self.ui.button_obj.clicked.connect(lambda: UIFunctions.convert_dwg_to_obj(self))
       # self.ui.button_svg2.clicked.connect(lambda: UIFunctions.convert_dxf_to_svg(self))
       # self.ui.button_fbx.clicked.connect(lambda: UIFunctions.convert_dwg_to_fbx(self))
        self.ui.button_start.clicked.connect(lambda: UIFunctions.start(self))

        self.ui.button_view_obj.clicked.connect(lambda: UIFunctions.view_obj(self))
        self.ui.button_info.clicked.connect(lambda: webbrowser.open("https://github.com/Mateusz-Dera/TechDraw3D"))

