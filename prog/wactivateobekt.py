# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wactivateobekt.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ActivateObekt(object):
    def setupUi(self, ActivateObekt):
        ActivateObekt.setObjectName("ActivateObekt")
        ActivateObekt.setWindowModality(QtCore.Qt.ApplicationModal)
        ActivateObekt.resize(420, 260)
        ActivateObekt.setSizeGripEnabled(False)
        ActivateObekt.setModal(True)
        self.comboBox = QtWidgets.QComboBox(ActivateObekt)
        self.comboBox.setEnabled(True)
        self.comboBox.setGeometry(QtCore.QRect(260, 10, 151, 27))
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(ActivateObekt)
        self.pushButton.setGeometry(QtCore.QRect(280, 220, 100, 27))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/16x16/actions/dialog-ok-apply.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(ActivateObekt)
        self.label.setGeometry(QtCore.QRect(14, 10, 240, 27))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(ActivateObekt)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 400, 171))
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(ActivateObekt)
        QtCore.QMetaObject.connectSlotsByName(ActivateObekt)

    def retranslateUi(self, ActivateObekt):
        _translate = QtCore.QCoreApplication.translate
        ActivateObekt.setWindowTitle(_translate("ActivateObekt", "Активація об\'єкта"))
        self.pushButton.setText(_translate("ActivateObekt", "OK"))
        self.label.setText(_translate("ActivateObekt", "Номер першої реєстрації або договору"))
