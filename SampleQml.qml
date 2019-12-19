import QtQuick 2.9
import QtQuick.Controls 2.5

import Charts 1.0

ApplicationWindow {
    visible: true
    width: 400
    height: 800

    header: ToolBar {
    }

    Column {
        anchors.fill: parent
        anchors.topMargin: 200
        spacing: 50
        Image {
            width: 200
            height: 200
            anchors.horizontalCenter: parent.horizontalCenter
            fillMode: Image.PreserveAspectFit
            source: "data/gopher.png"
        }

        Button {
            anchors.horizontalCenter: parent.horizontalCenter
            Text {
                id: buttonLabel
                anchors.centerIn: parent
                text: qsTr("Click")
                font.pointSize: 20
            }
        }

        PieChart {
            id: chartA
            width: 100; height: 100
            color: "red"
            anchors.centerIn:parent
        }
    }
}
