# main.py
import sys
import os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCharts import *
import qdarktheme

from ui import MainDash, SerialTab
from lib import SerialEmulator
from random import randint

Serial = SerialEmulator()
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.resize(1000,700)
        self.setWindowTitle("Live Telemtry")

        self.container = QFrame()
        self.container.setObjectName("container")
        #self.container.setStyleSheet("#container { background-color : #222}")
        
        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.North)
        self.tabs.setMovable(True)

        self.dashboard = MainDash()
        self.serialTab = SerialTab()
        self.tabs.addTab(self.dashboard,"Dashboard")
        self.tabs.addTab(self.serialTab,"Serial Connection")

        #self.tabs.setStyleSheet("background-color : #222;")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tabs)
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

        print(self.serialTab.ComPortLabel.text())
        # setup serial
        #ui serial
        self.serialTab.ComPortSelect.addItems(Serial.get_available_port())
        self.serialTab.ComBaudSelect.addItems(["57600", "115200"])
        self.serialTab.ConnectButton.clicked.connect(self.ConnectClicked)
        self.serialTab.clearButton.clicked.connect(self.ClearClicked)
        self.serialTab.refreshButton.clicked.connect(self.refreshClicked)
        self.timer = QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.update)
        self.timer.start()

        self.show()
    def update(self):
        # self.dashboard.updateData("Accumulator Temp",randint(0,60))
        # self.dashboard.updateData("Motor Temp",randint(2,50))
        # self.dashboard.updateData("MC Temp",randint(0,60))
        #self.dashboard.updateData("Throttle",randint(0,60))
        #self.dashboard.updateData("Brake",randint(0,60))
        self.dashboard.updateData("Accumulator Voltage",randint(500,600))
    
    def ConnectClicked(self):
        if(self.serialTab.ConnectButton.isChecked()):
            #Try to open serial port if there was a problem uncheck the button and tell user of error
            try:
                Serial.OpenPort(self.serialTab.ComPortSelect.currentText(), self.serialTab.ComBaudSelect.currentText())
                self.serialTab.ConnectButton.setText("Disconnect")
                self.serialTab.ComSerialOutput.append("SUCCESS: CONNECTED TO {} AT {}".format(self.serialTab.ComPortSelect.currentText(), self.serialTab.ComBaudSelect.currentText()))

                #Create worker thread that continuously reads from the COM PORT in the background
                self.SerialReaderThread = WorkerThread()
                self.SerialReaderThread.start()
                self.SerialReaderThread.SerialLine.connect(self.UpdateSerialMonitor) #Run UpdateSerialMonitor everytime an emit is received from SerialReaderThread

            except:
                self.serialTab.ComSerialOutput.append("ERROR: FAILED TO CONNECT TO COM PORT")
                self.serialTab.ConnectButton.toggle()
        else:
            self.SerialReaderThread.terminate() #Terminate the Serial Reader thread
            self.serialTab.ConnectButton.setText("Connect")
            Serial.ClosePort()
            self.serialTab.ComSerialOutput.setTextColor(self.GreenTextColour)
            self.serialTab.ComSerialOutput.append("SUCCESS: DISCONNECTED FROM {}".format(self.serialTab.ComPortSelect.currentText()))  

    #This function clears the COM viewer when the clear COM viewer button is clicked
    def ClearClicked(self):
        self.serialTab.ComSerialOutput.setText("")

    #This function updates the Serial monitor with the serial data read
    def UpdateSerialMonitor(self, SerialLineRead):
        self.serialTab.ComSerialOutput.append(SerialLineRead)
        print(SerialLineRead)
        self.dashboard.updateData("Accumulator Temp",int(SerialLineRead[0]))
        self.dashboard.updateData("Motor Temp",int(SerialLineRead[q]))
        self.dashboard.updateData("Brake",int(SerialLineRead[1]))

    def refreshClicked(self):
        self.serialTab.ComPortSelect.clear()
        self.serialTab.ComPortSelect.addItems(Serial.get_available_port())

#Thread that runs in the background when serial port is open and reads the COM port
class WorkerThread(QThread):
    SerialLine = Signal(list)
    def run(self):
        while True:
            rxData = Serial.Read()
            #print(LineRead)

            #If line read was empty then there was no data
            if not rxData:
                print("a")
                #Transmits data to the MainWindow class
                self.SerialLine.emit(rxData)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarktheme.load_stylesheet())
    window = MainWindow()
    sys.exit(app.exec())