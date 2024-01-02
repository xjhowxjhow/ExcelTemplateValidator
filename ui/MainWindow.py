# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uidesinger_multiclientWUAcXx.ui'
##
## Created by: Jhonatan Deni | Qt Designer version: 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import ui.sources

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.setWindowModality(Qt.NonModal)
        mainWindow.resize(1003, 568)
        mainWindow.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamily(u"Bahnschrift Light")
        mainWindow.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/iconexe/ico.ico", QSize(), QIcon.Normal, QIcon.Off)
        mainWindow.setWindowIcon(icon1)
        mainWindow.setStyleSheet(u"/*\n"
"Ubuntu Style Sheet for QT Applications\n"
"Author: Jaime A. Quiroga P.\n"
"Company: GTRONICK\n"
"Last updated: 01/10/2021 (dd/mm/yyyy), 15:18.\n"
"Available at: https://github.com/GTRONICK/QSS/blob/master/Ubuntu.qss\n"
"*/\n"
"QMainWindow {\n"
"	background-color:#f0f0f0;\n"
"}\n"
"QCheckBox {\n"
"	padding:2px;\n"
"}\n"
"QCheckBox:hover {\n"
"	border:1px solid rgb(255,150,60);\n"
"	border-radius:4px;\n"
"	padding: 1px;\n"
"	background-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(190, 90, 50, 50), stop:1 rgba(250, 130, 40, 50));\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	border:1px solid rgb(246, 134, 86);\n"
"	border-radius:4px;\n"
"  	background-color:rgb(246, 134, 86)\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"	border-width:1px solid rgb(246, 134, 86);\n"
"	border-radius:4px;\n"
"  	background-color:rgb(255,255,255);\n"
"}\n"
"QColorDialog {\n"
"	background-color:#f0f0f0;\n"
"}\n"
"QDateTimeEdit, QDateEdit, QDoubleSpinBox, QFontComboBox {\n"
"	color:rgb(81,72,65);\n"
""
                        "	background-color: #ffffff;\n"
"}\n"
"\n"
"QDialog {\n"
"	background-color:#f0f0f0;\n"
"}\n"
"\n"
"QLabel,QLineEdit {\n"
"	color:rgb(17,17,17);\n"
"}\n"
"QLineEdit {\n"
"	background-color:rgb(255,255,255);\n"
"	selection-background-color:rgb(236,116,64);\n"
"}\n"
"QMenuBar {\n"
"	color:rgb(223,219,210);\n"
"	background-color:rgb(65,64,59);\n"
"}\n"
"QMenuBar::item {\n"
"	padding-top:4px;\n"
"	padding-left:4px;\n"
"	padding-right:4px;\n"
"	color:rgb(223,219,210);\n"
"	background-color:rgb(65,64,59);\n"
"}\n"
"QMenuBar::item:selected {\n"
"	color:rgb(255,255,255);\n"
"	padding-top:2px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	border-top-width:2px;\n"
"	border-left-width:2px;\n"
"	border-right-width:2px;\n"
"	border-top-right-radius:4px;\n"
"	border-top-left-radius:4px;\n"
"	border-style:solid;\n"
"	background-color:rgb(65,64,59);\n"
"	border-top-color: rgb(47,47,44);\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(90, 87, 78, 255), stop:1 rgba(47,47,44, 255));\n"
""
                        "	border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(90, 87, 78, 255), stop:1 rgba(47,47,44, 255));\n"
"}\n"
"QMenu {\n"
"	color:rgb(223,219,210);\n"
"	background-color:rgb(65,64,59);\n"
"}\n"
"QMenu::item {\n"
"	color:rgb(223,219,210);\n"
"	padding:4px 10px 4px 20px;\n"
"}\n"
"QMenu::item:selected {\n"
"	color:rgb(255,255,255);\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(225, 108, 54, 255), stop:1 rgba(246, 134, 86, 255));\n"
"	border-style:solid;\n"
"	border-width:3px;\n"
"	padding:4px 7px 4px 17px;\n"
"	border-bottom-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(175,85,48,255), stop:1 rgba(236,114,67, 255));\n"
"	border-top-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));\n"
"	border-right-color:qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));\n"
"	border-left-colo"
                        "r:qlineargradient(spread:pad, x1:1, y1:0.5, x2:0, y2:0.5, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));\n"
"}\n"
"QPlainTextEdit {\n"
"	border: 1px solid transparent;\n"
"	color:rgb(17,17,17);\n"
"	selection-background-color:rgb(236,116,64);\n"
"    background-color: #FFFFFF;\n"
"}\n"
"QProgressBar {\n"
"	text-align: center;\n"
"	color: rgb(0, 0, 0);\n"
"	border: 1px inset rgb(150,150,150); \n"
"	border-radius: 10px;\n"
"	background-color:rgb(221,221,219);\n"
"}\n"
"QProgressBar::chunk:horizontal {\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(225, 108, 54, 255), stop:1 rgba(246, 134, 86, 255));\n"
"	border:1px solid;\n"
"	border-radius:8px;\n"
"	border-bottom-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(175,85,48,255), stop:1 rgba(236,114,67, 255));\n"
"	border-top-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));\n"
"	border-right-color:qlineargradien"
                        "t(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));\n"
"	border-left-color:qlineargradient(spread:pad, x1:1, y1:0.5, x2:0, y2:0.5, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));\n"
"}\n"
"QPushButton{\n"
"\n"
"	color:rgb(17,17,17);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-bottom-color: rgb(150,150,150);\n"
"	border-right-color: rgb(165,165,165);\n"
"	border-left-color: rgb(165,165,165);\n"
"	border-top-color: rgb(180,180,180);\n"
"	border-style: solid;\n"
"	padding: 4px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(17,17,17);\n"
"	border-width: 1px;\n"
"	border-radius:6px;\n"
"	border-top-color: rgb(255,150,60);\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
"	border-left-color:  qlineargradie"
                        "nt(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
"	border-bottom-color: rgb(200,70,20);\n"
"	border-style: solid;\n"
"	padding: 2px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:default{\n"
"	color:rgb(17,17,17);\n"
"	border-width: 1px;\n"
"	border-radius:6px;\n"
"	border-top-color: rgb(255,150,60);\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
"	border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
"	border-bottom-color: rgb(200,70,20);\n"
"	border-style: solid;\n"
"	padding: 2px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:pressed{\n"
""
                        "	color:rgb(17,17,17);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-width: 1px;\n"
"	border-top-color: rgba(255,150,60,200);\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 200));\n"
"	border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 200));\n"
"	border-bottom-color: rgba(200,70,20,200);\n"
"	border-style: solid;\n"
"	padding: 2px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:disabled{\n"
"	color:rgb(174,167,159);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(200, 200, 200, 255), stop:1 rgba(230, 230, 230, 255));\n"
"}\n"
"QRadioButton {\n"
"	padding: 1px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"	height: 10px;\n"
"	w"
                        "idth: 10px;\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: rgba(246, 134, 86, 255);\n"
"	color: #a9b7c6;\n"
"	background-color:rgba(246, 134, 86, 255);\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: rgb(246, 134, 86);\n"
"	color: #a9b7c6;\n"
"	background-color: transparent;\n"
"}\n"
"QScrollArea {\n"
"	color: white;\n"
"	background-color:#f0f0f0;\n"
"}\n"
"QSlider::groove {\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(207,207,207);\n"
"}\n"
"QSlider::groove:horizontal {\n"
"	height: 5px;\n"
"	background: rgb(246, 134, 86);\n"
"}\n"
"QSlider::groove:vertical {\n"
"	width: 5px;\n"
"	background: rgb(246, 134, 86);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"	background: rgb(253,253,253);\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(207,207,207);\n"
"	width: 12px;\n"
"	margin: -5px 0;\n"
"	b"
                        "order-radius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"	background: rgb(253,253,253);\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(207,207,207);\n"
"	height: 12px;\n"
"	margin: 0 -5px;\n"
"	border-radius: 7px;\n"
"}\n"
"QSlider::add-page:horizontal, QSlider::add-page:vertical {\n"
" 	background: white;\n"
"}\n"
"QSlider::sub-page:horizontal, QSlider::sub-page:vertical {\n"
"	background: rgb(246, 134, 86);\n"
"}\n"
"QStatusBar, QSpinBox {\n"
"	color:rgb(81,72,65);\n"
"}\n"
"QSpinBox {\n"
"	background-color: #ffffff;\n"
"}\n"
"QScrollBar:horizontal {\n"
"	max-height: 20px;\n"
"	border: 1px transparent;\n"
"	margin: 0px 20px 0px 20px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"	background: rgb(253,253,253);\n"
"	border: 1px solid rgb(207,207,207);\n"
"	border-radius: 7px;\n"
"	min-width: 25px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"	background: rgb(253,253,253);\n"
"	border: 1px solid rgb(255,150,60);\n"
"	border-radius: 7px;\n"
"	min-width: 25px;\n"
"}\n"
"QScroll"
                        "Bar::add-line:horizontal {\n"
"  	border: 1px solid rgb(207,207,207);\n"
"  	border-top-right-radius: 7px;\n"
"  	border-top-left-radius: 7px;\n"
"  	border-bottom-right-radius: 7px;\n"
"  	background: rgb(255, 255, 255);\n"
"  	width: 20px;\n"
"  	subcontrol-position: right;\n"
"  	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:hover {\n"
"  	border: 1px solid rgb(255,150,60);\n"
"  	border-top-right-radius: 7px;\n"
"  	border-top-left-radius: 7px;\n"
"  	border-bottom-right-radius: 7px;\n"
"  	background: rgb(255, 255, 255);\n"
"  	width: 20px;\n"
"  	subcontrol-position: right;\n"
"  	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"  	border: 1px solid grey;\n"
"  	border-top-left-radius: 7px;\n"
"  	border-top-right-radius: 7px;\n"
"  	border-bottom-right-radius: 7px;\n"
"  	background: rgb(231,231,231);\n"
"  	width: 20px;\n"
"  	subcontrol-position: right;\n"
"  	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"  	border: "
                        "1px solid rgb(207,207,207);\n"
"  	border-top-right-radius: 7px;\n"
"  	border-top-left-radius: 7px;\n"
"  	border-bottom-left-radius: 7px;\n"
"  	background: rgb(255, 255, 255);\n"
"  	width: 20px;\n"
"  	subcontrol-position: left;\n"
"  	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"  	border: 1px solid rgb(255,150,60);\n"
"  	border-top-right-radius: 7px;\n"
"  	border-top-left-radius: 7px;\n"
"  	border-bottom-left-radius: 7px;\n"
"  	background: rgb(255, 255, 255);\n"
"  	width: 20px;\n"
"  	subcontrol-position: left;\n"
"  	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"  	border: 1px solid grey;\n"
"  	border-top-right-radius: 7px;\n"
"  	border-top-left-radius: 7px;\n"
"  	border-bottom-left-radius: 7px;\n"
"  	background: rgb(231,231,231);\n"
"  	width: 20px;\n"
"  	subcontrol-position: left;\n"
"  	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::left-arrow:horizontal {\n"
"  	border: 1px transparent grey;\n"
"  	border-top-left-r"
                        "adius: 3px;\n"
"  	border-bottom-left-radius: 3px;\n"
"  	width: 6px;\n"
"  	height: 6px;\n"
"  	background: rgb(230,230,230);\n"
"}\n"
"QScrollBar::right-arrow:horizontal {\n"
"	border: 1px transparent grey;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;\n"
"  	width: 6px;\n"
"  	height: 6px;\n"
" 	background: rgb(230,230,230);\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
" 	background: none;\n"
"} \n"
"QScrollBar:vertical {\n"
"	max-width: 20px;\n"
"	border: 1px transparent grey;\n"
"	margin: 20px 0px 20px 0px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"	border: 1px solid;\n"
"	border-color: rgb(207,207,207);\n"
"	border-bottom-right-radius: 7px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-top-left-radius: 7px;\n"
"	background: rgb(255, 255, 255);\n"
"  	height: 20px;\n"
"  	subcontrol-position: bottom;\n"
"  	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {\n"
"  	border: 1px solid;\n"
"  	border-color: rgb(255,15"
                        "0,60);\n"
"  	border-bottom-right-radius: 7px;\n"
"  	border-bottom-left-radius: 7px;\n"
"  	border-top-left-radius: 7px;\n"
"  	background: rgb(255, 255, 255);\n"
"  	height: 20px;\n"
"  	subcontrol-position: bottom;\n"
"  	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {\n"
"  	border: 1px solid grey;\n"
"  	border-bottom-left-radius: 7px;\n"
"  	border-bottom-right-radius: 7px;\n"
"  	border-top-left-radius: 7px;\n"
"  	background: rgb(231,231,231);\n"
"  	height: 20px;\n"
"  	subcontrol-position: bottom;\n"
"  	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"  	border: 1px solid rgb(207,207,207);\n"
"  	border-top-right-radius: 7px;\n"
"  	border-top-left-radius: 7px;\n"
"  	border-bottom-left-radius: 7px;\n"
"  	background: rgb(255, 255, 255);\n"
"  	height: 20px;\n"
"  	subcontrol-position: top;\n"
"  	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {\n"
"  	border: 1px solid rgb(255,150,60);\n"
"  	border-top-right-radius: 7px"
                        ";\n"
"  	border-top-left-radius: 7px;\n"
"  	border-bottom-left-radius: 7px;\n"
"	background: rgb(255, 255, 255);\n"
"  	height: 20px;\n"
"  	subcontrol-position: top;\n"
"  	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"  	border: 1px solid grey;\n"
"  	border-top-left-radius: 7px;\n"
"  	border-top-right-radius: 7px;\n"
"  	background: rgb(231,231,231);\n"
" 	height: 20px;\n"
"  	subcontrol-position: top;\n"
"  	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"	background: rgb(253,253,253);\n"
"	border: 1px solid rgb(207,207,207);\n"
"	border-radius: 7px;\n"
"	min-height: 25px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"	background: rgb(253,253,253);\n"
"	border: 1px solid rgb(255,150,60);\n"
"	border-radius: 7px;\n"
"	min-height: 25px;\n"
"}\n"
"QScrollBar::up-arrow:vertical {\n"
"	border: 1px transparent grey;\n"
"  	border-top-left-radius: 3px;\n"
"	border-top-right-radius: 3px;\n"
"  	width: 6px;\n"
"  	height: 6px;\n"
"  	background: rgb(23"
                        "0,230,230);\n"
"}\n"
"QScrollBar::down-arrow:vertical {\n"
"  	border: 1px transparent grey;\n"
"  	border-bottom-left-radius: 3px;\n"
"  	border-bottom-right-radius: 3px;\n"
"  	width: 6px;\n"
"  	height: 6px;\n"
"  	background: rgb(230,230,230);\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"  	background: none;\n"
"}\n"
"QTabWidget {\n"
"	color:rgb(0,0,0);\n"
"	background-color:rgb(247,246,246);\n"
"}\n"
"QTabWidget::pane {\n"
"	border-color: rgb(180,180,180);\n"
"	background-color:rgb(247,246,246);\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"  	border-radius: 6px;\n"
"}\n"
"QTabBar::tab {\n"
"	padding-left:6px;\n"
"	padding-right:6px;\n"
"	padding-bottom:6px;\n"
"	padding-top:6px;\n"
"	color:rgb(81,72,65);\n"
"  	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(221,218,217,255), stop:1 rgba(240,239,238,255));\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"  	border-top-right-radius:4px;\n"
"	border-top-left-radius:4px;\n"
""
                        "	border-top-color: rgb(180,180,180);\n"
"	border-left-color: rgb(180,180,180);\n"
"	border-right-color: rgb(180,180,180);\n"
"	border-bottom-color: transparent;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"  	background-color:rgb(247,246,246);\n"
"  	margin-left: 0px;\n"
"  	margin-right: 1px;\n"
"}\n"
"QTabBar::tab:!selected {\n"
"	margin-top: 1px;\n"
"	margin-right: 1px;\n"
"}\n"
"QTextEdit {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color:transparent;\n"
"	color:rgb(17,17,17);\n"
"	selection-background-color:rgb(236,116,64);\n"
"}\n"
"QTimeEdit, QToolBox, QToolBox::tab, QToolBox::tab:selected {\n"
"	color:rgb(81,72,65);\n"
"	background-color: #ffffff;\n"
"}")
        mainWindow.setDocumentMode(False)
        mainWindow.setTabShape(QTabWidget.Rounded)
        mainWindow.setDockNestingEnabled(False)
        mainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.actionasda = QAction(mainWindow)
        self.actionasda.setObjectName(u"actionasda")
        self.actionasd = QAction(mainWindow)
        self.actionasd.setObjectName(u"actionasd")
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font1 = QFont()
        font1.setFamily(u"Bahnschrift Light")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setWeight(50)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.centralwidget.setFont(font1)
        self.centralwidget.setFocusPolicy(Qt.NoFocus)
        self.centralwidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Sunken)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1003, 568))
        self.horizontalLayout_7 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.togleframe = QFrame(self.scrollAreaWidgetContents)
        self.togleframe.setObjectName(u"togleframe")
        self.togleframe.setMinimumSize(QSize(60, 0))
        self.togleframe.setMaximumSize(QSize(70, 16777215))
        self.togleframe.setStyleSheet(u"")
        self.togleframe.setFrameShape(QFrame.StyledPanel)
        self.togleframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.togleframe)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.btn_page_home = QPushButton(self.togleframe)
        self.btn_page_home.setObjectName(u"btn_page_home")
        self.btn_page_home.setMinimumSize(QSize(0, 40))
        self.btn_page_home.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/newicons/newicons/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_page_home.setIcon(icon2)
        self.btn_page_home.setIconSize(QSize(20, 20))
        self.btn_page_home.setCheckable(False)
        self.btn_page_home.setAutoDefault(False)
        self.btn_page_home.setFlat(False)

        self.verticalLayout_8.addWidget(self.btn_page_home)

        self.btn_page_clients = QPushButton(self.togleframe)
        self.btn_page_clients.setObjectName(u"btn_page_clients")
        self.btn_page_clients.setMinimumSize(QSize(0, 40))
        self.btn_page_clients.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/newicons/newicons/cube-validate.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_page_clients.setIcon(icon3)

        self.verticalLayout_8.addWidget(self.btn_page_clients)

        self.btn_page_config = QPushButton(self.togleframe)
        self.btn_page_config.setObjectName(u"btn_page_config")
        self.btn_page_config.setMinimumSize(QSize(0, 40))
        self.btn_page_config.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/newicons/newicons/config.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_page_config.setIcon(icon4)
        self.btn_page_config.setIconSize(QSize(20, 20))

        self.verticalLayout_8.addWidget(self.btn_page_config)

        self.verticalSpacer = QSpacerItem(20, 770, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.btn_exit_program = QPushButton(self.togleframe)
        self.btn_exit_program.setObjectName(u"btn_exit_program")
        self.btn_exit_program.setMinimumSize(QSize(0, 40))
        self.btn_exit_program.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/newicons/newicons/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_exit_program.setIcon(icon5)

        self.verticalLayout_8.addWidget(self.btn_exit_program)


        self.horizontalLayout_7.addWidget(self.togleframe)

        self.content = QStackedWidget(self.scrollAreaWidgetContents)
        self.content.setObjectName(u"content")
        self.content.setMinimumSize(QSize(0, 0))
        self.content.setStyleSheet(u"")
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.verticalLayout_7 = QVBoxLayout(self.page1)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pagecontents = QFrame(self.page1)
        self.pagecontents.setObjectName(u"pagecontents")
        self.pagecontents.setMinimumSize(QSize(0, 500))
        self.pagecontents.setFrameShape(QFrame.StyledPanel)
        self.pagecontents.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.pagecontents)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.frame_14 = QFrame(self.pagecontents)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 50))
        self.frame_14.setMaximumSize(QSize(16777215, 50))
        self.frame_14.setStyleSheet(u"")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_14)
        self.label_8.setObjectName(u"label_8")
        font2 = QFont()
        font2.setFamily(u"Bahnschrift Light")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setWeight(50)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.label_8)

        self.horizontalSpacer_7 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_7)


        self.verticalLayout_2.addWidget(self.frame_14)

        self.tables = QGroupBox(self.pagecontents)
        self.tables.setObjectName(u"tables")
        self.tables.setMaximumSize(QSize(16777215, 100))
        self.tables.setStyleSheet(u"")
        self.tables.setFlat(True)
        self.tables.setCheckable(False)
        self.verticalLayout_4 = QVBoxLayout(self.tables)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.frame_8 = QFrame(self.tables)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 50))
        self.frame_8.setStyleSheet(u"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.metodo_tabela = QRadioButton(self.frame_8)
        self.metodo_tabela.setObjectName(u"metodo_tabela")
        self.metodo_tabela.setStyleSheet(u"")
        self.metodo_tabela.setChecked(True)

        self.horizontalLayout_3.addWidget(self.metodo_tabela)


        self.verticalLayout_4.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.tables)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.combo_templates = QComboBox(self.frame_9)
        self.combo_templates.setObjectName(u"combo_templates")
        self.combo_templates.setMinimumSize(QSize(0, 25))
        self.combo_templates.setStyleSheet(u"")
        self.combo_templates.setInsertPolicy(QComboBox.InsertAtBottom)

        self.horizontalLayout_4.addWidget(self.combo_templates)


        self.verticalLayout_4.addWidget(self.frame_9)


        self.verticalLayout_2.addWidget(self.tables)

        self.logvierw = QTabWidget(self.pagecontents)
        self.logvierw.setObjectName(u"logvierw")
        self.logvierw.setStyleSheet(u"")
        self.logvierw.setTabPosition(QTabWidget.North)
        self.logvierw.setTabShape(QTabWidget.Rounded)
        self.logvierw.setElideMode(Qt.ElideLeft)
        self.logvierw.setTabsClosable(False)
        self.logvierw.setMovable(True)
        self.logvierw.setTabBarAutoHide(True)
        self.inputmodel = QWidget()
        self.inputmodel.setObjectName(u"inputmodel")
        self.verticalLayout_5 = QVBoxLayout(self.inputmodel)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.groupBox_11 = QGroupBox(self.inputmodel)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setMaximumSize(QSize(16777215, 50))
        self.groupBox_11.setStyleSheet(u"")
        self.groupBox_11.setFlat(True)
        self.groupBox_11.setCheckable(False)
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_11 = QLabel(self.groupBox_11)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"")
        self.label_11.setTextFormat(Qt.AutoText)
        self.label_11.setScaledContents(False)
        self.label_11.setWordWrap(False)

        self.horizontalLayout_6.addWidget(self.label_11)

        self.horizontalSpacer_4 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)


        self.verticalLayout_5.addWidget(self.groupBox_11)

        self.frame_12 = QFrame(self.inputmodel)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_12)
        self.verticalLayout_6.setSpacing(15)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.set_view_template = QVBoxLayout()
        self.set_view_template.setSpacing(0)
        self.set_view_template.setObjectName(u"set_view_template")

        self.verticalLayout_6.addLayout(self.set_view_template)

        self.progressBar = QProgressBar(self.frame_12)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setLayoutDirection(Qt.LeftToRight)
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.progressBar)


        self.verticalLayout_5.addWidget(self.frame_12)

        self.logvierw.addTab(self.inputmodel, "")
        self.pageresults = QWidget()
        self.pageresults.setObjectName(u"pageresults")
        self.verticalLayout_16 = QVBoxLayout(self.pageresults)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.groupBox_21 = QGroupBox(self.pageresults)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.groupBox_21.setMaximumSize(QSize(16777215, 50))
        self.groupBox_21.setStyleSheet(u"")
        self.groupBox_21.setFlat(True)
        self.horizontalLayout_15 = QHBoxLayout(self.groupBox_21)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_12 = QLabel(self.groupBox_21)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"")
        self.label_12.setTextFormat(Qt.AutoText)
        self.label_12.setScaledContents(False)
        self.label_12.setWordWrap(False)

        self.horizontalLayout_15.addWidget(self.label_12)

        self.horizontalSpacer_5 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_5)


        self.verticalLayout_16.addWidget(self.groupBox_21)

        self.frame_16 = QFrame(self.pageresults)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_16)
        self.verticalLayout_12.setSpacing(15)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.set_validador_template_ = QVBoxLayout()
        self.set_validador_template_.setObjectName(u"set_validador_template_")

        self.verticalLayout_12.addLayout(self.set_validador_template_)

        self.progressBar_2 = QProgressBar(self.frame_16)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setLayoutDirection(Qt.LeftToRight)
        self.progressBar_2.setValue(0)
        self.progressBar_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.progressBar_2)


        self.verticalLayout_16.addWidget(self.frame_16)

        self.logvierw.addTab(self.pageresults, "")
        self.page_logger = QWidget()
        self.page_logger.setObjectName(u"page_logger")
        self.verticalLayout_11 = QVBoxLayout(self.page_logger)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.loger_layout_customwid = QVBoxLayout()
        self.loger_layout_customwid.setObjectName(u"loger_layout_customwid")

        self.verticalLayout_11.addLayout(self.loger_layout_customwid)

        self.logvierw.addTab(self.page_logger, "")

        self.verticalLayout_2.addWidget(self.logvierw)

        self.bottomconfig = QFrame(self.pagecontents)
        self.bottomconfig.setObjectName(u"bottomconfig")
        self.bottomconfig.setMaximumSize(QSize(16777215, 50))
        self.bottomconfig.setMouseTracking(False)
        self.bottomconfig.setStyleSheet(u"")
        self.horizontalLayout_5 = QHBoxLayout(self.bottomconfig)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.bottomconfig)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.icon = QLabel(self.bottomconfig)
        self.icon.setObjectName(u"icon")
        font3 = QFont()
        font3.setFamily(u"Yu Gothic")
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setUnderline(False)
        font3.setWeight(50)
        font3.setStrikeOut(False)
        font3.setKerning(True)
        font3.setStyleStrategy(QFont.PreferAntialias)
        self.icon.setFont(font3)
        self.icon.setPixmap(QPixmap(u":/newicons/newicons/openfolder.png"))

        self.horizontalLayout_5.addWidget(self.icon)

        self.label_file_directory = QLabel(self.bottomconfig)
        self.label_file_directory.setObjectName(u"label_file_directory")
        self.label_file_directory.setMaximumSize(QSize(400, 16777215))
        font4 = QFont()
        font4.setFamily(u"Bahnschrift Light")
        font4.setPointSize(6)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setUnderline(False)
        font4.setWeight(50)
        font4.setStrikeOut(False)
        font4.setKerning(True)
        font4.setStyleStrategy(QFont.PreferAntialias)
        self.label_file_directory.setFont(font4)
        self.label_file_directory.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.label_file_directory)

        self.spaceing = QSpacerItem(749, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.spaceing)

        self.start = QPushButton(self.bottomconfig)
        self.start.setObjectName(u"start")
        self.start.setMinimumSize(QSize(0, 30))
        self.start.setMaximumSize(QSize(100, 16777215))
        self.start.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/newicons/newicons/import-file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.start.setIcon(icon6)
        self.start.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.start)

        self.start_validation = QPushButton(self.bottomconfig)
        self.start_validation.setObjectName(u"start_validation")
        self.start_validation.setMinimumSize(QSize(0, 30))
        self.start_validation.setMaximumSize(QSize(100, 16777215))
        self.start_validation.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/newicons/newicons/start.png", QSize(), QIcon.Normal, QIcon.Off)
        self.start_validation.setIcon(icon7)
        self.start_validation.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.start_validation)

        self.export_xlsx = QPushButton(self.bottomconfig)
        self.export_xlsx.setObjectName(u"export_xlsx")
        self.export_xlsx.setMinimumSize(QSize(0, 30))
        self.export_xlsx.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/newicons/newicons/excel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.export_xlsx.setIcon(icon8)
        self.export_xlsx.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.export_xlsx)

        self.jsontoxls = QPushButton(self.bottomconfig)
        self.jsontoxls.setObjectName(u"jsontoxls")
        self.jsontoxls.setMinimumSize(QSize(0, 30))
        icon9 = QIcon()
        icon9.addFile(u":/newicons/newicons/excelimport.png", QSize(), QIcon.Normal, QIcon.Off)
        self.jsontoxls.setIcon(icon9)
        self.jsontoxls.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.jsontoxls)


        self.verticalLayout_2.addWidget(self.bottomconfig)


        self.verticalLayout_7.addWidget(self.pagecontents)

        self.content.addWidget(self.page1)
        self.page_view_clients = QWidget()
        self.page_view_clients.setObjectName(u"page_view_clients")
        self.page_view_clients.setStyleSheet(u"")
        self.verticalLayout_13 = QVBoxLayout(self.page_view_clients)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, -1, -1, -1)
        self.task = QFrame(self.page_view_clients)
        self.task.setObjectName(u"task")
        self.task.setMaximumSize(QSize(16777215, 40))
        self.task.setStyleSheet(u"")
        self.task.setFrameShape(QFrame.StyledPanel)
        self.task.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.task)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.labe_task = QLabel(self.task)
        self.labe_task.setObjectName(u"labe_task")
        self.labe_task.setMinimumSize(QSize(0, 50))
        self.labe_task.setMaximumSize(QSize(250, 16777215))
        self.labe_task.setFont(font2)
        self.labe_task.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.labe_task)

        self.line = QFrame(self.task)
        self.line.setObjectName(u"line")
        self.line.setLineWidth(0)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line)

        self.frame_2 = QFrame(self.task)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(100, 20))
        self.frame_2.setMaximumSize(QSize(100, 20))
        self.frame_2.setStyleSheet(u"border-image: url(:/icons/logo.webp);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.frame_2)


        self.verticalLayout_13.addWidget(self.task)

        self.header_view_client = QGroupBox(self.page_view_clients)
        self.header_view_client.setObjectName(u"header_view_client")
        self.header_view_client.setMinimumSize(QSize(0, 0))
        self.header_view_client.setMaximumSize(QSize(16777215, 16777215))
        self.header_view_client.setStyleSheet(u"")
        self.header_view_client.setFlat(True)
        self.horizontalLayout_10 = QHBoxLayout(self.header_view_client)
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 6, 0, 6)
        self.group_frame_seachr = QFrame(self.header_view_client)
        self.group_frame_seachr.setObjectName(u"group_frame_seachr")
        self.group_frame_seachr.setMinimumSize(QSize(0, 30))
        self.group_frame_seachr.setMaximumSize(QSize(300, 30))
        self.group_frame_seachr.setStyleSheet(u"")
        self.group_frame_seachr.setFrameShape(QFrame.StyledPanel)
        self.group_frame_seachr.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.group_frame_seachr)
        self.horizontalLayout_13.setSpacing(7)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.searchtemplates = QLineEdit(self.group_frame_seachr)
        self.searchtemplates.setObjectName(u"searchtemplates")
        self.searchtemplates.setMinimumSize(QSize(0, 0))
        self.searchtemplates.setFont(font3)
        self.searchtemplates.setStyleSheet(u"")
        self.searchtemplates.setAlignment(Qt.AlignCenter)
        self.searchtemplates.setClearButtonEnabled(True)

        self.horizontalLayout_13.addWidget(self.searchtemplates)

        self.btn_procurar = QPushButton(self.group_frame_seachr)
        self.btn_procurar.setObjectName(u"btn_procurar")
        self.btn_procurar.setMinimumSize(QSize(0, 30))
        self.btn_procurar.setMaximumSize(QSize(16777215, 16777215))
        self.btn_procurar.setFont(font3)
        self.btn_procurar.setStyleSheet(u"")
        icon10 = QIcon()
        icon10.addFile(u":/newicons/newicons/lupa.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_procurar.setIcon(icon10)

        self.horizontalLayout_13.addWidget(self.btn_procurar)


        self.horizontalLayout_10.addWidget(self.group_frame_seachr)

        self.group_buttons = QFrame(self.header_view_client)
        self.group_buttons.setObjectName(u"group_buttons")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group_buttons.sizePolicy().hasHeightForWidth())
        self.group_buttons.setSizePolicy(sizePolicy)
        self.group_buttons.setMinimumSize(QSize(0, 0))
        self.group_buttons.setLayoutDirection(Qt.LeftToRight)
        self.group_buttons.setStyleSheet(u"")
        self.group_buttons.setFrameShape(QFrame.StyledPanel)
        self.group_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.group_buttons)
        self.horizontalLayout_14.setSpacing(15)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_pg_add_new_template = QPushButton(self.group_buttons)
        self.btn_pg_add_new_template.setObjectName(u"btn_pg_add_new_template")
        self.btn_pg_add_new_template.setMinimumSize(QSize(0, 30))
        self.btn_pg_add_new_template.setMaximumSize(QSize(150, 16777215))
        self.btn_pg_add_new_template.setStyleSheet(u"")
        icon11 = QIcon()
        icon11.addFile(u":/newicons/newicons/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pg_add_new_template.setIcon(icon11)
        self.btn_pg_add_new_template.setIconSize(QSize(20, 20))

        self.horizontalLayout_14.addWidget(self.btn_pg_add_new_template)


        self.horizontalLayout_10.addWidget(self.group_buttons)

        self.line_4 = QFrame(self.header_view_client)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setStyleSheet(u"")
        self.line_4.setLineWidth(0)
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_10.addWidget(self.line_4)


        self.verticalLayout_13.addWidget(self.header_view_client)

        self.table_cllientes_frame = QFrame(self.page_view_clients)
        self.table_cllientes_frame.setObjectName(u"table_cllientes_frame")
        self.table_cllientes_frame.setStyleSheet(u"")
        self.table_cllientes_frame.setFrameShape(QFrame.StyledPanel)
        self.table_cllientes_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.table_cllientes_frame)
        self.verticalLayout_23.setSpacing(10)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 10, 0, 0)
        self.listWidget = QListWidget(self.table_cllientes_frame)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMaximumSize(QSize(16777215, 100))
        self.listWidget.setStyleSheet(u"")
        self.listWidget.setFrameShape(QFrame.Box)
        self.listWidget.setFrameShadow(QFrame.Sunken)
        self.listWidget.setLineWidth(1)
        self.listWidget.setMidLineWidth(0)
        self.listWidget.setTabKeyNavigation(True)
        self.listWidget.setDragEnabled(False)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setFlow(QListView.TopToBottom)
        self.listWidget.setProperty("isWrapping", False)
        self.listWidget.setResizeMode(QListView.Fixed)
        self.listWidget.setLayoutMode(QListView.SinglePass)
        self.listWidget.setSpacing(0)
        self.listWidget.setViewMode(QListView.ListMode)
        self.listWidget.setModelColumn(0)
        self.listWidget.setUniformItemSizes(True)
        self.listWidget.setWordWrap(False)
        self.listWidget.setSelectionRectVisible(False)
        self.listWidget.setSortingEnabled(True)

        self.verticalLayout_23.addWidget(self.listWidget)

        self.stackedWidget = QStackedWidget(self.table_cllientes_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.stackedWidget.setFrameShape(QFrame.Box)
        self.stackedWidget.setFrameShadow(QFrame.Sunken)
        self.page_new_template = QWidget()
        self.page_new_template.setObjectName(u"page_new_template")
        self.page_new_template.setStyleSheet(u"")
        self.verticalLayout_17 = QVBoxLayout(self.page_new_template)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.page_new_template)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 0))
        self.label_3.setMaximumSize(QSize(16777215, 35))
        self.label_3.setStyleSheet(u"")
        self.label_3.setMargin(5)

        self.verticalLayout_17.addWidget(self.label_3)

        self.frame = QFrame(self.page_new_template)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.verticalLayout_20 = QVBoxLayout(self.frame)
        self.verticalLayout_20.setSpacing(10)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.groupBox_3 = QGroupBox(self.frame)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setStyleSheet(u"")
        self.groupBox_3.setFlat(True)
        self.verticalLayout_21 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_21.setSpacing(5)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_conexao_oracle_2 = QFrame(self.groupBox_3)
        self.frame_conexao_oracle_2.setObjectName(u"frame_conexao_oracle_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_conexao_oracle_2.sizePolicy().hasHeightForWidth())
        self.frame_conexao_oracle_2.setSizePolicy(sizePolicy1)
        self.frame_conexao_oracle_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_conexao_oracle_2.setStyleSheet(u"")
        self.verticalLayout_19 = QVBoxLayout(self.frame_conexao_oracle_2)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(-1, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_conexao_oracle_2)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy2)
        self.frame_10.setStyleSheet(u"")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_24 = QFrame(self.frame_10)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMaximumSize(QSize(400, 16777215))
        self.frame_24.setStyleSheet(u"")
        self.frame_24.setFrameShape(QFrame.NoFrame)
        self.frame_24.setFrameShadow(QFrame.Sunken)
        self.formLayout_3 = QFormLayout(self.frame_24)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.formLayout_3.setRowWrapPolicy(QFormLayout.DontWrapRows)
        self.formLayout_3.setHorizontalSpacing(5)
        self.formLayout_3.setVerticalSpacing(5)
        self.formLayout_3.setContentsMargins(0, 5, 0, 0)
        self.label_7 = QLabel(self.frame_24)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"")
        self.label_7.setWordWrap(False)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_7)

        self.name_new_template = QLineEdit(self.frame_24)
        self.name_new_template.setObjectName(u"name_new_template")
        self.name_new_template.setStyleSheet(u"")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.name_new_template)

        self.label_13 = QLabel(self.frame_24)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_13)

        self.label_14 = QLabel(self.frame_24)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_14)

        self.encodinginput_2 = QLineEdit(self.frame_24)
        self.encodinginput_2.setObjectName(u"encodinginput_2")
        self.encodinginput_2.setEnabled(False)
        self.encodinginput_2.setStyleSheet(u"")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.encodinginput_2)

        self.comboBox = QComboBox(self.frame_24)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy3)
        self.comboBox.setMinimumSize(QSize(0, 0))
        self.comboBox.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox.setStyleSheet(u"")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.comboBox)


        self.horizontalLayout_19.addWidget(self.frame_24)

        self.frame_25 = QFrame(self.frame_10)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setStyleSheet(u"")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.formLayout_5 = QFormLayout(self.frame_25)
        self.formLayout_5.setObjectName(u"formLayout_5")

        self.horizontalLayout_19.addWidget(self.frame_25)


        self.verticalLayout_19.addWidget(self.frame_10)


        self.verticalLayout_21.addWidget(self.frame_conexao_oracle_2)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")

        self.verticalLayout_21.addLayout(self.verticalLayout_22)


        self.verticalLayout_20.addWidget(self.groupBox_3)

        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(16777215, 60))
        self.groupBox_2.setStyleSheet(u"")
        self.groupBox_2.setFlat(True)
        self.horizontalLayout_18 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalSpacer_2 = QSpacerItem(532, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_2)

        self.new_fild_template = QPushButton(self.groupBox_2)
        self.new_fild_template.setObjectName(u"new_fild_template")
        self.new_fild_template.setMinimumSize(QSize(0, 30))
        self.new_fild_template.setMaximumSize(QSize(16777215, 16777215))
        self.new_fild_template.setStyleSheet(u"")
        icon12 = QIcon()
        icon12.addFile(u":/newicons/newicons/insert-row.png", QSize(), QIcon.Normal, QIcon.Off)
        self.new_fild_template.setIcon(icon12)
        self.new_fild_template.setIconSize(QSize(20, 20))

        self.horizontalLayout_18.addWidget(self.new_fild_template)

        self.delete_fild_template = QPushButton(self.groupBox_2)
        self.delete_fild_template.setObjectName(u"delete_fild_template")
        self.delete_fild_template.setMinimumSize(QSize(0, 30))
        self.delete_fild_template.setMaximumSize(QSize(16777215, 16777215))
        self.delete_fild_template.setFocusPolicy(Qt.NoFocus)
        self.delete_fild_template.setLayoutDirection(Qt.LeftToRight)
        self.delete_fild_template.setStyleSheet(u"")
        icon13 = QIcon()
        icon13.addFile(u":/newicons/newicons/remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_fild_template.setIcon(icon13)
        self.delete_fild_template.setIconSize(QSize(20, 20))

        self.horizontalLayout_18.addWidget(self.delete_fild_template)

        self.btn_gerar_template = QPushButton(self.groupBox_2)
        self.btn_gerar_template.setObjectName(u"btn_gerar_template")
        self.btn_gerar_template.setMinimumSize(QSize(0, 30))
        self.btn_gerar_template.setMaximumSize(QSize(16777215, 16777215))
        self.btn_gerar_template.setStyleSheet(u"")
        icon14 = QIcon()
        icon14.addFile(u":/newicons/newicons/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_gerar_template.setIcon(icon14)
        self.btn_gerar_template.setIconSize(QSize(20, 20))

        self.horizontalLayout_18.addWidget(self.btn_gerar_template)


        self.verticalLayout_20.addWidget(self.groupBox_2)


        self.verticalLayout_17.addWidget(self.frame)

        self.stackedWidget.addWidget(self.page_new_template)
        self.page_view_template = QWidget()
        self.page_view_template.setObjectName(u"page_view_template")
        self.page_view_template.setStyleSheet(u"")
        self.verticalLayout_18 = QVBoxLayout(self.page_view_template)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.name_template_view = QLabel(self.page_view_template)
        self.name_template_view.setObjectName(u"name_template_view")
        self.name_template_view.setStyleSheet(u"")
        self.name_template_view.setScaledContents(False)
        self.name_template_view.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.name_template_view.setWordWrap(False)
        self.name_template_view.setMargin(5)

        self.verticalLayout_18.addWidget(self.name_template_view)

        self.scrollArea_4 = QScrollArea(self.page_view_template)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setStyleSheet(u"")
        self.scrollArea_4.setFrameShape(QFrame.NoFrame)
        self.scrollArea_4.setFrameShadow(QFrame.Sunken)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 259, 52))
        self.verticalLayout_24 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.set_view_template_layout = QVBoxLayout()
        self.set_view_template_layout.setObjectName(u"set_view_template_layout")

        self.verticalLayout_24.addLayout(self.set_view_template_layout)

        self.groupBox_4 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMaximumSize(QSize(16777215, 60))
        self.groupBox_4.setStyleSheet(u"")
        self.groupBox_4.setFlat(True)
        self.horizontalLayout_20 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, 11, -1, -1)
        self.horizontalSpacer_6 = QSpacerItem(532, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_6)

        self.btn_cria_xls_template = QPushButton(self.groupBox_4)
        self.btn_cria_xls_template.setObjectName(u"btn_cria_xls_template")
        self.btn_cria_xls_template.setMinimumSize(QSize(0, 30))
        self.btn_cria_xls_template.setMaximumSize(QSize(16777215, 16777215))
        self.btn_cria_xls_template.setFont(font1)
        self.btn_cria_xls_template.setStyleSheet(u"")
        self.btn_cria_xls_template.setIcon(icon8)
        self.btn_cria_xls_template.setIconSize(QSize(20, 20))

        self.horizontalLayout_20.addWidget(self.btn_cria_xls_template)

        self.btn_deleta_template = QPushButton(self.groupBox_4)
        self.btn_deleta_template.setObjectName(u"btn_deleta_template")
        self.btn_deleta_template.setMinimumSize(QSize(0, 30))
        self.btn_deleta_template.setMaximumSize(QSize(16777215, 16777215))
        self.btn_deleta_template.setFont(font1)
        self.btn_deleta_template.setFocusPolicy(Qt.NoFocus)
        self.btn_deleta_template.setLayoutDirection(Qt.LeftToRight)
        self.btn_deleta_template.setStyleSheet(u"")
        self.btn_deleta_template.setIcon(icon13)
        self.btn_deleta_template.setIconSize(QSize(20, 20))

        self.horizontalLayout_20.addWidget(self.btn_deleta_template)


        self.verticalLayout_24.addWidget(self.groupBox_4)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_18.addWidget(self.scrollArea_4)

        self.stackedWidget.addWidget(self.page_view_template)

        self.verticalLayout_23.addWidget(self.stackedWidget)


        self.verticalLayout_13.addWidget(self.table_cllientes_frame)

        self.content.addWidget(self.page_view_clients)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.verticalLayout_9 = QVBoxLayout(self.page2)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.page2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"")
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 924, 629))
        self.verticalLayout_15 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, -1, -1, -1)
        self.header_logo_config = QFrame(self.scrollAreaWidgetContents_2)
        self.header_logo_config.setObjectName(u"header_logo_config")
        self.header_logo_config.setMinimumSize(QSize(0, 50))
        self.header_logo_config.setMaximumSize(QSize(16777215, 50))
        self.header_logo_config.setStyleSheet(u"")
        self.header_logo_config.setFrameShape(QFrame.StyledPanel)
        self.header_logo_config.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header_logo_config)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.header_logo_config)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)
        self.label.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_15.addWidget(self.header_logo_config)

        self.groupBox = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_9 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(150, 16777215))
        self.label_9.setTextFormat(Qt.AutoText)
        self.label_9.setScaledContents(False)
        self.label_9.setWordWrap(True)
        self.label_9.setOpenExternalLinks(False)

        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setFlat(False)
        self.groupBox_5.setCheckable(False)
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.config_datatype_number_allowerd_v = QCheckBox(self.groupBox_5)
        self.config_datatype_number_allowerd_v.setObjectName(u"config_datatype_number_allowerd_v")
        self.config_datatype_number_allowerd_v.setChecked(True)

        self.verticalLayout_10.addWidget(self.config_datatype_number_allowerd_v)

        self.config_datatype_number_allowerd_p = QCheckBox(self.groupBox_5)
        self.config_datatype_number_allowerd_p.setObjectName(u"config_datatype_number_allowerd_p")

        self.verticalLayout_10.addWidget(self.config_datatype_number_allowerd_p)


        self.gridLayout.addWidget(self.groupBox_5, 0, 1, 1, 1)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_15.addWidget(self.groupBox)

        self.main_group_box_export = QGroupBox(self.scrollAreaWidgetContents_2)
        self.main_group_box_export.setObjectName(u"main_group_box_export")
        self.main_group_box_export.setMinimumSize(QSize(0, 0))
        self.verticalLayout_25 = QVBoxLayout(self.main_group_box_export)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_3 = QFrame(self.main_group_box_export)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_3)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.groupBox_7 = QGroupBox(self.frame_3)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setEnabled(False)
        self.groupBox_7.setFlat(True)
        self.verticalLayout_27 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_15 = QLabel(self.groupBox_7)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_15)

        self.label_16 = QLabel(self.groupBox_7)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_16)

        self.config_export_row_limit = QSpinBox(self.groupBox_7)
        self.config_export_row_limit.setObjectName(u"config_export_row_limit")
        self.config_export_row_limit.setMaximumSize(QSize(100, 16777215))
        self.config_export_row_limit.setProperty("showGroupSeparator", False)
        self.config_export_row_limit.setMaximum(999999999)
        self.config_export_row_limit.setStepType(QAbstractSpinBox.DefaultStepType)
        self.config_export_row_limit.setValue(5000)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.config_export_row_limit)

        self.config_export_coll_limit = QSpinBox(self.groupBox_7)
        self.config_export_coll_limit.setObjectName(u"config_export_coll_limit")
        self.config_export_coll_limit.setMaximumSize(QSize(100, 16777215))
        self.config_export_coll_limit.setMaximum(999999999)
        self.config_export_coll_limit.setValue(30)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.config_export_coll_limit)


        self.verticalLayout_27.addLayout(self.formLayout_4)


        self.verticalLayout_26.addWidget(self.groupBox_7)


        self.gridLayout_2.addWidget(self.frame_3, 0, 2, 1, 1)

        self.label_17 = QLabel(self.main_group_box_export)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(0, 50))

        self.gridLayout_2.addWidget(self.label_17, 1, 0, 1, 1)

        self.groupBox_8 = QGroupBox(self.main_group_box_export)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setFlat(True)
        self.verticalLayout_28 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.default_export = QComboBox(self.groupBox_8)
        self.default_export.addItem("")
        self.default_export.addItem("")
        self.default_export.setObjectName(u"default_export")
        self.default_export.setMaximumSize(QSize(150, 16777215))

        self.verticalLayout_28.addWidget(self.default_export)


        self.gridLayout_2.addWidget(self.groupBox_8, 1, 2, 1, 1)

        self.label_6 = QLabel(self.main_group_box_export)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setEnabled(False)
        self.label_6.setMaximumSize(QSize(150, 16777215))
        self.label_6.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_20 = QLabel(self.main_group_box_export)
        self.label_20.setObjectName(u"label_20")
        font5 = QFont()
        font5.setFamily(u"Bahnschrift Light")
        font5.setPointSize(9)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setUnderline(False)
        font5.setWeight(50)
        font5.setStrikeOut(False)
        font5.setKerning(True)
        font5.setStyleStrategy(QFont.PreferAntialias)
        self.label_20.setFont(font5)

        self.gridLayout_2.addWidget(self.label_20, 2, 0, 1, 1)

        self.groupBox_9 = QGroupBox(self.main_group_box_export)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setFlat(True)
        self.horizontalLayout_17 = QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.default_layout_type_export = QComboBox(self.groupBox_9)
        self.default_layout_type_export.addItem("")
        self.default_layout_type_export.addItem("")
        self.default_layout_type_export.setObjectName(u"default_layout_type_export")
        self.default_layout_type_export.setMinimumSize(QSize(150, 0))
        self.default_layout_type_export.setMaximumSize(QSize(150, 25))

        self.horizontalLayout_17.addWidget(self.default_layout_type_export)

        self.label_21 = QLabel(self.groupBox_9)
        self.label_21.setObjectName(u"label_21")
        font6 = QFont()
        font6.setFamily(u"Bahnschrift Light")
        font6.setPointSize(8)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setUnderline(False)
        font6.setWeight(50)
        font6.setStrikeOut(False)
        font6.setKerning(True)
        font6.setStyleStrategy(QFont.PreferAntialias)
        self.label_21.setFont(font6)

        self.horizontalLayout_17.addWidget(self.label_21)


        self.gridLayout_2.addWidget(self.groupBox_9, 2, 2, 1, 1)


        self.verticalLayout_25.addLayout(self.gridLayout_2)


        self.verticalLayout_15.addWidget(self.main_group_box_export)

        self.importacao_config = QGroupBox(self.scrollAreaWidgetContents_2)
        self.importacao_config.setObjectName(u"importacao_config")
        self.importacao_config.setMinimumSize(QSize(0, 0))
        self.formLayout_6 = QFormLayout(self.importacao_config)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.label_18 = QLabel(self.importacao_config)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 0))
        self.label_18.setMaximumSize(QSize(150, 16777215))

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_18)

        self.default_encondig = QComboBox(self.importacao_config)
        self.default_encondig.setObjectName(u"default_encondig")
        self.default_encondig.setMaximumSize(QSize(150, 16777215))

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.default_encondig)


        self.verticalLayout_15.addWidget(self.importacao_config)

        self.verticalSpacer_2 = QSpacerItem(20, 164, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_2)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_9.addWidget(self.scrollArea_2)

        self.frame_81 = QFrame(self.page2)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setMinimumSize(QSize(0, 60))
        self.horizontalLayout_11 = QHBoxLayout(self.frame_81)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_3 = QSpacerItem(752, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_3)

        self.save_config = QPushButton(self.frame_81)
        self.save_config.setObjectName(u"save_config")
        self.save_config.setIcon(icon14)
        self.save_config.setIconSize(QSize(20, 20))

        self.horizontalLayout_11.addWidget(self.save_config)

        self.reset_config = QPushButton(self.frame_81)
        self.reset_config.setObjectName(u"reset_config")
        self.reset_config.setIcon(icon12)
        self.reset_config.setIconSize(QSize(20, 20))

        self.horizontalLayout_11.addWidget(self.reset_config)


        self.verticalLayout_9.addWidget(self.frame_81)

        self.content.addWidget(self.page2)

        self.horizontalLayout_7.addWidget(self.content)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        mainWindow.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(mainWindow)

        self.btn_page_home.setDefault(False)
        self.content.setCurrentIndex(0)
        self.logvierw.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Template Validator V1.9.3", None))
        self.actionasda.setText(QCoreApplication.translate("mainWindow", u"asda", None))
        self.actionasd.setText(QCoreApplication.translate("mainWindow", u"asd", None))
