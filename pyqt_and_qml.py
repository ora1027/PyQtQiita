import sys
import os

#from PyQt5.QtWidgets import QApplication
#from PyQt5.QtQml import QQmlApplicationEngine, qmlRegisterType
#from PyQt5.QtQuick import QQuickPaintedItem, QQuickView
#from PyQt5.QtGui import QGuiApplication, QPainter, QPen, QColor
#from PyQt5.QtCore import QUrl

import os
import sys

import PySide2
from PySide2.QtQml import qmlRegisterType
from PySide2.QtQuick import QQuickPaintedItem, QQuickView
from PySide2.QtCore import QUrl
from PySide2.QtGui import QGuiApplication, QPainter, QPen, QColor

dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path


class PieChart (QQuickPaintedItem):
    def __init__(self, parent=None):
        QQuickPaintedItem.__init__(self, parent)
        self.color = QColor()

    def paint(self, painter):
        pen = QPen(self.color, 2)
        painter.setPen(pen)
        painter.setRenderHints(QPainter.Antialiasing, True)
        # From drawPie(const QRect &rect, int startAngle, int spanAngle)
        painter.drawPie(self.boundingRect().adjusted(1,1,-1,-1), 90 * 16, 290 * 16)

    def getColor(self):
        return self.color

    def setColor(self, value):
        if value != self.color:
            self.color = value
            self.update()
            self.colorChanged.emit()

#    colorChanged = Signal()
#    color = Property(QColor, getColor, setColor, notify=colorChanged)


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    qmlRegisterType(PieChart, 'Charts', 1, 0, 'PieChart')
    view = QQuickView()
    view.setReseizeMode(QQuickView.SizeRootObjectToView)
    current_path = os.path.abspath(os.path.dirname(__file__))
    qml_file = os.path.join(current_path, 'SampleQml.qml')
    view.setSource(QUrl.fromLocalFile(qml_file))
    if view.status() == QQuickView.Error:
        sys.exit(-1)
