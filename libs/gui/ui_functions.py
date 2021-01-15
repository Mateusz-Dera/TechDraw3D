from qtpy import QtCore, QtGui, QtWidgets
from qtpy.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from qtpy.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from qtpy.QtWidgets import *
import sys
import os

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

    def convert_dwg_to_dxf(self):
        dwg = DWGInput()
        if self.ui.lineEdit_dwg_file.text():
            file = self.ui.lineEdit_dwg_file.text()
            dwg.dwg2dxf_converter(file)

    def convert_dwg_to_svg(self):
        dwg = DWGInput()
        dxf = DXFInput()
        if self.ui.lineEdit_dwg_file.text():
            file = self.ui.lineEdit_dwg_file.text()
            dwg.dwg2dxf_converter(file)
            dxf.dxf2svg_converter(file.replace("dwg", "dxf"))


    def ui_definitions(self):

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))

        self.ui.shadow_frame.setGraphicsEffect(self.shadow)

        self.ui.button_close.clicked.connect(lambda: self.close())
        self.ui.button_choose_dwg_file.clicked.connect(lambda: UIFunctions.browse_dwg_file(self))
        self.ui.button_choose_dxf_file.clicked.connect(lambda: UIFunctions.browse_dxf_file(self))
        self.ui.button_dxf.clicked.connect(lambda: UIFunctions.convert_dwg_to_dxf(self))
        self.ui.button_svg.clicked.connect(lambda: UIFunctions.convert_dwg_to_svg(self))

