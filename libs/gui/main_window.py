# -*- coding: utf-8 -*-
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(986, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.shadow_layout = QVBoxLayout(self.centralwidget)
        self.shadow_layout.setSpacing(0)
        self.shadow_layout.setObjectName(u"shadow_layout")
        self.shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.shadow_frame = QFrame(self.centralwidget)
        self.shadow_frame.setObjectName(u"shadow_frame")
        self.shadow_frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(92, 99, 85, 255), stop:1 rgba(26, 26, 26, 255));\n"
"border-radius: 10px;")
        self.shadow_frame.setFrameShape(QFrame.NoFrame)
        self.shadow_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.shadow_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QFrame(self.shadow_frame)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMaximumSize(QSize(16777215, 50))
        self.title_bar.setStyleSheet(u"background-color: none;")
        self.title_bar.setFrameShape(QFrame.StyledPanel)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_icon = QFrame(self.title_bar)
        self.frame_icon.setObjectName(u"frame_icon")
        self.frame_icon.setMaximumSize(QSize(50, 16777215))
        self.frame_icon.setFrameShape(QFrame.NoFrame)
        self.frame_icon.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_icon)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_icon = QLabel(self.frame_icon)
        self.label_icon.setObjectName(u"label_icon")
        self.label_icon.setPixmap(QPixmap(u"libs/gui/icons/icon_square.png"))
        self.label_icon.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.label_icon)


        self.horizontalLayout.addWidget(self.frame_icon)

        self.frame_title = QFrame(self.title_bar)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setFrameShape(QFrame.NoFrame)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_title)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 0, 0, 0)
        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        self.label_title.setFont(font)

        self.verticalLayout_3.addWidget(self.label_title)


        self.horizontalLayout.addWidget(self.frame_title)

        self.frame_buttons = QFrame(self.title_bar)
        self.frame_buttons.setObjectName(u"frame_buttons")
        self.frame_buttons.setMaximumSize(QSize(100, 16777215))
        self.frame_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_buttons)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(60, 0, 0, 10)
        self.button_close = QPushButton(self.frame_buttons)
        self.button_close.setObjectName(u"button_close")
        self.button_close.setMinimumSize(QSize(20, 20))
        self.button_close.setMaximumSize(QSize(20, 20))
        font1 = QFont()
        font1.setFamily(u"System")
        font1.setPointSize(10)
        font1.setBold(True)
        self.button_close.setFont(font1)
        self.button_close.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.534364, y1:0, x2:0.528909, y2:1, stop:0.00568182 rgba(120, 129, 110, 255), stop:0.5 rgba(151, 162, 139, 255), stop:1 rgba(162, 173, 149, 255));\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(222, 222, 222);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(232, 17, 35, 255), stop:1 rgba(255, 34, 67, 255));\n"
"}")

        self.horizontalLayout_2.addWidget(self.button_close)


        self.horizontalLayout.addWidget(self.frame_buttons)


        self.verticalLayout.addWidget(self.title_bar)

        self.content_bar = QFrame(self.shadow_frame)
        self.content_bar.setObjectName(u"content_bar")
        self.content_bar.setStyleSheet(u"background-color: none;")
        self.content_bar.setFrameShape(QFrame.NoFrame)
        self.content_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.content_bar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_display = QFrame(self.content_bar)
        self.frame_display.setObjectName(u"frame_display")
        self.frame_display.setFrameShape(QFrame.StyledPanel)
        self.frame_display.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_display)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.frame_display_background = QFrame(self.frame_display)
        self.frame_display_background.setObjectName(u"frame_display_background")
        self.frame_display_background.setStyleSheet(u"background-color: rgb(151, 162, 139);\n"
"border-radius: 5px;")
        self.frame_display_background.setFrameShape(QFrame.StyledPanel)
        self.frame_display_background.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.frame_display_background)


        self.horizontalLayout_3.addWidget(self.frame_display)

        self.frame_menu = QFrame(self.content_bar)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setMaximumSize(QSize(200, 16777215))
        self.frame_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_menu)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_menu_tabs = QFrame(self.frame_menu)
        self.frame_menu_tabs.setObjectName(u"frame_menu_tabs")
        self.frame_menu_tabs.setMaximumSize(QSize(50, 16777215))
        self.frame_menu_tabs.setFrameShape(QFrame.StyledPanel)
        self.frame_menu_tabs.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_menu_tabs)

        self.frame_menu_options = QFrame(self.frame_menu)
        self.frame_menu_options.setObjectName(u"frame_menu_options")
        self.frame_menu_options.setMinimumSize(QSize(0, 0))
        self.frame_menu_options.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.534364, y1:0, x2:0.528909, y2:1, stop:0.00568182 rgba(68, 73, 63, 255), stop:0.5 rgba(107, 115, 99, 255), stop:1 rgba(92, 99, 85, 255));\n"
