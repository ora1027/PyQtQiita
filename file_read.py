import sys
import os.path

import numpy as np
import cv2

from PyQt5.QtWidgets import QMainWindow, QAction, QApplication, QTextEdit, QFileDialog


class ReadImg:
    def __init__(self, file):
        self.file = file
        print(self.file)

    def open_img(self):
        pic = cv2.imread(self.file)
        pic_color = cv2.cvtColor(pic, cv2.COLOR_BGR2RGB)
        return pic, pic_color

    def canny(self, pic):
        img = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(img, 100, 200)
        edges2 = np.zeros_like(pic)
        for i in (0, 1, 2):
            edges2[:, :, i] = edges
        add = cv2.addWeighted(pic, 1, edges2, 0, 4, 0)
        return add


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        self.statusBar()

        openFile = QAction('&File', self)
        openFile.triggered.connect(self.show_file_dialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Menu')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menubar')
        self.show()

    def show_file_dialog(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open file', '/home')

        if file_name[0]:
            print(file_name[0])
            self.identify_extension(file_name[0])

    def identify_extension(self, path):
        root, ext = os.path.splitext(path)
        print(path)
        if ext == '.txt':
            f = open(path, 'r')
            with f:
                data = f.read()
                self.textEdit.setText(data)
        elif ext == '.jpg' or ext == '.png':
            read_img = ReadImg(path)
            b, c = read_img.open_img()
            d = read_img.canny(b)
            cv2.imshow("", d)
            cv2.waitKey(0)
            cv2.destroyAllWindows()


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
