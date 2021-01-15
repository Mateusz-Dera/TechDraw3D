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

from main import MainWindow
from libs.extruder.svg import SVG
from libs.extruder.dwginput import DWGInput
from libs.extruder.dxfinput import DXFInput


class UIFunctions(MainWindow):
    
    def browse_dwg_file(self):
        if sys.platform == "win32":
            homepath = os.environ["HOMEPATH"]
        if sys.platform == "linux":
            homepath = os.environ["HOME"]

        fname=QFileDialog.getOpenFileName(self, "Open file", homepath, "DWG file (*.dwg)")
        self.ui.lineEdit_dwg_file.setText(fname[0])

    def browse_dxf_file(self):
        if sys.platform == "win32":
            homepath = os.environ["HOMEPATH"]
        if sys.platform == "linux":
            homepath = os.environ["HOME"]

        fname = QFileDialog.getOpenFileName(self, "Open file", homepath, "DXF file (*.dxf)")
        self.ui.lineEdit_dxf_file.setText(fname[0])

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


    def ui_definitions(self):

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))

        self.ui.shadow_frame.setGraphicsEffect(self.shadow)

        self.ui.lineEdit_dwg_file.setEnabled(False)
        self.ui.lineEdit_dxf_file.setEnabled(False)

        self.ui.button_close.clicked.connect(lambda: self.close())
        self.ui.button_choose_dwg_file.clicked.connect(lambda: UIFunctions.browse_dwg_file(self))
        self.ui.button_choose_dxf_file.clicked.connect(lambda: UIFunctions.browse_dxf_file(self))
        self.ui.button_view_obj.clicked.connect(lambda: UIFunctions.view_obj(self))
        self.ui.button_dxf.clicked.connect(lambda: UIFunctions.convert_dwg_to_dxf(self))
        self.ui.button_svg.clicked.connect(lambda: UIFunctions.convert_dwg_to_svg(self))
        self.ui.button_obj.clicked.connect(lambda: UIFunctions.convert_dwg_to_obj(self))
        self.ui.button_svg2.clicked.connect(lambda: UIFunctions.convert_dxf_to_svg(self))
        self.ui.button_fbx.clicked.connect(lambda: UIFunctions.convert_dwg_to_fbx(self))
        self.ui.button_stl.clicked.connect(lambda: UIFunctions.convert_dwg_to_stl(self))
        self.ui.button_info.clicked.connect(lambda: webbrowser.open("https://github.com/Mateusz-Dera/TechDraw3D"))

