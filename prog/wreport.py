# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wreport.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Report_win(object):
    def setupUi(self, Report_win):
        Report_win.setObjectName("Report_win")
        Report_win.setWindowModality(QtCore.Qt.ApplicationModal)
        Report_win.resize(800, 500)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/16x16/categories/applications-engineering.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Report_win.setWindowIcon(icon)
        Report_win.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        Report_win.setModal(True)
        self.treeView = QtWidgets.QTreeView(Report_win)
        self.treeView.setGeometry(QtCore.QRect(10, 40, 780, 380))
        self.treeView.setHeaderHidden(True)
        self.treeView.setObjectName("treeView")
        self.comboBox = QtWidgets.QComboBox(Report_win)
        self.comboBox.setGeometry(QtCore.QRect(170, 430, 510, 27))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(Report_win)
        self.label.setGeometry(QtCore.QRect(10, 430, 150, 27))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Report_win)
        self.label_2.setGeometry(QtCore.QRect(10, 460, 150, 27))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Report_win)
        self.lineEdit.setGeometry(QtCore.QRect(170, 460, 482, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.toolButton = QtWidgets.QToolButton(Report_win)
        self.toolButton.setGeometry(QtCore.QRect(653, 460, 27, 27))
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(Report_win)
        self.toolButton_2.setGeometry(QtCore.QRect(140, 10, 26, 26))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../icons/22x22/actions/expandall.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(Report_win)
        self.toolButton_3.setGeometry(QtCore.QRect(170, 10, 26, 26))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../icons/22x22/actions/collapsall.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon2)
        self.toolButton_3.setObjectName("toolButton_3")
        self.label_3 = QtWidgets.QLabel(Report_win)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 120, 26))
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Report_win)
        self.pushButton.setGeometry(QtCore.QRect(690, 430, 100, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Report_win)
        self.pushButton_2.setGeometry(QtCore.QRect(690, 460, 100, 27))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Report_win)
        self.toolButton_2.clicked.connect(self.treeView.expandAll)
        self.toolButton_3.clicked.connect(self.treeView.collapseAll)
        QtCore.QMetaObject.connectSlotsByName(Report_win)

    def retranslateUi(self, Report_win):
        _translate = QtCore.QCoreApplication.translate
        Report_win.setWindowTitle(_translate("Report_win", "Звітні матеріали"))
        self.label.setText(_translate("Report_win", "Формат вихідних даних"))
        self.label_2.setText(_translate("Report_win", "Вихідний файл звіту"))
        self.toolButton.setText(_translate("Report_win", "..."))
        self.label_3.setText(_translate("Report_win", "Звіти за розділами"))
        self.pushButton.setText(_translate("Report_win", "Звіт"))
        self.pushButton_2.setText(_translate("Report_win", "Відміна"))
