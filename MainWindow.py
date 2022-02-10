# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget, QTabWidget, QLineEdit, QTextEdit)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        MainWindow.setWindowIcon(QIcon(r"Files/59006981.png"))

        self.tabs = QTabWidget(MainWindow)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.resize(800,600)
        self.tabs.addTab(self.tab1,"COM settings")
        self.tabs.addTab(self.tab2,"COM viewer")

        #COM connection status output
        self.ComStatusOutput = QTextEdit(self.tab1)
        self.ComStatusOutput.setGeometry(QRect(10, 10, 770, 400))
        self.ComStatusOutput.setReadOnly(True)

        #COM PORT label
        self.ComPortLabel = QLabel(self.tab1)
        self.ComPortLabel.setGeometry(QRect(10, 490, 60, 30))
        self.ComPortLabel.setObjectName(u"ComPortLabel")
        #COM PORT select combo
        self.ComPortSelect = QComboBox(self.tab1)
        self.ComPortSelect.setGeometry(QRect(10, 520, 60, 30))
        self.ComPortSelect.setObjectName(u"ComPortSelect")

        #COM BAUD label
        self.ComBaudLabel = QLabel(self.tab1)
        self.ComBaudLabel.setGeometry(QRect(90, 490, 60, 30))
        self.ComBaudLabel.setObjectName(u"ComBaudLabel")
        #COM BAUD select combo
        self.ComBaudSelect = QComboBox(self.tab1)
        self.ComBaudSelect.setGeometry(QRect(90, 520, 100, 30))
        self.ComBaudSelect.setObjectName(u"ComBaudSelect")

        #COM connect button
        self.ConnectButton = QPushButton(self.tab1)
        self.ConnectButton.setGeometry(QRect(210, 520, 90, 30))
        self.ConnectButton.setObjectName(u"ConnectButton")
        self.ConnectButton.setCheckable(True)

        #COM serial view
        self.ComSerialOutput = QTextEdit(self.tab2)
        self.ComSerialOutput.setGeometry(QRect(10, 10, 770, 550))
        self.ComSerialOutput.setReadOnly(True)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Live Telemetry", None))
        self.ConnectButton.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.ComPortLabel.setText(QCoreApplication.translate("MainWindow", u"COM Port:", None))
        self.ComBaudLabel.setText(QCoreApplication.translate("MainWindow", u"Baud Rate:", None))
    # retranslateUi

