from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from chapter1.color_widget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Awesome App")

        button = QPushButton('click')
        button.clicked.connect(self.onMyToolBarButtonClick)

        self.setCentralWidget(button)

    def onMyToolBarButtonClick(self, s):
        print("click", s)
        dlg = QDialog(self)
        dlg.setWindowTitle("HELLO!")
        dlg.exec_()

if __name__ == '__main__':
    app = QApplication([])
    # window = QMainWindow()
    window = MainWindow()
    window.show()

    app.exec()