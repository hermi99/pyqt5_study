from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.windowTitleChanged.connect(self.on_window_title_changed)

        self.windowTitleChanged.connect(lambda x: self.my_custom_fn())
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x))
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x, 25))

        self.setWindowTitle('mainwindow title')

        label = QLabel('this is label')
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

    def on_window_title_changed(self, title):
        print(title)

    def my_custom_fn(self, a='hello', b=5):
        print(a, b)

    def contextMenuEvent(self, event):
        print('context menu event')
        super().contextMenuEvent(event)

if __name__ == '__main__':
    app = QApplication([])
    # window = QMainWindow()
    window = MainWindow()
    window.show()

    app.exec()

