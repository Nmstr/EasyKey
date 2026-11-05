import ActionSelector
import PropertyEditor
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import Toolbar
import WorkflowEditor

ApplicationWindow {
    visible: true
    width: 800
    height: 600
    title: "EasyKey"

    Rectangle {
        anchors.fill: parent
        color: "#303030"

        Toolbar {
            id: toolbar

            anchors {
                left: parent.left
                top: parent.top
                right: parent.right
            }

        }

        RowLayout {
            anchors {
                top: toolbar.bottom
                left: parent.left
                right: parent.right
                bottom: parent.bottom
            }

            ActionSelector {
                Layout.minimumWidth: 400
                Layout.fillHeight: true
            }

            WorkflowEditor {
                Layout.fillHeight: true
                Layout.fillWidth: true
            }

            PropertyEditor {
                Layout.minimumWidth: 400
                Layout.fillHeight: true
            }

        }

    }

}
