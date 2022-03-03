# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

from .dashboard import Ui_dashboard

class Ui_m(object):
    def setupUi(self, m):
        if not m.objectName():
            m.setObjectName(u"m")
        m.resize(803, 535)
        self.centralwidget = QWidget(m)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)

        self.widget = Ui_dashboard()
        self.widget.setupUi(self.centralwidget)
        self.widget.setObjectName(u"widget")

        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        m.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(m)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 803, 22))
        self.menuh = QMenu(self.menubar)
        self.menuh.setObjectName(u"menuh")
        m.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(m)
        self.statusbar.setObjectName(u"statusbar")
        m.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuh.menuAction())

        self.retranslateUi(m)

        QMetaObject.connectSlotsByName(m)
    # setupUi

    def retranslateUi(self, m):
        m.setWindowTitle(QCoreApplication.translate("m", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("m", u"PushButton", None))
        self.menuh.setTitle(QCoreApplication.translate("m", u"h", None))
    # retranslateUi

