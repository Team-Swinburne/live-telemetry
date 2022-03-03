// import QtQuick 2.12
// import QtQuick.Controls 2.3
// import QtQuick.Layouts 1.15

// Item {
//     anchors.fill: parent
//     RowLayout {
//         Rectangle {
//             implicitWidth: 50
//             Layout.maximumWidth: 1050
//             Layout.fillWidth: true
//             Layout.fillHeight: true
//         }
//         Rectangle {
//             implicitWidth: 100
//             Layout.maximumWidth: 2100
//             Layout.fillWidth: true
//             Layout.fillHeight: true
//         }
//     }
// }

import QtQuick 2.15
import QtQuick.Controls 2.15

Item {
    visible: true
    width: 600
    height: 500
    // title: "HelloApp"

    Text {
        anchors.centerIn: parent
        text: "Hello World"
        font.pixelSize: 24
    }

}