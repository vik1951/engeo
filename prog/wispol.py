# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wispol.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ispol_win(object):
    def setupUi(self, Ispol_win):
        Ispol_win.setObjectName("Ispol_win")
        Ispol_win.resize(600, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/16x16/categories/applications-engineering.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Ispol_win.setWindowIcon(icon)
        Ispol_win.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableIspol = QtWidgets.QTableView(self.tab)
        self.tableIspol.setGeometry(QtCore.QRect(10, 10, 576, 247))
        self.tableIspol.setObjectName("tableIspol")
        self.tableIspol.verticalHeader().setMinimumSectionSize(30)
        Ispol_win.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableIspol_2 = QtWidgets.QTableView(self.tab_2)
        self.tableIspol_2.setGeometry(QtCore.QRect(10, 10, 576, 247))
        self.tableIspol_2.setObjectName("tableIspol_2")
        Ispol_win.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableIspol_3 = QtWidgets.QTableView(self.tab_3)
        self.tableIspol_3.setGeometry(QtCore.QRect(10, 10, 576, 247))
        self.tableIspol_3.setObjectName("tableIspol_3")
        Ispol_win.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tableIspol_4 = QtWidgets.QTableView(self.tab_4)
        self.tableIspol_4.setGeometry(QtCore.QRect(10, 10, 576, 247))
        self.tableIspol_4.setObjectName("tableIspol_4")
        Ispol_win.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tableIspol_5 = QtWidgets.QTableView(self.tab_5)
        self.tableIspol_5.setGeometry(QtCore.QRect(10, 10, 576, 247))
        self.tableIspol_5.setObjectName("tableIspol_5")
        Ispol_win.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tableIspol_6 = QtWidgets.QTableView(self.tab_6)
        self.tableIspol_6.setGeometry(QtCore.QRect(10, 10, 576, 247))
        self.tableIspol_6.setObjectName("tableIspol_6")
        Ispol_win.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tableIspol_7 = QtWidgets.QTableView(self.tab_7)
        self.tableIspol_7.setGeometry(QtCore.QRect(10, 10, 576, 247))
        self.tableIspol_7.setObjectName("tableIspol_7")
        Ispol_win.addTab(self.tab_7, "")

        self.retranslateUi(Ispol_win)
        Ispol_win.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Ispol_win)

    def retranslateUi(self, Ispol_win):
        _translate = QtCore.QCoreApplication.translate
        Ispol_win.setWindowTitle(_translate("Ispol_win", "Виконавці робіт"))
        Ispol_win.setTabText(Ispol_win.indexOf(self.tab), _translate("Ispol_win", "Керівники"))
        Ispol_win.setTabText(Ispol_win.indexOf(self.tab_2), _translate("Ispol_win", "Буровики"))
        Ispol_win.setTabText(Ispol_win.indexOf(self.tab_3), _translate("Ispol_win", "Геологи"))
        Ispol_win.setTabText(Ispol_win.indexOf(self.tab_4), _translate("Ispol_win", "Геодезисти"))
        Ispol_win.setTabText(Ispol_win.indexOf(self.tab_5), _translate("Ispol_win", "Гідрологи"))
        Ispol_win.setTabText(Ispol_win.indexOf(self.tab_6), _translate("Ispol_win", "Геофізики"))
        Ispol_win.setTabText(Ispol_win.indexOf(self.tab_7), _translate("Ispol_win", "Лаборанти"))
