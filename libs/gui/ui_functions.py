from qtpy import QtCore, QtGui, QtWidgets
from qtpy.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from qtpy.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from qtpy.QtWidgets import *
import sys
import os

from main import MainWindow


class UIFunctions(MainWindow):
    
    def browse_dwg_file(self):

        if sys.platform == "win32":
            homepath = os.environ["HOMEPATH"]
        if sys.platform == "linux":
            homepath = os.environ["HOME"]

        fname=QFileDialog.getOpenFileName(self, "Open file", homepath, "DWG file (*.dwg)" )
        self.ui.lineEdit_dwg_file.setText(fname[0])


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

