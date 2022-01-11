from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Awesome App")
        widget = QCheckBox()
        widget.setCheckState(Qt.Checked)
        # For tristate: widget.setCheckState(Qt.PartiallyChecked)
        # widget.setCheckState(Qt.PartiallyChecked)

        widget.stateChanged.connect(self.show_state)
        self.setCentralWidget(widget)

    def show_state(self, s):
        print(s == Qt.Checked)
        print(s)

if __name__ == '__main__':
    app = QApplication([])
    # window = QMainWindow()
    window = MainWindow()
    window.show()

    app.exec()