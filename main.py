import sys
from PySide6 import QtWidgets

from MainWindow import Ui_MainWindow
from SerialHandler import Serial_Emulator


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        Serial = Serial_Emulator()
        self.comboBox.addItems(Serial.get_available_port())

        
 
app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()