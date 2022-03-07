# Main dashboard of the Telemetry Software
from pickle import TRUE
from re import X
import sys
import os
from turtle import right
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCharts import *
import pyqtgraph as pg
import numpy as np
from random import randint

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class MainDash(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()

        #init data
        self.data = {}
        self.data["Accumulator Temp"] = [0] * 300
        self.data["Motor Temp"] = [0] * 300
        self.data["MC Temp"] = [0] * 300
        self.data["Accumulator Voltage"] = 0
        self.data["Brake"] = [0] * 300
        self.data["Throttle"] = [0] * 300

        #init curves
        self.curves = {}

        #self.container = QFrame()
        #self.container.setObjectName("container")
        self.setStyleSheet("background-color : #222;")
        self.layout = QHBoxLayout()

        # Right panel
        
        self.rightPane = QVBoxLayout()
        self.accumulatorVoltageBar = QProgressBar()
        self.accumulatorVoltageBar.setOrientation(Qt.Vertical)
        self.accumulatorVoltageBar.setMaximum(600)
        self.accumulatorVoltageBar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.accumulatorText = QLabel("Accumulator Voltage")
        self.accumulatorText.setStyleSheet("color: #fff;")

        font = self.accumulatorText.font()
        font.setPointSize(10)
        self.accumulatorText.setFont(font)
        self.accumulatorVoltage = QLabel("400V")
        self.accumulatorVoltage.setStyleSheet("color: #fff;")
        self.accumulatorVoltage.setFont(font)
        # adding widget
        self.rightPane.addWidget(self.accumulatorText,alignment=Qt.AlignHCenter)
        self.rightPane.addWidget(self.accumulatorVoltageBar,alignment=Qt.AlignHCenter)
        self.rightPane.addWidget(self.accumulatorVoltage,alignment=Qt.AlignHCenter)
       

        # Top-left pannel
        self.topPane = QVBoxLayout()

        #main chart for temperature, using pyqtgraph for performance
        self.tempGraph = pg.PlotWidget(enableMenu = False) #disable mouse interaction
        self.tempGraph.setBackground("#222")
        self.tempGraph.setMouseEnabled(x=False,y=False)
        self.tempGraph.setYRange(-5,85,padding=0)
        self.tempGraph.addLegend()

        self.curves["Accumulator Temp"]   =  self.tempGraph.plot(self.data["Accumulator Temp"],
                                                pen='y',
                                                name="Accumulator Temp")
        self.curves["Motor Temp"]          =  self.tempGraph.plot(self.data["Motor Temp"],
                                                pen='g',
                                                name="Motor Temp")
        self.curves["MC Temp"]            =  self.tempGraph.plot(self.data["MC Temp"],
                                                pen='c',
                                                name="MC Temp")                                
       
        # adding widget
        self.topPane.addWidget(self.tempGraph,1)
        
        # Bottom panel
        self.bottomPane = QHBoxLayout()

        # Brake and Throttle graph
        self.pedalGraph = pg.PlotWidget(enableMenu = False)
        self.pedalGraph.setMouseEnabled(x=False,y=False)
        self.pedalGraph.setYRange(-10,110,padding=0)
        self.pedalGraph.addLegend()
        #self.pedalGraph.setYRange(0, 50, padding=0)
        self.curves["Throttle"]  =   self.pedalGraph.plot(self.data["Throttle"],
                                                    pen='b',
                                                    name="Throttle")
        self.curves["Brake"]     =   self.pedalGraph.plot(self.data["Brake"],
                                                    pen='r',
                                                    name="Brake")
        
        #gg diagram
        self.ggDiagram = QPolarChart()

        self.dataSeries2 = QLineSeries()
        self.dataSeries2.append(0,4)
        self.dataSeries2.append(3,1)
        self.dataSeries2.append(2,5)

        self.ggDiagram.addSeries(self.dataSeries2)

        #self.ggDiagram.a
        #set axis
        self.angularAxis = QValueAxis()
        self.angularAxis.setTickCount(9)
        self.angularAxis.setLabelFormat("%.1f")
        self.angularAxis.setShadesVisible(True)
        self.ggDiagram.addAxis(self.angularAxis,QPolarChart.PolarOrientationAngular)

        self.radialAxis = QValueAxis()
        self.radialAxis.setTickCount(9)
        self.radialAxis.setLabelFormat("%d")
        self.ggDiagram.addAxis(self.radialAxis,QPolarChart.PolarOrientationRadial)

        self.dataSeries2.attachAxis(self.angularAxis)
        self.dataSeries2.attachAxis(self.radialAxis)

        self.radialAxis.setRange(1,10)
        self.angularAxis.setRange(1,10)

        self.ggDiagramView = QChartView(self.ggDiagram)
        self.ggDiagramView.setRenderHint(QPainter.Antialiasing)

        self.bottomPane.addWidget(self.pedalGraph)
        self.bottomPane.addWidget(self.ggDiagramView)

        # Left pane - containting the top and bottom pane as well
        self.leftPane = QVBoxLayout()
        self.leftPane.addLayout(self.topPane,3)
        self.leftPane.addLayout(self.bottomPane,2)

        # Adding to the main layout
        self.layout.addLayout(self.leftPane,6)
        self.layout.addLayout(self.rightPane,1)

        self.setLayout(self.layout)
    
    def updateData(self,key,value):
        #self.x = self.x[1:]  # Remove the first y element.
        #self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.
        #self.x += 1
        if (key=="Accumulator Voltage"):
            self.accumulatorVoltageBar.setValue(value)
            self.accumulatorVoltage.setText(str(value) + " V")
        else:
            self.data[key] = self.data[key][1:]    
            self.data[key].append(value)
            self.curves[key].setData(self.data[key])
        # self.accumulatorTempCurve.  # Update the data.
        # self.accumulatorTempCurve.setData(self.data["Accumulator Temp"])
        #self.data_line1.setPos(self.x,0)

# if run as a standalone app
if __name__ == "__main__":
    from custom_widgets import PyToggle
    app = QApplication(sys.argv)
    window = MainDash()
    window.resize(1000,700)
    window.show()
    app.exec()
else:
    from ui.custom_widgets import PyToggle