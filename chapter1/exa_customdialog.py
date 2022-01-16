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
        dlg = CustomDialog(self)
        if dlg.exec_():
            print("Success!")
        else:
            print("Cancel!")


class CustomDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(CustomDialog, self).__init__(*args, **kwargs)
        self.setWindowTitle("HELLO!")
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


if __name__ == '__main__':
    app = QApplication([])
    # window = QMainWindow()
    window = MainWindow()
    window.show()

    app.exec()