# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1200, 678)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(400, 50, 711, 321))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.puan_2 = QtWidgets.QLineEdit(self.tab)
        self.puan_2.setGeometry(QtCore.QRect(10, 10, 171, 31))
        self.puan_2.setObjectName("puan_2")
        self.selected_liste1 = QtWidgets.QListWidget(self.tab)
        self.selected_liste1.setGeometry(QtCore.QRect(410, 40, 281, 241))
        self.selected_liste1.setObjectName("selected_liste1")
        self.liste1 = QtWidgets.QListWidget(self.tab)
        self.liste1.setGeometry(QtCore.QRect(10, 40, 281, 241))
        self.liste1.setObjectName("liste1")
        self.add = QtWidgets.QPushButton(self.tab)
        self.add.setGeometry(QtCore.QRect(320, 110, 51, 31))
        self.add.setObjectName("add")
        self.drop = QtWidgets.QPushButton(self.tab)
        self.drop.setGeometry(QtCore.QRect(320, 150, 51, 31))
        self.drop.setObjectName("drop")
        self.getir_1 = QtWidgets.QPushButton(self.tab)
        self.getir_1.setGeometry(QtCore.QRect(310, 190, 81, 61))
        self.getir_1.setObjectName("getir_1")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.drop_2 = QtWidgets.QPushButton(self.tab_2)
        self.drop_2.setGeometry(QtCore.QRect(320, 150, 51, 31))
        self.drop_2.setObjectName("drop_2")
        self.liste = QtWidgets.QListWidget(self.tab_2)
        self.liste.setGeometry(QtCore.QRect(10, 40, 281, 241))
        self.liste.setObjectName("liste")
        self.selected_liste2 = QtWidgets.QListWidget(self.tab_2)
        self.selected_liste2.setGeometry(QtCore.QRect(410, 40, 281, 241))
        self.selected_liste2.setObjectName("selected_liste2")
        self.puan_3 = QtWidgets.QLineEdit(self.tab_2)
        self.puan_3.setGeometry(QtCore.QRect(10, 10, 171, 31))
        self.puan_3.setObjectName("puan_3")
        self.add_2 = QtWidgets.QPushButton(self.tab_2)
        self.add_2.setGeometry(QtCore.QRect(320, 110, 51, 31))
        self.add_2.setObjectName("add_2")
        self.getir_2 = QtWidgets.QPushButton(self.tab_2)
        self.getir_2.setGeometry(QtCore.QRect(310, 190, 81, 61))
        self.getir_2.setObjectName("getir_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 370, 1151, 271))
        self.groupBox.setObjectName("groupBox")
        self.results_table = QtWidgets.QTableWidget(self.groupBox)
        self.results_table.setGeometry(QtCore.QRect(10, 20, 1121, 241))
        self.results_table.setObjectName("results_table")
        self.results_table.setColumnCount(0)
        self.results_table.setRowCount(0)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(60, 40, 191, 71))
        self.groupBox_2.setObjectName("groupBox_2")
        self.puan = QtWidgets.QLineEdit(self.groupBox_2)
        self.puan.setGeometry(QtCore.QRect(10, 20, 171, 31))
        self.puan.setObjectName("puan")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(60, 120, 191, 71))
        self.groupBox_3.setObjectName("groupBox_3")
        self.exams = QtWidgets.QComboBox(self.groupBox_3)
        self.exams.setGeometry(QtCore.QRect(10, 20, 171, 31))
        self.exams.setCurrentText("")
        self.exams.setModelColumn(0)
        self.exams.setObjectName("exams")
        self.getir = QtWidgets.QPushButton(self.centralwidget)
        self.getir.setGeometry(QtCore.QRect(60, 220, 181, 51))
        self.getir.setObjectName("getir")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(60, 300, 291, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        self.menuTercih_Yad_m = QtWidgets.QMenu(self.menubar)
        self.menuTercih_Yad_m.setObjectName("menuTercih_Yad_m")
        self.menuPuan_Hesaplama = QtWidgets.QMenu(self.menubar)
        self.menuPuan_Hesaplama.setObjectName("menuPuan_Hesaplama")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuTercih_Yad_m.menuAction())
        self.menubar.addAction(self.menuPuan_Hesaplama.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.puan_2.setPlaceholderText(_translate("MainWindow", "Search"))
        self.add.setText(_translate("MainWindow", "Ekle >>"))
        self.drop.setText(_translate("MainWindow", "<< Kaldır"))
        self.getir_1.setText(_translate("MainWindow", "Üniversiteleri \n"
"Getir"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Şehirler"))
        self.drop_2.setText(_translate("MainWindow", "<< Kaldır"))
        self.puan_3.setPlaceholderText(_translate("MainWindow", "Search"))
        self.add_2.setText(_translate("MainWindow", "Ekle >>"))
        self.getir_2.setText(_translate("MainWindow", "Bölümleri \n"
"getir"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Bölümler"))
        self.groupBox.setTitle(_translate("MainWindow", "Sonuç"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Puan"))
        self.puan.setPlaceholderText(_translate("MainWindow", "Sınav Puanı"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Sınav Türü Seçiniz"))
        self.getir.setText(_translate("MainWindow", "Getir"))
        self.menuTercih_Yad_m.setTitle(_translate("MainWindow", "Tercih Yardımı"))
        self.menuPuan_Hesaplama.setTitle(_translate("MainWindow", "Puan Hesaplama"))
