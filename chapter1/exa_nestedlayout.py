from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from chapter1.color_widget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Awesome App")

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()

        layout1.setContentsMargins(5, 5, 5, 5)
        layout1.setSpacing(5)

        layout2.addWidget(Color('red'))
        layout2.addWidget(Color('yellow'))
        layout2.addWidget(Color('purple'))

        layout1.addLayout(layout2)

        layout1.addWidget(Color('green'))

        layout3.addWidget(Color('red'))
        layout3.addWidget(Color('purple'))
        layout1.addLayout(layout3)



        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)

if __name__ == '__main__':
    app = QApplication([])
    # window = QMainWindow()
    window = MainWindow()
    window.show()

    app.exec()