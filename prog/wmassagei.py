# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wmassagei.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MassInfo(object):
    def setupUi(self, MassInfo):
        MassInfo.setObjectName("MassInfo")
        MassInfo.setWindowModality(QtCore.Qt.ApplicationModal)
        MassInfo.resize(400, 150)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(MassInfo.sizePolicy().hasHeightForWidth())
        MassInfo.setSizePolicy(sizePolicy)
        MassInfo.setSizeIncrement(QtCore.QSize(10, 10))
        MassInfo.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MassInfo.setSizeGripEnabled(True)
        MassInfo.setModal(True)
        self.label = QtWidgets.QLabel(MassInfo)
        self.label.setGeometry(QtCore.QRect(10, 20, 51, 70))
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../icons/48/dialog-warning.png"))
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(MassInfo)
        self.label_2.setGeometry(QtCore.QRect(70, 10, 320, 90))
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(MassInfo)
        self.pushButton.setGeometry(QtCore.QRect(190, 111, 85, 27))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/16x16/actions/dialog-ok-apply.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setAutoDefault(True)
        self.pushButton.setDefault(True)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(MassInfo)
        QtCore.QMetaObject.connectSlotsByName(MassInfo)

    def retranslateUi(self, MassInfo):
        _translate = QtCore.QCoreApplication.translate
        MassInfo.setWindowTitle(_translate("MassInfo", "Інженерна геологія"))
        self.label_2.setText(_translate("MassInfo", "<html><head/><body><p>Інформація</p></body></html>"))
        self.pushButton.setText(_translate("MassInfo", "OK"))