#if QT_CONFIG(tooltip)
        self.btn_page_home.setToolTip(QCoreApplication.translate("mainWindow", u"Pagina Inicial", None))
#endif // QT_CONFIG(tooltip)
        self.btn_page_home.setText("")
#if QT_CONFIG(tooltip)
        self.btn_page_clients.setToolTip(QCoreApplication.translate("mainWindow", u"Templates", None))
#endif // QT_CONFIG(tooltip)
        self.btn_page_clients.setText("")
#if QT_CONFIG(tooltip)
        self.btn_page_config.setToolTip(QCoreApplication.translate("mainWindow", u"Configura\u00e7\u00f5es", None))
#endif // QT_CONFIG(tooltip)
        self.btn_page_config.setText("")
#if QT_CONFIG(tooltip)
        self.btn_exit_program.setToolTip(QCoreApplication.translate("mainWindow", u"Sair", None))
#endif // QT_CONFIG(tooltip)
        self.btn_exit_program.setText("")
        self.label_8.setText(QCoreApplication.translate("mainWindow", u"Template Validator", None))
        self.metodo_tabela.setText(QCoreApplication.translate("mainWindow", u"Template", None))
#if QT_CONFIG(tooltip)
        self.combo_templates.setToolTip(QCoreApplication.translate("mainWindow", u"Selecao dos Eventos", None))
