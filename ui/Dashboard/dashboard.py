import os
import sys

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtQml import *
# from PySide6.QtWidgets import *
# from PySide6.QtQuick import *
# from PySide6.QtQuickWidgets import QQuickWidget

# class Dashboard(QQuickWidget):
#     def __init__(self):
#         QQuickWidget.__init__(self)
#         directory = os.path.dirname(os.path.abspath(__file__))
#         self.setSource(QUrl.fromLocalFile(os.path.join(directory, "dashboard.qml")))

# class Color(QWidget):

#     def __init__(self, color):
#         super(Color, self).__init__()
#         self.setAutoFillBackground(True)

#         palette = self.palette()
#         palette.setColor(QPalette.Window, QColor(color))
#         self.setPalette(palette)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = QMainWindow()
#     tab = QTabWidget()
#     tab.addTab(Color("red"),"red")
#     tab.addTab(Color("green"),"red")
#     #test = Dashboard()
#     view = QQuickView()
#     directory = os.path.dirname(os.path.abspath(__file__))
#     view.setSource(QUrl.fromLocalFile(os.path.join(directory, "dashboard.qml")))
#     test = QWidget()
#     test.createWindowContainer(view)
#     tab.addTab(test,"Test")
#     window.setCentralWidget(tab)
#     window.show()
#     app.exec()

app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
directory = os.path.dirname(os.path.abspath(__file__))
engine.load(QUrl.fromLocalFile(os.path.join(directory, "dashboard.qml")))

sys.exit(app.exec())