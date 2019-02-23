# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\God\Desktop\Qtplay\windows.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 180)


        # Buttons ######################################################################################################
        self.startBtn = QtWidgets.QPushButton(Dialog)
        self.startBtn.setGeometry(QtCore.QRect(10, 10, 120, 50))
        self.startBtn.setObjectName("startBtn")

        self.stopBtn = QtWidgets.QPushButton(Dialog)
        self.stopBtn.setGeometry(QtCore.QRect(160, 10, 120, 50))
        self.stopBtn.setObjectName("stopBtn")

        self.M2Btn = QtWidgets.QPushButton(Dialog)
        self.M2Btn.setGeometry(QtCore.QRect(310, 10, 120, 50))
        self.M2Btn.setObjectName("M2Btn")

        self.saveBtn = QtWidgets.QPushButton(Dialog)
        self.saveBtn.setGeometry(QtCore.QRect(450, 80, 120, 50))
        self.saveBtn.setObjectName("saveBtn")

        # TextBox for obtaned path to save directory  ##################################################################
        self.pathBox = QtWidgets.QLineEdit(Dialog)
        self.pathBox.setGeometry(QtCore.QRect(10, 90, 300, 25))
        self.pathBox.setObjectName("pathBox")

        self.nameBox = QtWidgets.QLineEdit(Dialog)
        self.nameBox.setGeometry(QtCore.QRect(320, 90, 100, 25))
        self.nameBox.setObjectName("nameBox")


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.startBtn.setText(_translate("Dialog", "Запустить"))
        self.stopBtn.setText(_translate("Dialog", "Остановить"))
        self.saveBtn.setText(_translate("Dialog", "Сохранить"))
        self.M2Btn.setText(_translate("Dialog", "М2"))

