import sys
from PyQt5 import QtWidgets
from PyQt5 import uic

class Form(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = uic.loadUi("HelloPyQt!.ui")
        self.ui.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    sys.exit(app.exec())
