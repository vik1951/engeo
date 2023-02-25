# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wmassageq.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MassQuestion(object):
    def setupUi(self, MassQuestion):
        MassQuestion.setObjectName("MassQuestion")
        MassQuestion.setWindowModality(QtCore.Qt.ApplicationModal)
        MassQuestion.resize(400, 150)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(MassQuestion.sizePolicy().hasHeightForWidth())
        MassQuestion.setSizePolicy(sizePolicy)
        MassQuestion.setSizeIncrement(QtCore.QSize(10, 10))
        MassQuestion.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MassQuestion.setSizeGripEnabled(True)
        MassQuestion.setModal(True)
        self.label = QtWidgets.QLabel(MassQuestion)
        self.label.setGeometry(QtCore.QRect(10, 20, 51, 70))
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../icons/48/dialog-question.png"))
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(MassQuestion)
        self.label_2.setGeometry(QtCore.QRect(70, 10, 320, 90))
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(MassQuestion)
        self.pushButton.setGeometry(QtCore.QRect(231, 111, 85, 27))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/16x16/actions/dialog-ok-apply.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(MassQuestion)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 111, 85, 27))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../icons/16x16/actions/dialog-cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setDefault(True)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(MassQuestion)
        QtCore.QMetaObject.connectSlotsByName(MassQuestion)

    def retranslateUi(self, MassQuestion):
        _translate = QtCore.QCoreApplication.translate
        MassQuestion.setWindowTitle(_translate("MassQuestion", "Інженерна геологія"))
        self.label_2.setText(_translate("MassQuestion", "<html><head/><body><p>Ви бажаєте завершити роботу з програмою? </p></body></html>"))
        self.pushButton.setText(_translate("MassQuestion", "Так"))
        self.pushButton_2.setText(_translate("MassQuestion", "Ні"))


