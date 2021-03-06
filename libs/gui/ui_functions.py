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

        fname = QFileDialog.getSaveFileName(self, "Output file", homepath, "DXF file (*.dxf);; FBX file (*.fbx);; OBJ file (*.obj);; STL file (*.stl);; SVG file (*.svg)")

        if sys.platform == "win32":
            filename = fname[0]
        if sys.platform == "linux":
            filename = fname[0] + fname[1][-5:-1]

        self.ui.lineEdit_output_file.setText(filename)

    def view_obj(self):
        if sys.platform == "win32":
            homepath = os.environ["HOMEPATH"]
        if sys.platform == "linux":
            homepath = os.environ["HOME"]

        fname = QFileDialog.getOpenFileName(self, "Open file", homepath, "OBJ file (*.obj)")

        if self.ui.checkBox_wireframe.isChecked():
            edges = True
            opacity = 0.5
            text = os.path.basename(fname[0]) + " wireframe"
        else:
            edges = False
            opacity = 1
            text = os.path.basename(fname[0])

        if fname[0]:
            mesh = pyvista.read(fname[0])
            plotter = pyvistaqt.BackgroundPlotter()
            plotter.add_mesh(mesh, show_edges=edges, opacity=opacity, color='blue')
            plotter.add_text(text)
            plotter.show_axes()

    def convert_dwg_to_dxf(self):
        input_file = self.ui.lineEdit_input_file.text()
        output_file = self.ui.lineEdit_output_file.text()
        dwg = DWGInput()
        dwg.dwg2dxf_converter(input_file, output_file)

    def convert_dwg_to_svg(self):
        input_file = self.ui.lineEdit_input_file.text()
        output_file = self.ui.lineEdit_output_file.text()
        dwg = DWGInput()
        dxf = DXFInput()
        dxf.dxf2svg_converter(dwg.dwg2dxf_converter(input_file, False), output_file)

    def convert_dxf_to_svg(self):
        input_file = self.ui.lineEdit_input_file.text()
        output_file = self.ui.lineEdit_output_file.text()
        dxf = DXFInput()
        dxf.dxf2svg_converter(input_file, output_file)

    def convert_2d_to_3d(self, type, dwg_switch):
        input_file = self.ui.lineEdit_input_file.text()
        output_file = self.ui.lineEdit_output_file.text()

        if dwg_switch:
            dwg = DWGInput()
            input_file = dwg.dwg2dxf_converter(input_file, False)

        dxf = DXFInput()
        svg = SVG(dxf.dxf2svg_converter(input_file, False))
        svg.split_svg()
        svg.save_walls()

        process = subprocess.Popen(['sh', "./libs/mesher/face/run.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()

        process = subprocess.Popen(['sh', "./libs/mesher/extrude/run.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()

        process = subprocess.Popen(['sh', "./libs/mesher/boolean/run.sh", type, output_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()

    def show_message(self, icon, message):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("TechDraw3D")
        msg.setWindowIcon(QtGui.QIcon("libs/gui/icons/icon_square.png"))
        msg.setText(message)
        msg.setIcon(icon)
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()

    def start(self):
        if not self.ui.lineEdit_input_file.text():
            UIFunctions.show_message(self, QMessageBox.Warning, "Choose input file!")
            return
        if not self.ui.lineEdit_output_file.text():
            UIFunctions.show_message(self, QMessageBox.Warning, "Choose output file!")
            return

        input_format = self.ui.lineEdit_input_file.text()[-3:].lower()
        output_format = self.ui.lineEdit_output_file.text()[-3:].lower()

        if input_format == output_format:
            UIFunctions.show_message(self, QMessageBox.Warning, "Choose different output file!")
            return

        self.ui.button_start.setEnabled(False)
        QApplication.setOverrideCursor(Qt.WaitCursor)

        if input_format == "dxf":
            if output_format == "svg":
                UIFunctions.convert_dxf_to_svg(self)
                QApplication.restoreOverrideCursor()
                if os.path.isfile(self.ui.lineEdit_output_file.text()):
                    UIFunctions.show_message(self, QMessageBox.Information, "SVG file saved successfully!")
                else:
                    UIFunctions.show_message(self, QMessageBox.Critical, "Error!")
                self.ui.button_start.setEnabled(True)
                return

            if output_format == "obj":
                UIFunctions.convert_2d_to_3d(self, "-obj", False)
                QApplication.restoreOverrideCursor()
                if os.path.isfile(self.ui.lineEdit_output_file.text()):
                    UIFunctions.show_message(self, QMessageBox.Information, "OBJ file saved successfully!")
                else:
                    UIFunctions.show_message(self, QMessageBox.Critical, "Error!")
                self.ui.button_start.setEnabled(True)
                return

            if output_format == "fbx":
                UIFunctions.convert_2d_to_3d(self, "-fbx", False)
                QApplication.restoreOverrideCursor()
                if os.path.isfile(self.ui.lineEdit_output_file.text()):
                    UIFunctions.show_message(self, QMessageBox.Information, "FBX file saved successfully!")
                else:
                    UIFunctions.show_message(self, QMessageBox.Critical, "Error!")
                self.ui.button_start.setEnabled(True)
                return

            if output_format == "stl":
                UIFunctions.convert_2d_to_3d(self, "-stl", False)
                QApplication.restoreOverrideCursor()
                if os.path.isfile(self.ui.lineEdit_output_file.text()):
                    UIFunctions.show_message(self, QMessageBox.Information, "STL file saved successfully!")
                else:
                    UIFunctions.show_message(self, QMessageBox.Critical, "Error!")
                self.ui.button_start.setEnabled(True)
                return
            QApplication.restoreOverrideCursor()
            UIFunctions.show_message(self, QMessageBox.Critical, "Something is wrong with output file!")
            return


        if input_format == "dwg":
            if output_format == "dxf":
                UIFunctions.convert_dwg_to_dxf(self)
                QApplication.restoreOverrideCursor()
                if os.path.isfile(self.ui.lineEdit_output_file.text()):
                    UIFunctions.show_message(self, QMessageBox.Information, "DXF file saved successfully!")
                else:
                    UIFunctions.show_message(self, QMessageBox.Critical, "Error!")
                self.ui.button_start.setEnabled(True)
                return

            if output_format == "svg":
                UIFunctions.convert_dwg_to_svg(self)
                QApplication.restoreOverrideCursor()
                if os.path.isfile(self.ui.lineEdit_output_file.text()):
                    UIFunctions.show_message(self, QMessageBox.Information, "SVG file saved successfully!")
                else:
                    UIFunctions.show_message(self, QMessageBox.Critical, "Error!")
                self.ui.button_start.setEnabled(True)
                return

            if output_format == "obj":
                UIFunctions.convert_2d_to_3d(self, "-obj", True)
                QApplication.restoreOverrideCursor()
                if os.path.isfile(self.ui.lineEdit_output_file.text()):
                    UIFunctions.show_message(self, QMessageBox.Information, "OBJ file saved successfully!")
                else:
                    UIFunctions.show_message(self, QMessageBox.Critical, "Error!")
                self.ui.button_start.setEnabled(True)
                return

            if output_format == "fbx":
                UIFunctions.convert_2d_to_3d(self, "-fbx", True)
                QApplication.restoreOverrideCursor()
                if os.path.isfile(self.ui.lineEdit_output_file.text()):
                    UIFunctions.show_message(self, QMessageBox.Information, "FBX file saved successfully!")
                else:
                    UIFunctions.show_message(self, QMessageBox.Critical, "Error!")
                self.ui.button_start.setEnabled(True)
                return

            if output_format == "stl":
                UIFunctions.convert_2d_to_3d(self, "-stl", True)
                QApplication.restoreOverrideCursor()
                if os.path.isfile(self.ui.lineEdit_output_file.text()):
                    UIFunctions.show_message(self, QMessageBox.Information, "STL file saved successfully!")
                else:
                    UIFunctions.show_message(self, QMessageBox.Critical, "Error!")
                self.ui.button_start.setEnabled(True)
                return
            QApplication.restoreOverrideCursor()
            UIFunctions.show_message(self, QMessageBox.Critical, "Something is wrong with output file!")
            return
        QApplication.restoreOverrideCursor()
        self.ui.button_start.setEnabled(True)
        UIFunctions.show_message(self, QMessageBox.Critical, "Something is wrong with input file!")



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

        self.ui.button_start.clicked.connect(lambda: UIFunctions.start(self))

        self.ui.button_view_obj.clicked.connect(lambda: UIFunctions.view_obj(self))
        self.ui.button_info.clicked.connect(lambda: webbrowser.open("https://github.com/Mateusz-Dera/TechDraw3D"))