"border-radius: 10px;")
        self.frame_menu_options.setFrameShape(QFrame.NoFrame)
        self.frame_menu_options.setFrameShadow(QFrame.Raised)
        self.button_start = QPushButton(self.frame_menu_options)
        self.button_start.setObjectName(u"button_start")
        self.button_start.setGeometry(QRect(25, 80, 100, 25))
        self.button_start.setMinimumSize(QSize(7, 0))
        font2 = QFont()
        font2.setFamily(u"MS Shell Dlg 2")
        font2.setPointSize(10)
        font2.setBold(True)
        self.button_start.setFont(font2)
        self.button_start.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	color: rgb(43, 43, 43);\n"
"	background-color: qlineargradient(spread:pad, x1:0.534364, y1:0, x2:0.528909, y2:1, stop:0.00568182 rgba(120, 129, 110, 255), stop:0.5 rgba(151, 162, 139, 255), stop:1 rgba(162, 173, 149, 255));\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: rgb(162, 173, 149);\n"
"}")
        self.button_exit = QPushButton(self.frame_menu_options)
        self.button_exit.setObjectName(u"button_exit")
        self.button_exit.setGeometry(QRect(25, 450, 100, 25))
        self.button_exit.setMinimumSize(QSize(7, 0))
        self.button_exit.setFont(font2)
        self.button_exit.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	color: rgb(43, 43, 43);\n"
"	background-color: qlineargradient(spread:pad, x1:0.534364, y1:0, x2:0.528909, y2:1, stop:0.00568182 rgba(120, 129, 110, 255), stop:0.5 rgba(151, 162, 139, 255), stop:1 rgba(162, 173, 149, 255));\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: rgb(162, 173, 149);\n"
"}")
        self.button_info = QPushButton(self.frame_menu_options)
        self.button_info.setObjectName(u"button_info")
        self.button_info.setGeometry(QRect(25, 415, 100, 25))
        self.button_info.setMinimumSize(QSize(7, 0))
        self.button_info.setFont(font2)
        self.button_info.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	color: rgb(43, 43, 43);\n"
"	background-color: qlineargradient(spread:pad, x1:0.534364, y1:0, x2:0.528909, y2:1, stop:0.00568182 rgba(120, 129, 110, 255), stop:0.5 rgba(151, 162, 139, 255), stop:1 rgba(162, 173, 149, 255));\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: rgb(162, 173, 149);\n"
"}")
        self.lineEdit_dwg_file = QLineEdit(self.frame_menu_options)
        self.lineEdit_dwg_file.setObjectName(u"lineEdit_dwg_file")
        self.lineEdit_dwg_file.setGeometry(QRect(10, 50, 109, 20))
        self.lineEdit_dwg_file.setStyleSheet(u"background-color: rgb(151, 162, 139);\n"
"border-radius: 0px;")
        self.button_choose_file = QPushButton(self.frame_menu_options)
        self.button_choose_file.setObjectName(u"button_choose_file")
        self.button_choose_file.setGeometry(QRect(120, 50, 20, 20))
        self.button_choose_file.setMinimumSize(QSize(7, 0))
        self.button_choose_file.setFont(font2)
        self.button_choose_file.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	color: rgb(43, 43, 43);\n"
"	background-color: qlineargradient(spread:pad, x1:0.534364, y1:0, x2:0.528909, y2:1, stop:0.00568182 rgba(120, 129, 110, 255), stop:0.5 rgba(151, 162, 139, 255), stop:1 rgba(162, 173, 149, 255));\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: rgb(162, 173, 149);\n"
"}")
        self.label_dwg = QLabel(self.frame_menu_options)
        self.label_dwg.setObjectName(u"label_dwg")
        self.label_dwg.setGeometry(QRect(45, 25, 55, 16))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.label_dwg.setFont(font3)
        self.label_dwg.setStyleSheet(u"background-color: none;\n"
"color: rgb(151, 162, 139);")

        self.horizontalLayout_4.addWidget(self.frame_menu_options)


        self.horizontalLayout_3.addWidget(self.frame_menu)


        self.verticalLayout.addWidget(self.content_bar)

        self.credits_bar = QFrame(self.shadow_frame)
        self.credits_bar.setObjectName(u"credits_bar")
        self.credits_bar.setMaximumSize(QSize(16777215, 30))
        self.credits_bar.setStyleSheet(u"background-color: none;")
        self.credits_bar.setFrameShape(QFrame.StyledPanel)
        self.credits_bar.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.credits_bar)


        self.shadow_layout.addWidget(self.shadow_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"window", None))
        self.label_icon.setText("")
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"TechDraw3D", None))
        self.button_close.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.button_start.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.button_exit.setText(QCoreApplication.translate("MainWindow", u"EXIT", None))
        self.button_info.setText(QCoreApplication.translate("MainWindow", u"INFO", None))
        self.button_choose_file.setText(QCoreApplication.translate("MainWindow", u"\u25bc", None))
        self.label_dwg.setText(QCoreApplication.translate("MainWindow", u"DWG file", None))
    # retranslateUi

