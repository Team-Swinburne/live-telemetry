# Based a lot on this https://github.com/GKPr0/Formula-Student-Telemetry

import sys
import os
import random

from PySide6.QtWidgets import *
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import *
from PySide6.QtCharts import *
from time import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.load('MainWindow.qml')
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())

# # This Python file uses the following encoding: utf-8
# import sys
# from os.path import abspath, dirname, join
# import random

# from PySide6.QtWidgets import *
# from PySide6.QtQml import QQmlApplicationEngine
# from PySide6.QtCore import *
# from PySide6.QtCharts import *

# class Bridge(QObject):
#     def __init__(self, parent=None):
#         super(Bridge, self).__init__(parent)
#         self.my_data = []
#         self.index = -1

#     @Slot(QAbstractSeries)
#     def update_series(self, series):
#         self.index += 1
#         if(self.index > 4):
#             self.index = 0
#         series.replace(self.my_data[self.index])

#     @Slot()
#     def generateData(self):
#         my_data = []

#         for i in range (5):
#             my_list = []
#             for j in range(200):
#                 my_list.append(QPoint(j,random.uniform(0,100)))
#             self.my_data.append(my_list)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     engine = QQmlApplicationEngine()

#     bridge = Bridge()

#     # Expose the Python object to QML
#     context = engine.rootContext()
#     context.setContextProperty("con", bridge)

#     #engine.load(os.path.join(os.path.dirname(__file__), "main.qml"))
#     # Get the path of the current directory, and then add the name
#     # of the QML file, to load it.
#     qmlFile = join(dirname(__file__), 'MainWindow.qml')
#     engine.load(abspath(qmlFile))

#     if not engine.rootObjects():
#         sys.exit(-1)
#     sys.exit(app.exec_())