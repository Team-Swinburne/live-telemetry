# -*- coding: utf-8 -*-
import sys
import os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCharts import *

class SerialTab(QWidget):
    def __init__(self):
        super().__init__()
        #MainWindow.setWindowIcon(QIcon(r"Files/59006981.png"))

        #Set layout
        self.layout = QVBoxLayout()
        self.horizontalLayout = QHBoxLayout()

        #COM connection status output
        self.ComSerialOutput = QTextEdit()
        self.ComSerialOutput.setGeometry(QRect(10, 10, 770, 400))
        self.ComSerialOutput.setReadOnly(True)

        #COM Port Layout
        self.ComLayout = QVBoxLayout()

        #COM PORT label
        self.ComPortLabel = QLabel("COM Port:")
        self.ComLayout.addWidget(self.ComPortLabel)

        #COM PORT select combo
        self.ComPortSelect = QComboBox()
        self.ComLayout.addWidget(self.ComPortSelect)

        #COM Baud Layout
        self.ComBaudLayout = QVBoxLayout()
        #COM BAUD label
        self.ComBaudLabel = QLabel("Baudrate")
        self.ComBaudLayout.addWidget(self.ComBaudLabel)

        #COM BAUD select combo
        self.ComBaudSelect = QComboBox()
        self.ComBaudLayout.addWidget(self.ComBaudSelect)

        #COM connect button
        self.ConnectButton = QPushButton("Connect")
        self.ConnectButton.setCheckable(True)

        #COM connect button
        self.refreshButton = QPushButton("Refresh")
        

        #COM serial clear button
        self.clearButton = QPushButton("Clear")

        self.horizontalLayout.addWidget(self.clearButton,alignment=Qt.AlignBottom)
        self.horizontalLayout.addLayout(self.ComLayout)
        self.horizontalLayout.addLayout(self.ComBaudLayout)
        self.horizontalLayout.addWidget(self.refreshButton,alignment=Qt.AlignBottom)
        self.horizontalLayout.addWidget(self.ConnectButton,alignment=Qt.AlignBottom)

        self.layout.addWidget(self.ComSerialOutput)
        self.layout.addLayout(self.horizontalLayout)
        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SerialTab()
    window.resize(1000,600)
    window.show()
    app.exec()
else:
    from ui.custom_widgets import PyToggle