#endif // QT_CONFIG(tooltip)
        self.label_11.setText(QCoreApplication.translate("mainWindow", u"Modelo", None))
        self.logvierw.setTabText(self.logvierw.indexOf(self.inputmodel), QCoreApplication.translate("mainWindow", u"Input Modelo", None))
        self.label_12.setText(QCoreApplication.translate("mainWindow", u"Resultados:", None))
        self.logvierw.setTabText(self.logvierw.indexOf(self.pageresults), QCoreApplication.translate("mainWindow", u"Analise Resultados", None))
        self.logvierw.setTabText(self.logvierw.indexOf(self.page_logger), QCoreApplication.translate("mainWindow", u"Logger", None))
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"Caminho", None))
        self.icon.setText("")
        self.label_file_directory.setText("")
#if QT_CONFIG(tooltip)
        self.start.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.start.setText(QCoreApplication.translate("mainWindow", u" Importar", None))
#if QT_CONFIG(tooltip)
        self.start_validation.setToolTip(QCoreApplication.translate("mainWindow", u"Parar", None))
#endif // QT_CONFIG(tooltip)
        self.start_validation.setText(QCoreApplication.translate("mainWindow", u" Iniciar", None))
#if QT_CONFIG(tooltip)
        self.export_xlsx.setToolTip(QCoreApplication.translate("mainWindow", u"Exporta somente valores Validos", None))
