from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('mainwindow title')

        label = QLabel('this is label')
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))

        self.addToolBar(toolbar)

        # button_action = QAction("Your button", self)
        button_action = QAction(QIcon("address-book.png"), "your button", self)
        button_action.setStatusTip("This is your button")
        # button_action.triggered.connect(self.onMyToolBarButtonClick)
        # button_action.setCheckable(True)

        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action2 = QAction(QIcon("acorn.png"), "Your button2", self)
        button_action2.setStatusTip("This is your button2")
        # button_action2.triggered.connect(self.onMyToolBarButtonClick)
        # button_action2.setCheckable(True)
        toolbar.addAction(button_action2)
        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))

if __name__ == '__main__':
    app = QApplication([])
    # window = QMainWindow()
    window = MainWindow()
    window.show()

    app.exec()

