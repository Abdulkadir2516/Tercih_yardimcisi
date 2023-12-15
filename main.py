
import sys


from pencere import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class window(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(window, self).__init__()
        self.setup()

    def setup(self):

        self.setupUi(self)
        self.exams.addItems(["LGS","YKS","DGS","TUS","DUS"])





app = QtWidgets.QApplication(sys.argv)
win = window()
win.show()
sys.exit(app.exec_())





