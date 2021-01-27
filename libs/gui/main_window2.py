# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(986, 600)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.shadow_layout = QVBoxLayout(self.centralwidget)
        self.shadow_layout.setSpacing(0)
        self.shadow_layout.setObjectName(u"shadow_layout")
        self.shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.shadow_frame = QFrame(self.centralwidget)
        self.shadow_frame.setObjectName(u"shadow_frame")
        self.shadow_frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.534364, y1:0, x2:0.528909, y2:1, stop:0.00568182 rgba(126, 126, 126, 255), stop:0.5 rgba(142, 142, 142, 255), stop:1 rgba(142, 142, 142, 255));\n"
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
        font.setWeight(75)
        self.label_title.setFont(font)

        self.verticalLayout_3.addWidget(self.label_title)


        self.horizontalLayout.addWidget(self.frame_title)

        self.frame_buttons = QFrame(self.title_bar)
        self.frame_buttons.setObjectName(u"frame_buttons")
        self.frame_buttons.setMaximumSize(QSize(100, 16777215))
        self.frame_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_buttons.setFrameShadow(QFrame.Raised)
        self.button_close = QPushButton(self.frame_buttons)
        self.button_close.setObjectName(u"button_close")
        self.button_close.setGeometry(QRect(70, 10, 20, 20))
        self.button_close.setMinimumSize(QSize(20, 20))
        self.button_close.setMaximumSize(QSize(20, 20))
        font1 = QFont()
        font1.setFamily(u"System")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.button_close.setFont(font1)
        self.button_close.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.534364, y1:0, x2:0.528909, y2:1, stop:0.00568182 rgba(129, 129, 129, 255), stop:0.5 rgba(162, 162, 162, 255), stop:1 rgba(173, 173, 173, 255));\n"
"}\n"
"QPushButton:hover{\n"
"	color: rgb(222, 222, 222);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(232, 17, 35, 255), stop:1 rgba(255, 34, 67, 255));\n"
"}")
        self.button_minimalize = QPushButton(self.frame_buttons)
        self.button_minimalize.setObjectName(u"button_minimalize")
        self.button_minimalize.setGeometry(QRect(45, 10, 20, 20))
        self.button_minimalize.setMinimumSize(QSize(20, 20))
        self.button_minimalize.setMaximumSize(QSize(20, 20))
        font2 = QFont()
        font2.setFamily(u"System")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.button_minimalize.setFont(font2)
        self.button_minimalize.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.534364, y1:0, x2:0.528909, y2:1, stop:0.00568182 rgba(129, 129, 129, 255), stop:0.5 rgba(162, 162, 162, 255), stop:1 rgba(173, 173, 173, 255));\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(185, 185, 185);\n"
"}")

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
        self.frame_display_background.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.534364, y1:0, x2:0.528909, y2:1, stop:0.00568182 rgba(73, 73, 73, 255), stop:1 rgba(99, 99, 99, 255));\n"
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
        self.frame_menu_tabs = QFrame(self.frame_menu)
        self.frame_menu_tabs.setObjectName(u"frame_menu_tabs")
        self.frame_menu_tabs.setGeometry(QRect(0, 0, 50, 500))
        self.frame_menu_tabs.setMaximumSize(QSize(50, 16777215))
        self.frame_menu_tabs.setFrameShape(QFrame.StyledPanel)
        self.frame_menu_tabs.setFrameShadow(QFrame.Raised)
        self.frame_menu_options = QFrame(self.frame_menu)
        self.frame_menu_options.setObjectName(u"frame_menu_options")
        self.frame_menu_options.setGeometry(QRect(40, 0, 150, 500))
        self.frame_menu_options.setMinimumSize(QSize(0, 0))
        self.frame_menu_options.setToolTipDuration(1)
        self.frame_menu_options.setLayoutDirection(Qt.LeftToRight)
        self.frame_menu_options.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.534364, y1:0, x2:0.528909, y2:1, stop:0.00568182 rgba(73, 73, 73, 255), stop:0.5 rgba(115, 115, 115, 255), stop:1 rgba(99, 99, 99, 255));\n"
"border-radius: 10px;")
        self.frame_menu_options.setFrameShape(QFrame.NoFrame)
        self.frame_menu_options.setFrameShadow(QFrame.Raised)
        self.button_info = QPushButton(self.frame_menu_options)
        self.button_info.setObjectName(u"button_info")
        self.button_info.setGeometry(QRect(25, 450, 100, 25))
        self.button_info.setMinimumSize(QSize(7, 0))
        font3 = QFont()
        font3.setFamily(u"MS Shell Dlg 2")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.button_info.setFont(font3)
        self.button_info.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	color: rgb(43, 43, 43);\n"
"	background-color: qlineargradient(spread:pad, x1:0.534364, y1:0, x2:0.528909, y2:1, stop:0.00568182 rgba(129, 129, 129, 255), stop:0.5 rgba(162, 162, 162, 255), stop:1 rgba(173, 173, 173, 255));\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: rgb(185, 185, 185);\n"
"}")
        self.lineEdit_input_file = QLineEdit(self.frame_menu_options)
        self.lineEdit_input_file.setObjectName(u"lineEdit_input_file")
        self.lineEdit_input_file.setGeometry(QRect(10, 55, 109, 20))
        self.lineEdit_input_file.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.534364, y1:0, x2:0.528909, y2:1, stop:0.00568182 rgba(129, 129, 129, 255), stop:0.5 rgba(162, 162, 162, 255), stop:1 rgba(173, 173, 173, 255));\n"
