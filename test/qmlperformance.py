# This Python file uses the following encoding: utf-8
import sys
from os.path import abspath, dirname, join
import random

from PySide6.QtCore import *
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCharts import QAbstractSeries
from PySide6.QtWidgets import QApplication # <---

class Bridge(QObject):
    def __init__(self, parent=None):
        super(Bridge, self).__init__(parent)
        self.dataBuffer = []
        self.index = 0


    @Slot(QAbstractSeries)
    def update_series(self, series):
        #create point
        self.index += 1
        y = random.uniform(0,100)
        self.dataBuffer.append(QPoint(self.index,y))
        if (len(self.dataBuffer) > 200):
            self.dataBuffer.pop(0)

        series.replace(self.dataBuffer)

    @Slot()
    def generateData(self):
        my_data = []
        print("gell")

        for i in range (5):
            my_list = []
            for j in range(200):
                my_list.append(QPoint(j,random.uniform(0,50)))
            self.my_data.append(my_list)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()

    bridge = Bridge()

    # Expose the Python object to QML
    context = engine.rootContext()
    context.setContextProperty("con", bridge)

    #engine.load(os.path.join(os.path.dirname(__file__), "main.qml"))
    # Get the path of the current directory, and then add the name
    # of the QML file, to load it.
    qmlFile = join(dirname(__file__), 'main.qml')
    engine.load(QUrl("main.qml"))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())