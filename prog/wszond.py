# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wszond.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Szond_win(object):
    def setupUi(self, Szond_win):
        Szond_win.setObjectName("Szond_win")
        Szond_win.resize(1124, 690)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/16x16/categories/applications-engineering.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Szond_win.setWindowIcon(icon)
        Szond_win.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab)
        self.comboBox_4.setGeometry(QtCore.QRect(168, 450, 140, 27))
        self.comboBox_4.setObjectName("comboBox_4")
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.tab)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(168, 270, 100, 27))
        self.doubleSpinBox_3.setLocale(QtCore.QLocale(QtCore.QLocale.C, QtCore.QLocale.AnyCountry))
        self.doubleSpinBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_3.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.doubleSpinBox_3.setMinimum(-10000.0)
        self.doubleSpinBox_3.setMaximum(10000.0)
        self.doubleSpinBox_3.setSingleStep(0.01)
        self.doubleSpinBox_3.setProperty("value", -10000.0)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(10, 535, 300, 101))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.toolButton_1 = QtWidgets.QToolButton(self.tab)
        self.toolButton_1.setGeometry(QtCore.QRect(320, 10, 26, 26))
        self.toolButton_1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../icons/16x16/actions/list-add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_1.setIcon(icon1)
        self.toolButton_1.setObjectName("toolButton_1")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(0, 390, 160, 27))
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.label_22 = QtWidgets.QLabel(self.tab)
        self.label_22.setGeometry(QtCore.QRect(0, 480, 160, 27))
        self.label_22.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.toolButton_3 = QtWidgets.QToolButton(self.tab)
        self.toolButton_3.setGeometry(QtCore.QRect(380, 10, 26, 26))
        self.toolButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../icons/16x16/actions/edit-table-insert-row-under.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon2)
        self.toolButton_3.setObjectName("toolButton_3")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 10, 300, 77))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(0, 240, 160, 27))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(20, 542, 240, 22))
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(0, 360, 160, 27))
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(0, 90, 160, 27))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_18 = QtWidgets.QLabel(self.tab)
        self.label_18.setGeometry(QtCore.QRect(20, 584, 240, 22))
        self.label_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(0, 330, 160, 27))
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.tab)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(168, 240, 100, 27))
        self.doubleSpinBox_2.setLocale(QtCore.QLocale(QtCore.QLocale.C, QtCore.QLocale.AnyCountry))
        self.doubleSpinBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_2.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.doubleSpinBox_2.setMaximum(9999999.99)
        self.doubleSpinBox_2.setSingleStep(0.01)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.tab)
        self.doubleSpinBox_4.setGeometry(QtCore.QRect(168, 300, 100, 27))
        self.doubleSpinBox_4.setLocale(QtCore.QLocale(QtCore.QLocale.C, QtCore.QLocale.AnyCountry))
        self.doubleSpinBox_4.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_4.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.doubleSpinBox_4.setMaximum(999.99)
        self.doubleSpinBox_4.setSingleStep(0.01)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(0, 150, 160, 27))
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.comboBox_5 = QtWidgets.QComboBox(self.tab)
        self.comboBox_5.setGeometry(QtCore.QRect(168, 480, 140, 27))
        self.comboBox_5.setObjectName("comboBox_5")
        self.toolButton_6 = QtWidgets.QToolButton(self.tab)
        self.toolButton_6.setGeometry(QtCore.QRect(470, 10, 26, 26))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../icons/16x16/actions/edit-clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_6.setIcon(icon3)
        self.toolButton_6.setObjectName("toolButton_6")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(0, 120, 160, 27))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.comboBox_1 = QtWidgets.QComboBox(self.tab)
        self.comboBox_1.setGeometry(QtCore.QRect(168, 90, 140, 27))
        self.comboBox_1.setObjectName("comboBox_1")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_1.setGeometry(QtCore.QRect(168, 120, 100, 27))
        self.lineEdit_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.toolButton_2 = QtWidgets.QToolButton(self.tab)
        self.toolButton_2.setGeometry(QtCore.QRect(350, 10, 26, 26))
        self.toolButton_2.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../icons/16x16/actions/list-remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon4)
        self.toolButton_2.setObjectName("toolButton_2")
        self.label_17 = QtWidgets.QLabel(self.tab)
        self.label_17.setGeometry(QtCore.QRect(2, 510, 160, 27))
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.doubleSpinBox_1 = QtWidgets.QDoubleSpinBox(self.tab)
        self.doubleSpinBox_1.setGeometry(QtCore.QRect(168, 210, 100, 27))
        self.doubleSpinBox_1.setAutoFillBackground(False)
        self.doubleSpinBox_1.setLocale(QtCore.QLocale(QtCore.QLocale.C, QtCore.QLocale.AnyCountry))
        self.doubleSpinBox_1.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_1.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.doubleSpinBox_1.setMaximum(9999999.99)
        self.doubleSpinBox_1.setSingleStep(0.01)
        self.doubleSpinBox_1.setProperty("value", 0.0)
        self.doubleSpinBox_1.setObjectName("doubleSpinBox_1")
        self.label_20 = QtWidgets.QLabel(self.tab)
        self.label_20.setGeometry(QtCore.QRect(920, 7, 190, 30))
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setWordWrap(True)
        self.label_20.setObjectName("label_20")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(0, 450, 160, 27))
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(self.tab)
        self.doubleSpinBox_5.setGeometry(QtCore.QRect(168, 330, 100, 27))
        self.doubleSpinBox_5.setLocale(QtCore.QLocale(QtCore.QLocale.C, QtCore.QLocale.AnyCountry))
        self.doubleSpinBox_5.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_5.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.doubleSpinBox_5.setMaximum(999.99)
        self.doubleSpinBox_5.setSingleStep(0.01)
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_2.setGeometry(QtCore.QRect(168, 150, 100, 27))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_16 = QtWidgets.QLabel(self.tab)
        self.label_16.setGeometry(QtCore.QRect(20, 563, 240, 22))
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(0, 300, 160, 27))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab)
        self.comboBox_3.setGeometry(QtCore.QRect(168, 420, 140, 27))
        self.comboBox_3.setObjectName("comboBox_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(0, 210, 160, 27))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.doubleSpinBox_6 = QtWidgets.QDoubleSpinBox(self.tab)
        self.doubleSpinBox_6.setGeometry(QtCore.QRect(168, 360, 100, 27))
        self.doubleSpinBox_6.setLocale(QtCore.QLocale(QtCore.QLocale.C, QtCore.QLocale.AnyCountry))
        self.doubleSpinBox_6.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_6.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.doubleSpinBox_6.setMaximum(1.0)
        self.doubleSpinBox_6.setSingleStep(0.01)
        self.doubleSpinBox_6.setObjectName("doubleSpinBox_6")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(0, 270, 160, 27))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.dateEdit_1 = QtWidgets.QDateEdit(self.tab)
        self.dateEdit_1.setGeometry(QtCore.QRect(168, 390, 100, 27))
        self.dateEdit_1.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_1.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_1.setCalendarPopup(True)
        self.dateEdit_1.setObjectName("dateEdit_1")
        self.label_19 = QtWidgets.QLabel(self.tab)
        self.label_19.setGeometry(QtCore.QRect(20, 605, 240, 22))
        self.label_19.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(720, 7, 190, 30))
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName("label_13")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(0, 420, 160, 27))
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.toolButton_4 = QtWidgets.QToolButton(self.tab)
        self.toolButton_4.setGeometry(QtCore.QRect(410, 10, 26, 26))
        self.toolButton_4.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../icons/16x16/actions/edit-table-delete-row.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_4.setIcon(icon5)
        self.toolButton_4.setObjectName("toolButton_4")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.tab)
        self.graphicsView_2.setGeometry(QtCore.QRect(920, 40, 190, 595))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.tableSzond = QtWidgets.QTableView(self.tab)
        self.tableSzond.setGeometry(QtCore.QRect(320, 40, 392, 595))
        self.tableSzond.setObjectName("tableSzond")
        self.tableSzond.verticalHeader().setDefaultSectionSize(24)
        self.toolButton_5 = QtWidgets.QToolButton(self.tab)
        self.toolButton_5.setGeometry(QtCore.QRect(440, 10, 26, 26))
        self.toolButton_5.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../icons/16x16/actions/document-import.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_5.setIcon(icon6)
        self.toolButton_5.setObjectName("toolButton_5")
        self.label_21 = QtWidgets.QLabel(self.tab)
        self.label_21.setGeometry(QtCore.QRect(510, 10, 161, 27))
        self.label_21.setObjectName("label_21")
        self.graphicsView = QtWidgets.QGraphicsView(self.tab)
        self.graphicsView.setGeometry(QtCore.QRect(720, 40, 190, 595))
        self.graphicsView.setObjectName("graphicsView")
        self.label_23 = QtWidgets.QLabel(self.tab)
        self.label_23.setGeometry(QtCore.QRect(0, 180, 160, 27))
        self.label_23.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_23.setObjectName("label_23")
        self.comboBox_6 = QtWidgets.QComboBox(self.tab)
        self.comboBox_6.setGeometry(QtCore.QRect(170, 180, 140, 27))
        self.comboBox_6.setObjectName("comboBox_6")
        Szond_win.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout.setObjectName("gridLayout")
        self.tablePointSzond = QtWidgets.QTableView(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tablePointSzond.sizePolicy().hasHeightForWidth())
        self.tablePointSzond.setSizePolicy(sizePolicy)
        self.tablePointSzond.setObjectName("tablePointSzond")
        self.gridLayout.addWidget(self.tablePointSzond, 0, 0, 1, 1)
        Szond_win.addTab(self.tab_2, "")

        self.retranslateUi(Szond_win)
        Szond_win.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Szond_win)
        Szond_win.setTabOrder(self.comboBox_1, self.lineEdit_1)
        Szond_win.setTabOrder(self.lineEdit_1, self.comboBox_2)
        Szond_win.setTabOrder(self.comboBox_2, self.comboBox_6)
        Szond_win.setTabOrder(self.comboBox_6, self.doubleSpinBox_1)
        Szond_win.setTabOrder(self.doubleSpinBox_1, self.doubleSpinBox_2)
        Szond_win.setTabOrder(self.doubleSpinBox_2, self.doubleSpinBox_3)
        Szond_win.setTabOrder(self.doubleSpinBox_3, self.doubleSpinBox_4)
        Szond_win.setTabOrder(self.doubleSpinBox_4, self.doubleSpinBox_5)
        Szond_win.setTabOrder(self.doubleSpinBox_5, self.doubleSpinBox_6)
        Szond_win.setTabOrder(self.doubleSpinBox_6, self.dateEdit_1)
        Szond_win.setTabOrder(self.dateEdit_1, self.comboBox_3)
        Szond_win.setTabOrder(self.comboBox_3, self.comboBox_4)
        Szond_win.setTabOrder(self.comboBox_4, self.comboBox_5)
        Szond_win.setTabOrder(self.comboBox_5, self.tableSzond)
        Szond_win.setTabOrder(self.tableSzond, self.toolButton_1)
        Szond_win.setTabOrder(self.toolButton_1, self.toolButton_2)
        Szond_win.setTabOrder(self.toolButton_2, self.toolButton_3)
        Szond_win.setTabOrder(self.toolButton_3, self.toolButton_4)
        Szond_win.setTabOrder(self.toolButton_4, self.toolButton_5)
        Szond_win.setTabOrder(self.toolButton_5, self.toolButton_6)
        Szond_win.setTabOrder(self.toolButton_6, self.graphicsView)
        Szond_win.setTabOrder(self.graphicsView, self.graphicsView_2)
        Szond_win.setTabOrder(self.graphicsView_2, self.tablePointSzond)

    def retranslateUi(self, Szond_win):
        _translate = QtCore.QCoreApplication.translate
        Szond_win.setWindowTitle(_translate("Szond_win", "Статичне зондування"))
        self.doubleSpinBox_3.setSpecialValueText(_translate("Szond_win", "-"))
        self.toolButton_1.setToolTip(_translate("Szond_win", "Додати один рядок до таблиці"))
        self.toolButton_1.setStatusTip(_translate("Szond_win", "Додавання одного рядка до таблиці вимірювань статичного зондування"))
        self.label_10.setText(_translate("Szond_win", "Дата іспитів"))
        self.label_22.setText(_translate("Szond_win", "Геодезіст"))
        self.toolButton_3.setToolTip(_translate("Szond_win", "Додати всі рядки до таблиці"))
        self.toolButton_3.setStatusTip(_translate("Szond_win", "Додавання всіх рядків до таблиці вимірювань статичного зондування"))
        self.label.setText(_translate("Szond_win", "label"))
        self.label_5.setText(_translate("Szond_win", "Координата Y"))
        self.label_15.setText(_translate("Szond_win", "Кут при вершині конуса - 60 град."))
        self.label_9.setText(_translate("Szond_win", "Крок вимірювань (м)"))
        self.label_2.setText(_translate("Szond_win", "Тип зонда"))
        self.label_18.setText(_translate("Szond_win", "Зовнішній діаметр муфти - 35,7 мм"))
        self.label_8.setText(_translate("Szond_win", "Кінцева глибина (м)"))
        self.doubleSpinBox_2.setSpecialValueText(_translate("Szond_win", "-"))
        self.doubleSpinBox_4.setSpecialValueText(_translate("Szond_win", "-"))
        self.label_14.setText(_translate("Szond_win", "Номер свердловини"))
        self.toolButton_6.setToolTip(_translate("Szond_win", "Очистити комірку від значення"))
        self.toolButton_6.setStatusTip(_translate("Szond_win", "Очистити комірку від значення. Відобразити None"))
        self.label_3.setText(_translate("Szond_win", "Номер точки зондування"))
        self.toolButton_2.setToolTip(_translate("Szond_win", "Вилучити поточний рядок з таблиці"))
        self.toolButton_2.setStatusTip(_translate("Szond_win", "Вилучення поточного рядка з таблиці вимірювань статичного зондування"))
        self.label_17.setText(_translate("Szond_win", "Характеристика зонда"))
        self.doubleSpinBox_1.setSpecialValueText(_translate("Szond_win", "-"))
        self.label_20.setText(_translate("Szond_win", "Графік зміни fs (кПа) від глибини (м)"))
        self.label_12.setText(_translate("Szond_win", "Геолог"))
        self.doubleSpinBox_5.setSpecialValueText(_translate("Szond_win", "-"))
        self.label_16.setText(_translate("Szond_win", "Діаметр основи конуса - 35,7 мм"))
        self.label_7.setText(_translate("Szond_win", "Початкова глибина (м)"))
        self.label_4.setText(_translate("Szond_win", "Координата X"))
        self.doubleSpinBox_6.setSpecialValueText(_translate("Szond_win", "-"))
        self.label_6.setText(_translate("Szond_win", "Абсолютна відмітка (м)"))
        self.dateEdit_1.setDisplayFormat(_translate("Szond_win", "yyyy-MM-dd"))
        self.label_19.setText(_translate("Szond_win", "Довжина муфти тертя - 310 мм"))
        self.label_13.setText(_translate("Szond_win", "Графік зміни qc (МПа) від глибини (м)"))
        self.label_11.setText(_translate("Szond_win", "Буровий майстер"))
        self.toolButton_4.setToolTip(_translate("Szond_win", "Вилучити всі рядки з таблиці"))
        self.toolButton_4.setStatusTip(_translate("Szond_win", "Вилучення всіх рядків з таблиці вимірювань статичного зондування"))
        self.toolButton_5.setToolTip(_translate("Szond_win", "Імпортувати дані з першоджерела файлу CSV"))
        self.toolButton_5.setStatusTip(_translate("Szond_win", "Імпортує дані з файлу формату CSV"))
        self.label_21.setText(_translate("Szond_win", "Результати випробувань"))
        self.label_23.setText(_translate("Szond_win", "Система координат"))
        Szond_win.setTabText(Szond_win.indexOf(self.tab), _translate("Szond_win", "Один запис"))
        Szond_win.setTabText(Szond_win.indexOf(self.tab_2), _translate("Szond_win", "Таблиця"))
