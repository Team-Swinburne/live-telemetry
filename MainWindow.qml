//import QtQuick 2.9
//import QtQuick.Controls 2.15
//import QtQuick.Layouts 1.3

//ApplicationWindow {
//    visible: true
//    width: 1300
//    height: 600
//    title: "HelloApp"

//    ColumnLayout {
//        x: 0
//        y: 0
//        anchors.fill: parent


//        TabBar {
//            id: tabBar
//            Layout.fillWidth: true
//            TabButton {
//                text: qsTr("Home")
//            }
//            TabButton {
//                text: qsTr("Discover")
//            }
//            TabButton {
//                text: qsTr("Activity")
//            }
//        }
//        StackLayout {
//            id: stackLayout
//            Layout.fillHeight: true
//            Layout.preferredHeight: 100
//            Layout.preferredWidth: 100
//            currentIndex: tabBar.currentIndex
//            Item {
//                id: homeTab

//                DashBoard {
//                    id: dashBoard
//                }
//            }
//            Item {
//                id: discoverTab

//                Rectangle {
//                    anchors.fill: parent
//                    id: rectangle1
//                    width: 200
//                    height: 200
//                    color: "#0da6f9"
//                }

//            }
//            Item {
//                id: activityTab


//                Rectangle {
//                    color: "#fe0606"
//                    anchors.fill: parent
//                }

//            }
//        }
//    }

//}

///*##^##
//Designer {
//    D{i:0;formeditorZoom:0.25}D{i:3}D{i:4}D{i:5}D{i:2}D{i:8}D{i:7}D{i:10}D{i:9}D{i:12}
//D{i:11}D{i:6}D{i:1}
//}
//##^##*/

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
        interval: 1 / 24 * 1000  //update every 200ms
        running: true
        repeat: true
        onTriggered: {
            con.update_series(chart.series(0))
        }
    }

    Label {
        id: label
        x: 298
        color: "#f1f3f4"
        text: qsTr("Graphin dynamically with python")
        anchors.horizontalCenterOffset: 0
        anchors.top: parent.top
        anchors.topMargin: 10
        font.bold: true
        font.pointSize: 25
        anchors.horizontalCenter: parent.horizontalCenter
    }

    ChartView {
        id: chart
        x: 180
        y: 90
        width: 500
        height: 300
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
        con.generateData()
    }
}
