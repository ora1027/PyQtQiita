import sys
import os
import urllib.request, json

from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QApplication


def main():
    url = 'http://country.io/names.json'
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    list = []
    for value in data.values():
        list.append(value)
    list.sort()

    os.environ['QT_DEBUG_PLUGINS'] = "1"
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()

    my_model = QStringListModel()
    my_model.setStringList(list)
    engine.rootContext().setContextProperty('myModel', my_model)

    engine.load('SampleQml.qml')

    if not engine.rootObjects():
        return -1

    return app.exec_()


if __name__ == '__main__':
    sys.exit(main())
