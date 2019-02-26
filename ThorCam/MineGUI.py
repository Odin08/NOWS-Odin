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
        Dialog.resize(1300, 1000)

        # Window for display image  ####################################################################################
        self.imshow = pg.GraphicsView(Dialog)
        self.imshow.setGeometry(QtCore.QRect(10, 10, 800, 800))
        self.imshow.setObjectName("imshow")

        # X and Y profile  #############################################################################################
        self.xprof = pg.PlotWidget(Dialog)
        self.xprof.setGeometry(QtCore.QRect(820, 10, 440, 280))
        self.xprof.setObjectName("xprof")
        self.xprof.setYRange(0, 100)
        self.xprof.getAxis('left').setPen(pg.mkPen(color='w', width=3))
        self.xprof.getAxis('bottom').setPen(pg.mkPen(color='w', width=3))

        self.yprof = pg.PlotWidget(Dialog)
        self.yprof.setGeometry(QtCore.QRect(820, 300, 440, 280))
        self.yprof.setObjectName("yprof")
        self.yprof.setYRange(0, 100)
        self.yprof.getAxis('left').setPen(pg.mkPen(color='w', width=3))
        self.yprof.getAxis('bottom').setPen(pg.mkPen(color='w', width=3))

        # Buttons ######################################################################################################
        self.startBtn = QtWidgets.QPushButton(Dialog)
        self.startBtn.setGeometry(QtCore.QRect(830, 780, 120, 50))
        self.startBtn.setObjectName("startBtn")
        self.stopBtn = QtWidgets.QPushButton(Dialog)
        self.stopBtn.setGeometry(QtCore.QRect(1100, 780, 120, 50))
        self.stopBtn.setObjectName("stopBtn")
        self.saveBtn = QtWidgets.QPushButton(Dialog)
        self.saveBtn.setGeometry(QtCore.QRect(1100, 860, 120, 50))
        self.saveBtn.setObjectName("saveBtn")

        self.M2Btn = QtWidgets.QPushButton(Dialog)
        self.M2Btn.setGeometry(QtCore.QRect(1100, 940, 120, 50))
        self.M2Btn.setObjectName("M2Btn")
        # TextBox for obtaned path to save directory  ##################################################################
        self.pathBox = QtWidgets.QLineEdit(Dialog)
        self.pathBox.setGeometry(QtCore.QRect(10, 880, 600, 25))
        self.pathBox.setObjectName("pathBox")

        self.nameBox = QtWidgets.QLineEdit(Dialog)
        self.nameBox.setGeometry(QtCore.QRect(610, 880, 200, 25))
        self.nameBox.setObjectName("nameBox")

        self.pathLable = QtWidgets.QLabel(Dialog)
        self.pathLable.setGeometry(QtCore.QRect(260, 830, 320, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pathLable.setFont(font)
        self.pathLable.setTextFormat(QtCore.Qt.AutoText)
        self.pathLable.setObjectName("pathLable")

        # Label for show value of beam size  ###########################################################################
        self.hwLabel = QtWidgets.QLabel(Dialog)
        self.hwLabel.setGeometry(QtCore.QRect(830, 630, 170, 70))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.hwLabel.setFont(font)
        self.hwLabel.setObjectName("hwLabel")

        self.sizeBeam = QtWidgets.QTextEdit(Dialog)
        self.sizeBeam.setGeometry(QtCore.QRect(1020, 650, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sizeBeam.setFont(font)
        self.sizeBeam.setObjectName("sizeBeam")

        # Average image  ###############################################################################################
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(940, 880, 45, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox.setFont(font)
        self.spinBox.setObjectName("spinNAverage")
        self.spinBox.setRange(1, 10)

        self.avrLabel = QtWidgets.QLabel(Dialog)
        self.avrLabel.setGeometry(QtCore.QRect(850, 830, 280, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.avrLabel.setFont(font)
        self.avrLabel.setObjectName("avrLabel")

        # Resize image  ################################################################################################
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(440, 935, 45, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox.setFont(font)
        self.spinBox.setObjectName("spinResize")
        self.spinBox.setRange(1, 4)

        self.resizeLabel = QtWidgets.QLabel(Dialog)
        self.resizeLabel.setGeometry(QtCore.QRect(10, 920, 430, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.resizeLabel.setFont(font)
        self.resizeLabel.setObjectName("ResizeLabel")

        # Label for show value of exposure time ########################################################################
        self.exposLabel = QtWidgets.QLabel(Dialog)
        self.exposLabel.setGeometry(QtCore.QRect(20, 10, 140, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.exposLabel.setFont(font)
        self.exposLabel.setStyleSheet("color: rgb(255,255,255)")
        self.exposLabel.setObjectName("exposLabel")

        self.exposValue = QtWidgets.QLabel(Dialog)
        self.exposValue.setGeometry(QtCore.QRect(150, 15, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.exposValue.setFont(font)
        self.exposValue.setStyleSheet("color: rgb(255,255,255)")
        self.exposValue.setObjectName("exposLabel")


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.startBtn.setText(_translate("Dialog", "Запустить"))
        self.stopBtn.setText(_translate("Dialog", "Остановить"))
        self.saveBtn.setText(_translate("Dialog", "Сохранить"))
        self.M2Btn.setText(_translate("Dialog", "М2"))
        self.pathLable.setText(_translate("Dialog", "Укажите путь и название файла"))
        self.avrLabel.setText(_translate("Dialog", "Колличество усреднений"))
        self.hwLabel.setText(_translate("Dialog", "<html><head/><body><p>Радиус пучка</p><p>по уровню exp(-2)</p></body></html>"))
        self.exposLabel.setText(_translate("Dialog", "Экспозиция:"))
        self.resizeLabel.setText(_translate("Dialog", "Изменение размера основного окна (от 0 до 4)"))