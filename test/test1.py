from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer
import pyqtgraph as pg
import sys
import numpy as np
from random import randint

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        self.data1 = np.random.normal(size=300)
        self.ptr1 = 0

        self.curve2 = self.graphWidget.plot(self.data1)

        self.timer = QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):
        self.data1[:-1] = self.data1[1:]
        self.data1[-1] = np.random.normal()

        self.ptr1 += 1
        self.curve2.setData(self.data1)
        self.curve2.setPos(self.ptr1, 0)

app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec()