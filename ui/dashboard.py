# Main dashboard of the Telemetry Software
from pickle import TRUE
import sys
import os
from turtle import right
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCharts import *



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

        #self.container = QFrame()
        #self.container.setObjectName("container")
        #self.container.setStyleSheet("#container { background-color : #222}")
        self.layout = QHBoxLayout()

        # Right panel
        self.rightPane = QVBoxLayout()
        self.accumulatorVoltageBar = QProgressBar()
        self.accumulatorVoltageBar.setOrientation(Qt.Vertical)
        self.accumulatorText = QLabel("Accumulator Voltage")
        self.accumulatorVoltage = QLabel("400V")
        # adding widget
        self.rightPane.addWidget(self.accumulatorText,alignment=Qt.AlignHCenter)
        self.rightPane.addWidget(self.accumulatorVoltageBar,alignment=Qt.AlignHCenter)
        self.rightPane.addWidget(self.accumulatorVoltage,alignment=Qt.AlignHCenter)
        # self.rightPane.addWidget(Color("red"))
        # self.rightPane.addWidget(Color("blue"))
        # self.rightPane.addWidget(Color("green"))
       
        # Top-left pannel
        self.topPane = QVBoxLayout()
        #char1
        self.chart1 = QChart()
        self.chart_view = QChartView(self.chart1)
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.dataSeries = QLineSeries()
        self.dataSeries.append(0,4)
        self.dataSeries.append(4,8)
        self.chart1.addSeries(self.dataSeries)
        #chart2
        self.chart2 = QChart()
        self.chart_view1 = QChartView(self.chart2)
        self.chart_view1.setRenderHint(QPainter.Antialiasing)
        self.dataSeries = QLineSeries()
        self.dataSeries.append(0,4)
        self.dataSeries.append(4,8)
        self.chart2.addSeries(self.dataSeries)
        #chart 3
        self.chart3 = QChart()
        self.chart_view3 = QChartView(self.chart3)
        self.chart_view3.setRenderHint(QPainter.Antialiasing)
        self.dataSeries = QLineSeries()
        self.dataSeries.append(0,4)
        self.dataSeries.append(4,8)
        self.chart3.addSeries(self.dataSeries)
        # adding widget
        self.topPane.addWidget(self.chart_view,1)
        self.topPane.addWidget(self.chart_view1,1)
        self.topPane.addWidget(self.chart_view3,1)
        # self.topPane.addWidget(Color("yellow"))
        # self.topPane.addWidget(Color("black"))
        # self.topPane.addWidget(Color("green"))
        
        # Bottom panel
        self.bottomPane = QHBoxLayout()
        self.toggle = PyToggle()
        self.bottomPane.addWidget(self.toggle)
        
        
        #throttle bar
        self.throttle = QProgressBar()
        self.throttle.setOrientation(Qt.Vertical)
        
        #brake bar
        self.brake = QProgressBar()
        self.brake.setOrientation(Qt.Vertical)
        
        #
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

        self.bottomPane.addWidget(self.brake)
        self.bottomPane.addWidget(self.throttle)
        self.bottomPane.addWidget(self.ggDiagramView)

        # Left pane - containting the top and bottom pane as well
        self.leftPane = QVBoxLayout()
        self.leftPane.addLayout(self.topPane,2)
        self.leftPane.addLayout(self.bottomPane,1)

        # Adding to the main layout
        self.layout.addLayout(self.leftPane,5)
        self.layout.addLayout(self.rightPane,1)
        
        #self.toggle = PyToggle()
        #self.layout.addWidget(self.toggle, Qt.AlignCenter, Qt.AlignCenter)

        self.setLayout(self.layout)
        #self.show()

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