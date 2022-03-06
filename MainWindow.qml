import QtQuick 2.9
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.3

ApplicationWindow {
    visible: true
    width: 1300
    height: 600
    title: "HelloApp"

    ColumnLayout {
        x: 0
        y: 0
        anchors.fill: parent


        TabBar {
            id: tabBar
            Layout.fillWidth: true
            TabButton {
                text: qsTr("Home")
            }
            TabButton {
                text: qsTr("Discover")
            }
            TabButton {
                text: qsTr("Activity")
            }
        }
        StackLayout {
            id: stackLayout
            Layout.fillHeight: true
            Layout.preferredHeight: 100
            Layout.preferredWidth: 100
            currentIndex: tabBar.currentIndex
            Item {
                id: homeTab

                DashBoard {
                    id: dashBoard
                }
            }
            Item {
                id: discoverTab

                Rectangle {
                    anchors.fill: parent
                    id: rectangle1
                    width: 200
                    height: 200
                    color: "#0da6f9"
                }

            }
            Item {
                id: activityTab


                Rectangle {
                    color: "#fe0606"
                    anchors.fill: parent
                }

            }
        }
    }

}


//Window {
//    id: root

//    width: 640
//    height: 480
//    visible: true
//    title: "Hello Python World!"

//    Flow {
//        Button {
//            text: "Give me a number!"
//            onClicked: numberGenerator.updateNumber()
//        }
//        Label {
//            id: numberLabel
//            text: "no number"
//        }
//    }

//    Connections {
//        target: graphBridge
//        function onAddPoint(x,y) {
//            console.log(x, " ",y)
//            numberLabel.text = x
//        }
//    }
//}