"border-radius: 0px;")
        self.button_choose_input_file = QPushButton(self.frame_menu_options)
        self.button_choose_input_file.setObjectName(u"button_choose_input_file")
        self.button_choose_input_file.setGeometry(QRect(120, 55, 20, 20))
        self.button_choose_input_file.setMinimumSize(QSize(7, 0))
        font4 = QFont()
        font4.setFamily(u"MS Shell Dlg 2")
        font4.setPointSize(11)
        font4.setBold(True)
        font4.setUnderline(False)
        font4.setWeight(75)
        font4.setStrikeOut(False)
        font4.setKerning(True)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.button_choose_input_file.setFont(font4)
        self.button_choose_input_file.setToolTipDuration(2)
        self.button_choose_input_file.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	color: rgb(43, 43, 43);\n"
"	background-color: qlineargradient(spread:pad, x1:0.534364, y1:0, x2:0.528909, y2:1, stop:0.00568182 rgba(129, 129, 129, 255), stop:0.5 rgba(162, 162, 162, 255), stop:1 rgba(173, 173, 173, 255));\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: rgb(185, 185, 185);\n"
"}")
        self.label_input = QLabel(self.frame_menu_options)
        self.label_input.setObjectName(u"label_input")
        self.label_input.setGeometry(QRect(45, 30, 61, 16))
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_input.setFont(font5)
        self.label_input.setStyleSheet(u"background-color: none;\n"
"color:rgb(167, 167, 167);")
        self.button_start = QPushButton(self.frame_menu_options)
        self.button_start.setObjectName(u"button_start")
        self.button_start.setGeometry(QRect(25, 150, 100, 25))
        self.button_start.setMinimumSize(QSize(7, 0))
        self.button_start.setFont(font3)
        self.button_start.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	color: rgb(43, 43, 43);\n"
"	background-color: qlineargradient(spread:pad, x1:0.534364, y1:0, x2:0.528909, y2:1, stop:0.00568182 rgba(129, 129, 129, 255), stop:0.5 rgba(162, 162, 162, 255), stop:1 rgba(173, 173, 173, 255));\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: rgb(185, 185, 185);\n"
"}")
        self.label_output = QLabel(self.frame_menu_options)
        self.label_output.setObjectName(u"label_output")
        self.label_output.setGeometry(QRect(43, 90, 81, 16))
        self.label_output.setFont(font5)
        self.label_output.setStyleSheet(u"background-color: none;\n"
"color: rgb(167, 167, 167);")
        self.button_view_obj = QPushButton(self.frame_menu_options)
        self.button_view_obj.setObjectName(u"button_view_obj")
        self.button_view_obj.setGeometry(QRect(25, 200, 100, 25))
        self.button_view_obj.setMinimumSize(QSize(7, 0))
        self.button_view_obj.setFont(font3)
        self.button_view_obj.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	color: rgb(43, 43, 43);\n"
"	background-color: qlineargradient(spread:pad, x1:0.534364, y1:0, x2:0.528909, y2:1, stop:0.00568182 rgba(129, 129, 129, 255), stop:0.5 rgba(162, 162, 162, 255), stop:1 rgba(173, 173, 173, 255));\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: rgb(185, 185, 185);\n"
"}")
        self.lineEdit_output_file = QLineEdit(self.frame_menu_options)
        self.lineEdit_output_file.setObjectName(u"lineEdit_output_file")
        self.lineEdit_output_file.setGeometry(QRect(10, 115, 109, 20))
        self.lineEdit_output_file.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.534364, y1:0, x2:0.528909, y2:1, stop:0.00568182 rgba(129, 129, 129, 255), stop:0.5 rgba(162, 162, 162, 255), stop:1 rgba(173, 173, 173, 255));\n"
"border-radius: 0px;")
        self.button_choose_output_file = QPushButton(self.frame_menu_options)
        self.button_choose_output_file.setObjectName(u"button_choose_output_file")
        self.button_choose_output_file.setGeometry(QRect(120, 115, 20, 20))
        self.button_choose_output_file.setMinimumSize(QSize(7, 0))
        self.button_choose_output_file.setFont(font4)
        self.button_choose_output_file.setToolTipDuration(2)
        self.button_choose_output_file.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	color: rgb(43, 43, 43);\n"
"	background-color: qlineargradient(spread:pad, x1:0.534364, y1:0, x2:0.528909, y2:1, stop:0.00568182 rgba(129, 129, 129, 255), stop:0.5 rgba(162, 162, 162, 255), stop:1 rgba(173, 173, 173, 255));\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: rgb(185, 185, 185);\n"
"}")

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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TechDraw3D v0.2.2", None))
        MainWindow.setWindowIcon(QIcon('./libs/gui/icons/icon_square.png'))

        self.label_icon.setText("")
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"TechDraw3D", None))
        self.button_close.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.button_minimalize.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.button_info.setText(QCoreApplication.translate("MainWindow", u"INFO", None))
        self.button_choose_input_file.setText(QCoreApplication.translate("MainWindow", u"\u25ba", None))
        self.label_input.setText(QCoreApplication.translate("MainWindow", u"Input file:", None))
        self.button_start.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.label_output.setText(QCoreApplication.translate("MainWindow", u"Output file:", None))
        self.button_view_obj.setText(QCoreApplication.translate("MainWindow", u"VIEW OBJ", None))
        self.button_choose_output_file.setText(QCoreApplication.translate("MainWindow", u"\u25ba", None))
    # retranslateUi

