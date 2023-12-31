# pyuic5 untitled.ui - o pencere.py
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
        self.tabWidget.setCurrentIndex(0)

        self.getir_1.clicked.connect(self.uni_bolumleri_getir)
        self.getir_2.clicked.connect(self.bolum_hastane_getir)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), "Şehirler")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), "Üniversiteler")

    def uni_bolumleri_getir(self):
        sinav = self.exams.currentText()
        # bolum


        secilen_bolumler = self.selected_liste1.count()
        print(secilen_bolumler)

        for i in range(secilen_bolumler):
            alan = str(self.selected_liste1.item(i).text())
            alan = alan.translate(str.maketrans("üışçö","uisco"))
            veri_getir.getir2(sinav,alan)




    def bolum_hastane_getir(self):
        pass



    def append(self):
        secilen = self.liste1.currentItem()

        self.selected_liste1.addItem(secilen.text())

    def append2(self):
        secilen = self.liste.currentItem()
        self.selected_liste2.addItem(secilen.text())

    def remove(self):
        self.selected_liste1.takeItem(self.selected_liste1.currentRow())

    def remove2(self):
        self.selected_liste2.takeItem(self.selected_liste2.currentRow())

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
            self.getir_1.setText("Üniversiteleri \n Getir")
            self.getir_2.setText("Bölümleri \n Getir")

            # !!!
            self.liste.addItems(veri_getir.getir(f"{sinav.lower()}/uni"))
            self.liste1.addItems(veri_getir.getir(f"{sinav.lower()}/bolum"))

        elif sinav == "TUS" or sinav == "DUS":
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), "Hastaneler")
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), "Bölümler")
            self.getir_1.setText("Bölümleri \n Getir")
            self.getir_2.setText("Hastaneleri \n Getir")

            self.liste1.addItems(veri_getir.getir(f"{sinav.lower()}/hastane"))
            self.liste.addItems(veri_getir.getir(f"{sinav.lower()}/bolum"))






app = QtWidgets.QApplication(sys.argv)
win = window()
win.show()
sys.exit(app.exec_())





