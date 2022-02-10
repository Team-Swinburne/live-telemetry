import sys
from PySide6 import QtWidgets
import PySide6

from MainWindow import Ui_MainWindow
from SerialHandler import Serial_Emulator


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    #Text colours for different widgets
    RedTextColour = PySide6.QtGui.QColor("red")
    GreenTextColour = PySide6.QtGui.QColor("green")

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.Serial = Serial_Emulator()
        self.ComPortSelect.addItems(self.Serial.get_available_port())
        self.ComBaudSelect.addItems(["57600", "115200"])
        self.ConnectButton.clicked.connect(self.ConnectClicked)

    def ConnectClicked(self):
        if(self.ConnectButton.isChecked()):
            #Try to open serial port if there was a problem uncheck the button and tell user of error
            try:
                self.Serial.OpenPort(self.ComPortSelect.currentText(), self.ComBaudSelect.currentText())
                self.ConnectButton.setText("Disconnect")
                self.ComStatusOutput.setTextColor(self.GreenTextColour)
                self.ComStatusOutput.append("SUCCESS: CONNECTED TO {} AT {}".format(self.ComPortSelect.currentText(), self.ComBaudSelect.currentText()))
            except:
                self.ComStatusOutput.setTextColor(self.RedTextColour)
                self.ComStatusOutput.append("ERROR: FAILED TO CONNECT TO COM PORT")
                self.ConnectButton.toggle()
        else:
            self.ConnectButton.setText("Connect")
            self.Serial.ClosePort()
            self.ComStatusOutput.setTextColor(self.GreenTextColour)
            self.ComStatusOutput.append("SUCCESS: DISCONNECTED FROM {}".format(self.ComPortSelect.currentText()))     
 
app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()