
import sys

import veri_getir
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
        self.exams.currentIndexChanged.connect(self.change)
        self.add.clicked.connect(self.append)
        self.add_2.clicked.connect(self.append2)
        self.drop.clicked.connect(self.remove)
        self.drop_2.clicked.connect(self.remove2)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), "Şehirler")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), "Üniversiteler")

    def append(self):
        secilen = self.liste1.currentItem()

        self.selected_liste1.addItem(secilen.text())

    def append2(self):
        secilen = self.liste.currentItem()
        self.selected_liste2.addItem(secilen.text())

    def remove(self):
        secilen = self.selected_liste1.currentItem().text()

    def remove2(self):
        secilen = self.liste1.currentItem()

        self.selected_liste1.addItem(secilen.text())

    def temizle(self):
        self.liste1.clear()
        self.liste.clear()
        self.selected_liste1.clear()
        self.selected_liste2.clear()

    def change(self, value):
        sinav = self.exams.itemText(value)
        print(sinav)
        self.temizle()
        if sinav == "LGS":
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), "Şehirler")

            self.liste1.addItems(veri_getir.getir("lgs"))

        elif sinav == "YKS" or sinav == "DGS":
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), "Bölümler")
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), "Üniversiteler")

            self.liste.addItems(veri_getir.getir(f"{sinav.lower()}/uni"))
            self.liste1.addItems(veri_getir.getir(f"{sinav.lower()}/bolum"))

        elif sinav == "TUS" or sinav == "DUS":
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), "Hastaneler")
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), "Bölümler")

            self.liste1.addItems(veri_getir.getir(f"{sinav.lower()}/hastane"))
            self.liste.addItems(veri_getir.getir(f"{sinav.lower()}/bolum"))






app = QtWidgets.QApplication(sys.argv)
win = window()
win.show()
sys.exit(app.exec_())





