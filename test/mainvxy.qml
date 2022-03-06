import QtQuick 2.9
import QtQuick.Window 2.2
import QtCharts 2.2

Window {
    visible: true
    width: 640
    height: 480
    title: qsTr("Hello World")

    ChartView {
        antialiasing: true
        anchors.fill: parent
        id: chart

        ValueAxis {
            id: axisX
            max: 100
            //format: "HH:mm:ss"
        }

        ValueAxis {
            id: axisY
            min: 0
            max: 100
        }

        LineSeries{
            id: line
            axisX: axisX
            axisY: axisY
        }

        VXYModelMapper {
            id: modelMapper
            model: lineModel // QStandardModel in C++
            series: line
            firstRow: 1
            xColumn: 1
            yColumn: 2
        }
    }

    Connections {
        target: lineModel
        function onRowsInserted() {
            var count = chart.series(0).count;
            axisX.min = chart.series(0).at(0).x;
            axisX.max = chart.series(0).at(count-1).x;
            //axisX.max = lineModel.get_max_x()
        }
    }
}