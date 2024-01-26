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
        self.getir.clicked.connect(self.artik_getir)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), "Şehirler")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), "Üniversiteler")

    def elemanlar(self, liste):
        
        sayi = liste.count()
        elemanlar = []

        for i in range(sayi):
            bolum = str(liste.item(i).text())
            bolum = bolum.translate(str.maketrans("İÜÇÖŞĞ", "ıüçöşğ"))
            bolum = bolum.translate(str.maketrans("üışçöğ", "uiscog"))
            

            elemanlar.append(bolum)

        return elemanlar

    def artik_getir(self):
        sinav = self.exams.currentText().lower()
        
        elements = self.elemanlar(self.selected_liste2)
        
        for i in elements:

            sayi = self.selected_liste1.count()
            istekler = []

            for j in range(sayi):
                uni = str(self.selected_liste1.item(j).text())
                istekler.append(uni)


            x = veri_getir.find(sinav,i,"bolum")
            print(x)

            print("\n\n")
            for i in x:

                if i[2] in istekler:
                    print(i)

            



    def uni_bolumleri_getir(self):
        sinav = self.exams.currentText().lower()
        # bolum
        print(sinav)
        if sinav == "yks" or sinav == "dgs":
            part = "bolum"
        elif sinav == "tus" or sinav == "dus":
            part = "hastane"

        self.temizle(1)

        secilen_bolumler = self.selected_liste1.count()
        print(secilen_bolumler)
        üniler = []
        for i in range(secilen_bolumler):
            alan = str(self.selected_liste1.item(i).text())
            alan = alan.translate(str.maketrans("İÜÇÖŞĞ", "ıüçöşğ"))
            alan = alan.translate(str.maketrans("üışçöğ", "uiscog"))

            print(veri_getir.getir2(sinav,alan,part))
            üniler += list(veri_getir.getir2(sinav,alan,part))

        self.liste.addItems(list(set(üniler)))
        self.liste.sortItems()


    def bolum_hastane_getir(self):
        sinav = self.exams.currentText().lower()
        # bolum
        print(sinav)
        if sinav == "yks" or sinav == "dgs":
            part = "uni"
        elif sinav == "tus" or sinav == "dus":
            part = "bolum"

        self.temizle(2)

        secilen_bolumler = self.selected_liste2.count()
        print(secilen_bolumler)
        üniler = []
        for i in range(secilen_bolumler):
            alan = str(self.selected_liste2.item(i).text())
            alan = alan.translate(str.maketrans("İÜÇÖŞĞ", "ıüçöşğ"))
            alan = alan.translate(str.maketrans("üışçöğ", "uiscog"))

            print(veri_getir.getir2(sinav, alan, part))
            üniler += list(veri_getir.getir2(sinav, alan, part))

        self.liste1.addItems(list(set(üniler)))
        self.liste1.sortItems()




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

    def temizle(self, kimi=3):
        if kimi == 1:
            self.liste.clear()
            self.selected_liste2.clear()


        elif kimi==2:
            self.liste1.clear()
            self.selected_liste1.clear()

        elif kimi == 3:
            self.liste.clear()
            self.selected_liste1.clear()
            self.liste1.clear()
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