#endif // QT_CONFIG(tooltip)
        self.export_xlsx.setText(QCoreApplication.translate("mainWindow", u"Exportar", None))
#if QT_CONFIG(tooltip)
        self.jsontoxls.setToolTip(QCoreApplication.translate("mainWindow", u"\u00c9 exportado uma planilha de erros identificados.", None))
#endif // QT_CONFIG(tooltip)
        self.jsontoxls.setText(QCoreApplication.translate("mainWindow", u"Log to Excel", None))
        self.labe_task.setText(QCoreApplication.translate("mainWindow", u"Templates", None))
        self.searchtemplates.setPlaceholderText(QCoreApplication.translate("mainWindow", u"Search", None))
        self.btn_procurar.setText("")
        self.btn_pg_add_new_template.setText(QCoreApplication.translate("mainWindow", u"Adicionar Novo  ", None))
        self.label_3.setText(QCoreApplication.translate("mainWindow", u"Configuracao Novo Template", None))
        self.groupBox_3.setTitle("")
        self.label_7.setText(QCoreApplication.translate("mainWindow", u"Nome Template", None))
        self.name_new_template.setText("")
        self.label_13.setText(QCoreApplication.translate("mainWindow", u"Formato Data", None))
        self.label_14.setText(QCoreApplication.translate("mainWindow", u"Encoding:", None))
        self.encodinginput_2.setText(QCoreApplication.translate("mainWindow", u"UTF-8", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("mainWindow", u"dd/mm/yyyy", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("mainWindow", u"dd-mm-yyyy", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("mainWindow", u"yyyy-mm-dd", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("mainWindow", u"yyyy/mm/dd", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("mainWindow", u"TimeStamp", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("mainWindow", u"ISO", None))

        self.groupBox_2.setTitle("")
        self.new_fild_template.setText(QCoreApplication.translate("mainWindow", u"Novo Campo", None))
        self.delete_fild_template.setText(QCoreApplication.translate("mainWindow", u"Deletar Campo", None))
        self.btn_gerar_template.setText(QCoreApplication.translate("mainWindow", u"Salvar", None))
        self.name_template_view.setText(QCoreApplication.translate("mainWindow", u"View Template", None))
        self.groupBox_4.setTitle("")
        self.btn_cria_xls_template.setText(QCoreApplication.translate("mainWindow", u"Gerar Xlsx", None))
        self.btn_deleta_template.setText(QCoreApplication.translate("mainWindow", u"Deletar Template", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"Configura\u00e7\u00f5es", None))
        self.groupBox.setTitle(QCoreApplication.translate("mainWindow", u"Preferencias de Dados", None))
        self.label_9.setText(QCoreApplication.translate("mainWindow", u"Tipos Valores Number :", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("mainWindow", u"Aceita:", None))
#if QT_CONFIG(tooltip)
        self.config_datatype_number_allowerd_v.setToolTip(QCoreApplication.translate("mainWindow", u"Exemplo : 1,1", None))
#endif // QT_CONFIG(tooltip)
        self.config_datatype_number_allowerd_v.setText(QCoreApplication.translate("mainWindow", u"Virgula", None))
#if QT_CONFIG(tooltip)
        self.config_datatype_number_allowerd_p.setToolTip(QCoreApplication.translate("mainWindow", u"Exemplo : 1.1", None))
#endif // QT_CONFIG(tooltip)
        self.config_datatype_number_allowerd_p.setText(QCoreApplication.translate("mainWindow", u"Ponto", None))
        self.main_group_box_export.setTitle(QCoreApplication.translate("mainWindow", u"Exporta\u00e7\u00e3o de Planilhas", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("mainWindow", u"Com planilhas de no maximo:", None))
        self.label_15.setText(QCoreApplication.translate("mainWindow", u"Linhas", None))
#if QT_CONFIG(tooltip)
        self.label_16.setToolTip(QCoreApplication.translate("mainWindow", u"Apartir de ", None))
#endif // QT_CONFIG(tooltip)
        self.label_16.setText(QCoreApplication.translate("mainWindow", u"Colunas", None))
#if QT_CONFIG(tooltip)
        self.config_export_row_limit.setToolTip(QCoreApplication.translate("mainWindow", u"Apartir de ", None))
#endif // QT_CONFIG(tooltip)
        self.config_export_coll_limit.setSuffix("")
        self.config_export_coll_limit.setPrefix("")
        self.label_17.setText(QCoreApplication.translate("mainWindow", u"Formato Exportacao Padrao", None))
        self.groupBox_8.setTitle("")
        self.default_export.setItemText(0, QCoreApplication.translate("mainWindow", u"xlsx", None))
        self.default_export.setItemText(1, QCoreApplication.translate("mainWindow", u"csv", None))

        self.label_6.setText(QCoreApplication.translate("mainWindow", u"Gera excel colorido com marca\u00e7\u00e3o de erros:", None))
        self.label_20.setText(QCoreApplication.translate("mainWindow", u"Tipo de Export Planilha De Erros", None))
        self.groupBox_9.setTitle("")
        self.default_layout_type_export.setItemText(0, QCoreApplication.translate("mainWindow", u"Minima", None))
        self.default_layout_type_export.setItemText(1, QCoreApplication.translate("mainWindow", u"Completa", None))

#if QT_CONFIG(tooltip)
        self.default_layout_type_export.setToolTip(QCoreApplication.translate("mainWindow", u"Completa: Validos + Linhas de Erros |  Minima : Somente linhas com erros", None))
#endif // QT_CONFIG(tooltip)
        self.label_21.setText("")
        self.importacao_config.setTitle(QCoreApplication.translate("mainWindow", u"Codificacao de Planilhas", None))
        self.label_18.setText(QCoreApplication.translate("mainWindow", u"Encondig Type", None))
        self.save_config.setText(QCoreApplication.translate("mainWindow", u"Salvar", None))
        self.reset_config.setText(QCoreApplication.translate("mainWindow", u"Reset", None))
    # retranslateUi

