import QtQuick 2.10
import QtQuick.Window 2.5
import QtQuick.Controls 2.4
import QtCharts 2.0

Window {
    id: window
    title: qsTr("QML and Python graphing dynamically")
    width: 640
    height: 480
    color: "#1b480d"
    visible: true

    Timer{
        id: miTimer
        interval: 10  //update frequency = 100Hz
        running: true
        repeat: true
        onTriggered: {
            con.update_series(chart.series(0))
            var count = chart.series(0).count
            var Xmax = chart.series(0).at(count-1).x
            var Xmin = chart.series(0).at(0).x
            if (Xmax > axisX.max)
                axisX.max = Xmax
            if (Xmin > axisX.min)
                axisX.min = Xmin
        }
    }

    ChartView {
        id: chart
        anchors.fill: parent
        antialiasing: true
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter

        ValueAxis{
            id: axisX
            min: 0
            max: 200
        }

        ValueAxis{
            id: axisY
            min: 0
            max: 100
        }

        }

    Component.onCompleted: {
        console.log("Se ha iniciado QML\n")
        var series = chart.createSeries(ChartView.SeriesTypeLine,"My grafico",axisX,axisY)
        //con.generateData()
    }
}
