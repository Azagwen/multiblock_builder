# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qt_guiyXtdUO.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint, QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QIcon,
    QLinearGradient,
    QPalette,
    QPainter,
    QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *


class UiMainWindow(QMainWindow):
    def setup_ui(self):
        locale = Qt.QLocale
        if self.objectName():
            self.setObjectName(u"MainWindow")
        self.resize(500, 600)
        self.setLocale(locale(locale.English, locale.Canada))
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 109, 481, 431))
        self.settings_layout = QGridLayout(self.gridLayoutWidget)
        self.settings_layout.setObjectName(u"settings_layout")
        self.settings_layout.setHorizontalSpacing(6)
        self.settings_layout.setVerticalSpacing(20)
        self.settings_layout.setContentsMargins(0, 0, 0, 0)
        self.line = QFrame(self.gridLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.settings_layout.addWidget(self.line, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCheckable(False)
        self.pushButton.setFlat(False)

        self.settings_layout.addWidget(self.pushButton, 2, 0, 1, 1)

        self.tabWidget = QTabWidget(self.gridLayoutWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.models = QWidget()
        self.models.setObjectName(u"models")
        self.gridLayoutWidget_3 = QWidget(self.models)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(9, 20, 451, 131))
        self.model_settings_layout = QGridLayout(self.gridLayoutWidget_3)
        self.model_settings_layout.setSpacing(15)
        self.model_settings_layout.setObjectName(u"model_settings_layout")
        self.model_settings_layout.setContentsMargins(15, 15, 15, 15)
        self.lineEdit_4 = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.model_settings_layout.addWidget(self.lineEdit_4, 2, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_3.setMaxLength(40)
        self.lineEdit_3.setFrame(True)
        self.lineEdit_3.setReadOnly(False)
        self.lineEdit_3.setClearButtonEnabled(False)

        self.model_settings_layout.addWidget(self.lineEdit_3, 2, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.model_settings_layout.addWidget(self.lineEdit_5, 2, 2, 1, 1)

        self.comboBox = QComboBox(self.gridLayoutWidget_3)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEditable(False)
        self.comboBox.setMaxVisibleItems(2)

        self.model_settings_layout.addWidget(self.comboBox, 0, 0, 1, 3)

        self.line_3 = QFrame(self.gridLayoutWidget_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShpe(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.model_settings_layout.addWidget(self.line_3, 1, 0, 1, 3)

        self.tabWidget.addTab(self.models, "")
        self.recipes = QWidget()
        self.recipes.setObjectName(u"recipes")
        self.tabWidget.addTab(self.recipes, "")
        self.loot_tables = QWidget()
        self.loot_tables.setObjectName(u"loot_tables")
        self.tabWidget.addTab(self.loot_tables, "")

        self.settings_layout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 10, 481, 71))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaxLength(40)

        self.gridLayout_2.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.line_2 = QFrame(self.gridLayoutWidget_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_2, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaxLength(40)

        self.gridLayout_2.addWidget(self.lineEdit_2, 2, 0, 1, 1)

        self.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(self)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 500, 26))
        self.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)

        self.tabWidget.setCurrentIndex(0)
        self.comboBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslate_ui(self):
        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Texture top Name:", None))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Texture Name:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Full Blocks", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Stairs", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Slabs", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Walls", None))

        self.comboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"Full Blocks", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.models), QCoreApplication.translate("MainWindow", u"Models", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.recipes), QCoreApplication.translate("MainWindow", u"Recipes", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.loot_tables), QCoreApplication.translate("MainWindow", u"Loot Tables", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Namespace:", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Block Name:", None))
    # retranslateUi

