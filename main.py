import sys
from PySide6 import QtWidgets
import PySide6

from MainWindow import Ui_MainWindow
from SerialHandler import Serial_Emulator

import time

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QThread, Signal)

Serial = Serial_Emulator()

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    #Text colours for different widgets
    RedTextColour = PySide6.QtGui.QColor("red")
    GreenTextColour = PySide6.QtGui.QColor("green")

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.ComPortSelect.addItems(Serial.get_available_port())
        self.ComBaudSelect.addItems(["57600", "115200"])
        self.ConnectButton.clicked.connect(self.ConnectClicked)
        self.ComSerialClearButton.clicked.connect(self.ClearClicked)

    #This function handles when the Connect button is clicked
    def ConnectClicked(self):
        if(self.ConnectButton.isChecked()):
            #Try to open serial port if there was a problem uncheck the button and tell user of error
            try:
                Serial.OpenPort(self.ComPortSelect.currentText(), self.ComBaudSelect.currentText())
                self.ConnectButton.setText("Disconnect")
                self.ComStatusOutput.setTextColor(self.GreenTextColour)
                self.ComStatusOutput.append("SUCCESS: CONNECTED TO {} AT {}".format(self.ComPortSelect.currentText(), self.ComBaudSelect.currentText()))

                #Create worker thread that continuously reads from the COM PORT in the background
                self.SerialReaderThread = WorkerThread()
                self.SerialReaderThread.start()
                self.SerialReaderThread.SerialLine.connect(self.UpdateSerialMonitor) #Run UpdateSerialMonitor everytime an emit is received from SerialReaderThread

            except:
                self.ComStatusOutput.setTextColor(self.RedTextColour)
                self.ComStatusOutput.append("ERROR: FAILED TO CONNECT TO COM PORT")
                self.ConnectButton.toggle()
        else:
            self.SerialReaderThread.terminate() #Terminate the Serial Reader thread
            self.ConnectButton.setText("Connect")
            Serial.ClosePort()
            self.ComStatusOutput.setTextColor(self.GreenTextColour)
            self.ComStatusOutput.append("SUCCESS: DISCONNECTED FROM {}".format(self.ComPortSelect.currentText()))  

    #This function clears the COM viewer when the clear COM viewer button is clicked
    def ClearClicked(self):
        self.ComSerialOutput.setText("")

    #This function updates the Serial monitor with the serial data read
    def UpdateSerialMonitor(self, SerialLineRead):
        self.ComSerialOutput.append(SerialLineRead)

#Thread that runs in the background when serial port is open and reads the COM port
class WorkerThread(QThread):
    SerialLine = Signal(str)
    def run(self):
        while True:
            LineRead = Serial.Read()

            #If line read was empty then there was no data
            if(not(LineRead == '')):
                #Transmits data to the MainWindow class
                self.SerialLine.emit(LineRead)



app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
#When window opens
app.exec()
#When program closes
