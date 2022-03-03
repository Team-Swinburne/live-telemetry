# 
import sys
import os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCharts import *

from ui import MainDash, dashboard

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.resize(1000,700)
        self.setWindowTitle("Live Telemtry")

        self.container = QFrame()
        #self.container.setObjectName("container")
        #self.container.setStyleSheet("#container { background-color : #222}")
        
        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.North)
        self.tabs.setMovable(True)

        for n, color in enumerate(["red", "green", "blue", "yellow"]):
            self.tabs.addTab(Color(color), color)
        dashboard = MainDash()
        self.tabs.addTab(dashboard,"Dashboard")

        #self.container.setLayout(self.layout)
        self.setCentralWidget(self.tabs)

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())