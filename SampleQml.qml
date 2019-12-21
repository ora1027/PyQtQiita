import QtQuick 2.9
import QtQuick.Controls 2.5

ApplicationWindow {
    id: root

    visible: true
    width: 400
    height: 800


    StackView {
        id: stackView
        anchors.fill: parent
        initialItem: page1

        Page {
            id: page1

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
                    onClicked: {
                        stackView.push(page2)
                    }
                }

                Rectangle {
                    id: listRect

                    width: root.width
                    height: root.height / 2

                    ListView {
                        id: view
                        anchors.fill: parent
                        anchors.rightMargin: 25
                        anchors.leftMargin: 25
                        anchors.bottomMargin: 25
                        anchors.topMargin: 25

                        model: myModel
                        delegate: Text {
                            anchors.leftMargin: 50
                            font.pointSize: 15
                            horizontalAlignment: Text.AlignHCenter
                            text: display
                        }
                    }
                }
            }
            NumberAnimation { id: anim; running: true; target: view; property: "contentY"; duration: 500 }
        }

        Page {
            id: page2

            Column {
                anchors.fill: parent
                anchors.topMargin: 200
                spacing: 50

                Button {
                    id: buttonPage2
                    text: "back to 1"
                    anchors.centerIn: parent
                    onClicked: {
                        stackView.pop()
                    }
                }
                TextEdit {
                    id: te2
                    width: 109
                    height: 29
                    text: "This is Application by PyQt5"
                }
            }
        }
    }
}
