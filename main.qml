import QtQuick
import QtQuick.Window 2.3
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.3

Window {
    visible: true
    width: 600
    height: 500
    title: "Team Swinburne Live Telemtry"

    TabBar {
        id: bar
        width: parent.width
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
    id: layout
    anchors.fill: parent
    currentIndex: bar.currentIndex
    Rectangle {
        color: 'teal'
        implicitWidth: 200
        implicitHeight: 200
    }
    Rectangle {
        color: 'plum'
        implicitWidth: 300
        implicitHeight: 200
    }
}

}
/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}D{i:2}D{i:3}D{i:4}D{i:1}D{i:7}D{i:6}D{i:8}
D{i:9}D{i:5}
}
##^##*/
