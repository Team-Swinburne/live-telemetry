import os
import sys
import random
from PySide6 import QtCore, QtGui, QtWidgets, QtQml

class test(QtGui.QStandardItemModel):
    def __init__(self):
        super().__init__(100,3)
        print(self.rowCount())
        self.idx = self.rowCount()

        for row in range(self.rowCount()):
            item1 = QtGui.QStandardItem()
            item1.setData(row, QtCore.Qt.DisplayRole)
            item2 = QtGui.QStandardItem()
            item2.setData(row, QtCore.Qt.DisplayRole)
            item3 = QtGui.QStandardItem()
            item3.setData(row**2, QtCore.Qt.DisplayRole)
            self.setItem(row, 0, item1)
            self.setItem(row, 1, item2)
            self.setItem(row, 2, item3)

    def update_plot_data(self):
        global idx 
        self.idx += 1
        self.y = random.uniform(0,100)
        item11 = QtGui.QStandardItem()
        item11.setData(self.idx, QtCore.Qt.DisplayRole)
        item22 = QtGui.QStandardItem()
        item22.setData(self.idx, QtCore.Qt.DisplayRole)
        item33 = QtGui.QStandardItem()
        item33.setData(self.y, QtCore.Qt.DisplayRole)

        self.removeRow(0)
        line = [item11 ,item22 ,item33]
        self.appendRow(line)
        # print(type()))

    @QtCore.Slot()
    def get_max_x(self):
        return(int(self.item(0).text()))  
    







# timer = QtCore.QTimer()
# timer.setInterval(100)
# timer.timeout.connect(update_plot_data)

if __name__ == '__main__':
    lineModel = test()
    app = QtWidgets.QApplication(sys.argv)
    engine = QtQml.QQmlApplicationEngine()
    engine.rootContext().setContextProperty("lineModel", lineModel);
    engine.load(QtCore.QUrl.fromLocalFile(os.path.join(os.path.dirname(__file__), "mainvxy.qml")))
    
    timer = QtCore.QTimer()
    timer.setInterval(20)
    timer.timeout.connect(lineModel.update_plot_data)
    timer.start()
    timer.start()
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())