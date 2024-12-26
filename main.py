import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from currency import Ui_MainWindow
from currency import QtCore

class CurrencyConv(QtWidgets.QMainWindow):
    def __init__(self):
        super(CurrencyConv, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

app = QtWidgets.QApplication([])
application = CurrencyConv()
application.show()

sys.exit(app.exec())