# main.py
import sys
import os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCharts import *

from ui import MainDash, dashboard
from random import randint

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
        self.container.setObjectName("container")
        self.container.setStyleSheet("#container { background-color : #222}")
        
        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.North)
        self.tabs.setMovable(True)

        self.dashboard = MainDash()
        self.tabs.addTab(self.dashboard,"Dashboard")

        self.tabs.setStyleSheet("background-color : #222;")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tabs)
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

        self.timer = QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.update)
        self.timer.start()

        self.show()
    def update(self):
        self.dashboard.updateData("Accumulator Temp",randint(0,60))
        self.dashboard.updateData("Motor Temp",randint(2,50))
        self.dashboard.updateData("MC Temp",randint(0,60))
        self.dashboard.updateData("Throttle",randint(0,60))
        self.dashboard.updateData("Brake",randint(0,60))
        self.dashboard.updateData("Accumulator Voltage",randint(0,600))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())