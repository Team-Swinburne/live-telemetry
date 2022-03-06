import QtQuick 2.9
import QtQuick.Layouts 1.3
import QtQuick.Controls 2.15
import QtCharts 2.3

Item {
    id: root

    implicitHeight : 600
    implicitWidth: 1000

    anchors.fill: parent

    RowLayout {
        id: container
        anchors.fill: parent

        // left pane of the ui
        ColumnLayout {
            id: leftpane
            Layout.preferredWidth: 85

            ColumnLayout {
               id: graphPane
               Layout.preferredHeight: 70

//               Timer{
//                           id: miTimer
//                           interval: 100
//                           running: true
//                           repeat: true
//                           onTriggered: {
//                               chartmodel.update_series(chartViewItem.series(0))
//                           }
//                       }
                LineGraph{
                    id: temperatureGraph

                    Layout.preferredHeight: 55
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                }

                LineGraph{
                    id: pedelGraph

                    Layout.preferredHeight: 45
                    Layout.fillHeight: true
                    Layout.fillWidth: true
                }

                ValueAxis {
                                id: axisX
                                min:0
                                max:200

                            }

                            ValueAxis{
                                id: axisY
                                min:0
                                max:100
                            }
            }



            RowLayout {
                id: peripheralPane
                Layout.preferredHeight: 30
                Rectangle {
                    Layout.fillHeight: true
                    Layout.fillWidth: true
                    color: "black"
                }

                PolarChartView {
                    id: scatter
                    Layout.fillHeight: true
                    Layout.fillWidth: true
                    margins.top: 0
                    margins.bottom: 0
                    margins.left: 0
                    margins.right: 0
                    ScatterSeries {
                        name: "ScatterSeries"
                        XYPoint {
                            x: 0
                            y: 4.3
                        }

                        XYPoint {
                            x: 2
                            y: 4.7
                        }

                        XYPoint {
                            x: 4
                            y: 5.2
                        }

                        XYPoint {
                            x: 8
                            y: 12.9
                        }

                        XYPoint {
                            x: 9
                            y: 19.2
                        }
                        axisRadial: CategoryAxis {
                            min: 0
                            max: 20
                        }
                        axisAngular: ValueAxis {
                            tickCount: 9
                        }
                    }
                }

                StraightGauge {
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                    value: 50
                    maxValue: 100
                    minValue: 0
                }

                StraightGauge {
                    //Layout.fillWidth: true
                    Layout.fillHeight: true
                    width: 100
                    value: 50
                    maxValue: 100
                    minValue: 0

                    function foo() {
                        //console.log(peripheralPane.width)
                        return peripheralPane.width + 100
                    }
                }

//                Gauge {

//                    size: parent.height
//                }

            }
        }

        ColumnLayout {
            Layout.preferredWidth: 15
            Layout.fillWidth: true
            Layout.fillHeight: true

            Text {
                id: text1
                text: qsTr("Text")
                font.pixelSize: 12
            }
            //https://stackoverflow.com/questions/38500989/qml-qt-quick-weird-layout
            StraightGauge {
                id: myGauge
                Layout.fillWidth: true
                Layout.fillHeight: true
                maxValue: 600
                minValue: 0
                //onAngleChanged: spinBox.value = angle
            }
            SpinBox {
                Layout.fillWidth: true
                id: spinBox
                from: 0
                to: 600
                stepSize: 1
                onValueModified: myGauge.value = value
            }
        }
    }

    Component.onCompleted: {
            //var MotorTempSeries = temperatureGraph.createSeries(ChartView.SeriesTypeSpline,"Motor Temp",axisX,axisY)
            //var McTempSeries = temperatureGraph.createSeries(ChartView.SeriesTypeSpline,"MC Temp",axisX,axisY)
            var BattTempSeries = temperatureGraph.createSeries(ChartView.SeriesTypeLine,"Accumulator Temp",axisX,axisY)

            //var a = graphUpdate.update()
            //var throttleSeries = pedelGraph.createSeries(ChartView.SeriesTypeSpline,"R Temp",axisX,axisY)
            //miTimer.start()
        }

    Connections {
        target: graphBridge
        function onAddPoint(x,y) {
            temperatureGraph.series(0).append(x,y)
            var count = temperatureGraph.series(0).count
            if (count > 200) {
                temperatureGraph.series(0).remove(0)
            }
            if (x > axisX.max) {
                axisX.max = x;
                axisX.min = temperatureGraph.series(0).at(0).x
            }
        }
    }

}

//ChartView {
//            id: chartViewItem
//            x: 0
//            y: 0
//            Layout.fillHeight: true
//            Layout.fillWidth: true
//            antialiasing: true
//            theme:ChartView.ChartThemeDark
//            ValueAxis {
//                id: axisX
//                min:0
//                max:500

//            }

//            ValueAxis{
//                id: axisY
//                min:0
//                max:100
//            }

//            Rectangle {
//                id: horizontalScrollMask
//                visible: false
//                anchors.fill: parent
//            }

//            MouseArea {
//                id: chartMouseAreaA
//                anchors.fill: parent
//                anchors.rightMargin: -8
//                anchors.bottomMargin: -8
//                anchors.leftMargin: 8
//                anchors.topMargin: 8

//                acceptedButtons: Qt.LeftButton | Qt.RightButton

//                onMouseXChanged: {
//                    if ((mouse.buttons & Qt.LeftButton) == Qt.LeftButton) {
//                        chartViewItem.scrollLeft(mouseX - horizontalScrollMask.x);


//                        horizontalScrollMask.x = mouseX;
//                    }
//                }
//                onPressed: {
//                    if (mouse.button == Qt.LeftButton) {
//                        horizontalScrollMask.x = mouseX;
//                    }
//                }
//            }
//        }

/*##^##
Designer {
    D{i:0;formeditorZoom:2}D{i:5}D{i:4}D{i:8}D{i:7}D{i:11}D{i:10}D{i:3}D{i:14}D{i:13}
D{i:2}D{i:16}D{i:17}D{i:18}D{i:15}D{i:1}
}
##^##*/
