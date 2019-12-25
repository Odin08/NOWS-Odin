# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\App_v4.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 980)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(140, 10, 330, 40))
        self.textBrowser.setObjectName("textBrowser")
        self.StartDecompose = QtWidgets.QPushButton(self.centralwidget)
        self.StartDecompose.setEnabled(False)
        self.StartDecompose.setGeometry(QtCore.QRect(1340, 800, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.StartDecompose.setFont(font)
        self.StartDecompose.setObjectName("StartDecompose")
        self.ylabel_5 = QtWidgets.QLabel(self.centralwidget)
        self.ylabel_5.setGeometry(QtCore.QRect(1100, 690, 51, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ylabel_5.setFont(font)
        self.ylabel_5.setAlignment(QtCore.Qt.AlignCenter)
        self.ylabel_5.setObjectName("ylabel_5")
        self.pathDecompose = QtWidgets.QLineEdit(self.centralwidget)
        self.pathDecompose.setGeometry(QtCore.QRect(1230, 850, 581, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pathDecompose.setFont(font)
        self.pathDecompose.setText("")
        self.pathDecompose.setObjectName("pathDecompose")
        self.beamOrigin = pg.GraphicsView(self.centralwidget)
        self.beamOrigin.setGeometry(QtCore.QRect(1600, 110, 241, 241))
        self.beamOrigin.setToolTipDuration(-3)
        self.beamOrigin.setObjectName("beamOrigin")
        self.spinY = QtWidgets.QSpinBox(self.centralwidget)
        self.spinY.setGeometry(QtCore.QRect(1643, 732, 100, 27))
        self.spinY.setObjectName("spinY")
        self.spinY.setMinimum(0)
        self.spinY.setMaximum(2048)
        self.ylabel_4 = QtWidgets.QLabel(self.centralwidget)
        self.ylabel_4.setGeometry(QtCore.QRect(1180, 650, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ylabel_4.setFont(font)
        self.ylabel_4.setObjectName("ylabel_4")
        self.InitButton = QtWidgets.QPushButton(self.centralwidget)
        self.InitButton.setGeometry(QtCore.QRect(1560, 10, 321, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.InitButton.setFont(font)
        self.InitButton.setObjectName("InitButton")
        self.lcdNumberModes = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumberModes.setGeometry(QtCore.QRect(1220, 650, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lcdNumberModes.setFont(font)
        self.lcdNumberModes.setStyleSheet("color: rgb(255, 0, 0);")
        self.lcdNumberModes.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdNumberModes.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumberModes.setLineWidth(1)
        self.lcdNumberModes.setMidLineWidth(0)
        self.lcdNumberModes.setSmallDecimalPoint(False)
        self.lcdNumberModes.setDigitCount(1)
        self.lcdNumberModes.setProperty("value", 0.0)
        self.lcdNumberModes.setProperty("intValue", 0)
        self.lcdNumberModes.setObjectName("lcdNumberModes")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(1230, 920, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(990, 850, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setEnabled(False)
        self.stop.setGeometry(QtCore.QRect(70, 10, 61, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.stop.setFont(font)
        self.stop.setStyleSheet("background-color: rgb(255, 96, 99);")
        self.stop.setObjectName("stop")
        self.InitExperiment = QtWidgets.QPushButton(self.centralwidget)
        self.InitExperiment.setGeometry(QtCore.QRect(990, 800, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.InitExperiment.setFont(font)
        self.InitExperiment.setObjectName("InitExperiment")
        self.StopDecompose = QtWidgets.QPushButton(self.centralwidget)
        self.StopDecompose.setEnabled(False)
        self.StopDecompose.setGeometry(QtCore.QRect(1590, 800, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.StopDecompose.setFont(font)
        self.StopDecompose.setObjectName("StopDecompose")
        self.SaveButton = QtWidgets.QPushButton(self.centralwidget)
        self.SaveButton.setGeometry(QtCore.QRect(990, 910, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.SaveButton.setFont(font)
        self.SaveButton.setObjectName("SaveButton")
        self.spinX = QtWidgets.QSpinBox(self.centralwidget)
        self.spinX.setGeometry(QtCore.QRect(1643, 700, 100, 27))
        self.spinX.setObjectName("spinX")
        self.spinX.setMinimum(0)
        self.spinX.setMaximum(2048)
        self.spinSizeBeam = QtWidgets.QSpinBox(self.centralwidget)
        self.spinSizeBeam.setGeometry(QtCore.QRect(1643, 670, 100, 27))
        self.spinSizeBeam.setObjectName("spinSizeBeam")
        self.spinSizeBeam.setMinimum(50)
        self.spinSizeBeam.setMaximum(10000)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(540, 10, 171, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.setBG = QtWidgets.QPushButton(self.centralwidget)
        self.setBG.setGeometry(QtCore.QRect(780, 10, 291, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.setBG.setFont(font)
        self.setBG.setObjectName("setBG")
        self.saturationLevel = QtWidgets.QLineEdit(self.centralwidget)
        self.saturationLevel.setGeometry(QtCore.QRect(710, 10, 61, 40))
        self.saturationLevel.setObjectName("saturationLevel")
        self.yline_2 = QtWidgets.QFrame(self.centralwidget)
        self.yline_2.setGeometry(QtCore.QRect(1540, 70, 31, 541))
        self.yline_2.setLineWidth(0)
        self.yline_2.setMidLineWidth(4)
        self.yline_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.yline_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.yline_2.setObjectName("yline_2")
        self.mainWindowCamera = QtWidgets.QWidget(self.centralwidget)#pg.GraphicsView(self.centralwidget)
        self.mainWindowCamera.setGeometry(QtCore.QRect(10, 60, 900, 900))
        self.mainWindowCamera.setObjectName("mainWindowCamera")
        self.intenferenceWindow = pg.GraphicsView(self.centralwidget)
        self.intenferenceWindow.setGeometry(QtCore.QRect(1010, 110, 500, 500))
        self.intenferenceWindow.setToolTipDuration(-3)
        self.intenferenceWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.intenferenceWindow.setObjectName("intenferenceWindow")
        self.line_11 = QtWidgets.QFrame(self.intenferenceWindow)
        self.line_11.setGeometry(QtCore.QRect(249, 0, 2, 230))
        self.line_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.line_11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_11.setLineWidth(2)
        self.line_11.setMidLineWidth(0)
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(self.intenferenceWindow)
        self.line_12.setGeometry(QtCore.QRect(0, 249, 230, 2))
        self.line_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.line_12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_12.setLineWidth(2)
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setObjectName("line_12")
        self.line_13 = QtWidgets.QFrame(self.intenferenceWindow)
        self.line_13.setGeometry(QtCore.QRect(249, 270, 2, 230))
        self.line_13.setStyleSheet("color: rgb(255, 255, 255);")
        self.line_13.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_13.setLineWidth(2)
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setObjectName("line_13")
        self.line_14 = QtWidgets.QFrame(self.intenferenceWindow)
        self.line_14.setGeometry(QtCore.QRect(270, 249, 230, 2))
        self.line_14.setStyleSheet("color: rgb(255, 255, 255);")
        self.line_14.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_14.setLineWidth(2)
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setObjectName("line_14")
        self.lcdNumberModes_P = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumberModes_P.setGeometry(QtCore.QRect(1150, 690, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lcdNumberModes_P.setFont(font)
        self.lcdNumberModes_P.setStyleSheet("color: rgb(255, 0, 0);")
        self.lcdNumberModes_P.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdNumberModes_P.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumberModes_P.setLineWidth(1)
        self.lcdNumberModes_P.setMidLineWidth(0)
        self.lcdNumberModes_P.setSmallDecimalPoint(False)
        self.lcdNumberModes_P.setDigitCount(1)
        self.lcdNumberModes_P.setProperty("value", 0.0)
        self.lcdNumberModes_P.setProperty("intValue", 0)
        self.lcdNumberModes_P.setObjectName("lcdNumberModes_P")
        self.ylabel_6 = QtWidgets.QLabel(self.centralwidget)
        self.ylabel_6.setGeometry(QtCore.QRect(1240, 690, 51, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ylabel_6.setFont(font)
        self.ylabel_6.setAlignment(QtCore.Qt.AlignCenter)
        self.ylabel_6.setObjectName("ylabel_6")
        self.lcdNumberModes_M = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumberModes_M.setGeometry(QtCore.QRect(1290, 690, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lcdNumberModes_M.setFont(font)
        self.lcdNumberModes_M.setStyleSheet("color: rgb(255, 0, 0);")
        self.lcdNumberModes_M.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdNumberModes_M.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumberModes_M.setLineWidth(1)
        self.lcdNumberModes_M.setMidLineWidth(0)
        self.lcdNumberModes_M.setSmallDecimalPoint(False)
        self.lcdNumberModes_M.setDigitCount(1)
        self.lcdNumberModes_M.setProperty("value", 0.0)
        self.lcdNumberModes_M.setProperty("intValue", 0)
        self.lcdNumberModes_M.setObjectName("lcdNumberModes_M")
        self.pathSave = QtWidgets.QLineEdit(self.centralwidget)
        self.pathSave.setGeometry(QtCore.QRect(1300, 920, 581, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pathSave.setFont(font)
        self.pathSave.setObjectName("pathSave")
        self.recBeam = pg.GraphicsView(self.centralwidget)
        self.recBeam.setGeometry(QtCore.QRect(1600, 370, 241, 241))
        self.recBeam.setToolTipDuration(-3)
        self.recBeam.setObjectName("recBeam")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setEnabled(False)
        self.start.setGeometry(QtCore.QRect(10, 10, 60, 40))

        self.spinBoxExpos = QtWidgets.QSpinBox(self.textBrowser)
        self.spinBoxExpos.setGeometry(QtCore.QRect(250, 0, 80, 40))
        self.spinBoxExpos.setObjectName("spinX")
        self.spinBoxExpos.setMinimum(10)
        self.spinBoxExpos.setMaximum(200)

        font = QtGui.QFont()
        font.setPointSize(16)
        self.start.setFont(font)
        self.start.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.start.setObjectName("start")
        self.ylabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.ylabel_2.setGeometry(QtCore.QRect(1060, 60, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.ylabel_2.setFont(font)
        self.ylabel_2.setObjectName("ylabel_2")
        self.ylabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.ylabel_3.setGeometry(QtCore.QRect(1610, 60, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.ylabel_3.setFont(font)
        self.ylabel_3.setObjectName("ylabel_3")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(1430, 640, 331, 120))
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 253, 192))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 253, 192))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 253, 192))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        self.tableWidget.setItem(2, 0, item)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(950, 890, 951, 20))
        self.line.setLineWidth(10)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tableWidget.raise_()
        self.textBrowser.raise_()
        self.StartDecompose.raise_()
        self.ylabel_5.raise_()
        self.pathDecompose.raise_()
        self.beamOrigin.raise_()
        self.spinY.raise_()
        self.ylabel_4.raise_()
        self.InitButton.raise_()
        self.lcdNumberModes.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.stop.raise_()
        self.InitExperiment.raise_()
        self.StopDecompose.raise_()
        self.SaveButton.raise_()
        self.spinX.raise_()
        self.spinSizeBeam.raise_()
        self.label.raise_()
        self.setBG.raise_()
        self.saturationLevel.raise_()
        self.yline_2.raise_()
        self.mainWindowCamera.raise_()
        self.intenferenceWindow.raise_()
        self.lcdNumberModes_P.raise_()
        self.ylabel_6.raise_()
        self.lcdNumberModes_M.raise_()
        self.pathSave.raise_()
        self.recBeam.raise_()
        self.start.raise_()
        self.ylabel_2.raise_()
        self.ylabel_3.raise_()
        self.line.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Время экспозиции (мс):</span></p></body></html>"))
        self.StartDecompose.setText(_translate("MainWindow", "Начать разложение"))
        self.ylabel_5.setText(_translate("MainWindow", "p  = "))
        self.ylabel_4.setText(_translate("MainWindow", "n = "))
        self.InitButton.setText(_translate("MainWindow", "Инициализация камеры и SLM"))
        self.lineEdit.setText(_translate("MainWindow", "Путь:"))
        self.lineEdit_2.setText(_translate("MainWindow", "Путь декомпозиции:"))
        self.stop.setText(_translate("MainWindow", "Стоп"))
        self.InitExperiment.setText(_translate("MainWindow", "Инициализация"))
        self.StopDecompose.setText(_translate("MainWindow", "Завершить"))
        self.SaveButton.setText(_translate("MainWindow", "Сохранить"))
        self.label.setText(_translate("MainWindow", "Насыщение (%):"))
        self.setBG.setText(_translate("MainWindow", "Установить уровень чёрного"))
        self.ylabel_6.setText(_translate("MainWindow", "m = "))
        self.start.setText(_translate("MainWindow", "Пуск"))
        self.ylabel_2.setText(_translate("MainWindow", "Результат интенференции"))
        self.ylabel_3.setText(_translate("MainWindow", "Реконстуркция"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Радиус моды (мкм)"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Положение центра по X"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Положение центра по Y"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Значения"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)