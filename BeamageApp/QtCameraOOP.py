# -*- coding: utf-8 -*-
#
import sys

import matplotlib.pyplot as plt
import numpy as np

import pyqtgraph as pg
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from GUI_OOP import Ui_MainWindow
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import types

import clr
path1 = r".\BeamageSDKPy"
assembly_path = r".\BeamageSDKPy\BeamageCsh\BeamageApi\bin\Debug"
sys.path.append(assembly_path)
sys.path.append(path1)

import modesPattern as mp

def FieldRamochka(arr, x0, y0):
    if x0 == 0 or y0 == 0:
        return arr[0:400,0:400]
    else:
        return arr[abs(x0 - 200):200 + x0,abs(y0 - 200):200 + y0]

def set2dOptions(obj):
    mask = np.arange(0, 2048 * 2048, 2)
    bit = np.arange(0, 257, 1) / 256
    colmap = np.array(255 * plt.cm.nipy_spectral(bit), dtype=np.ubyte)
    cmap = pg.ColorMap(bit, colmap)
    lut = cmap.getLookupTable(0.0, 1.0, 255)
    obj.setLookupTable(lut)
    obj.setAutoDownsample(True)
    obj.setBorder('b')
    return obj

class ModesDecompositionApp(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None, *args, **kwargs):
        QMainWindow.__init__(self)
        self.setupUi(self)

        ###############################################################
# -------------------------------------------------------------------------------------------------------
        #### PyQT grapg инициализация окон ##########################

        self.shapeMainWindow = [2048, 2048]
        self.X, self.Y = np.mgrid[-500:500, -500:500]
        ######## Главное #################################################
        self.mainWindowCamera.setLayout(QtWidgets.QGridLayout())
        layout = self.mainWindowCamera.layout()
        win = pg.GraphicsWindow()
        layout.addWidget(win, 0, 0)
        self.Positioner = win.addPlot(row=0, col=0)
        self.imgMain = set2dOptions(pg.ImageItem())
        self.Positioner.addItem(self.imgMain)
        self.proxyMoved = pg.SignalProxy(self.Positioner.scene().sigMouseMoved, rateLimit=120, slot=self.mouseMoved)
        win.scene().sigMouseClicked.connect(self.crossHairPartial)
        ### Рисуем крестик ###############################################
        self.vLine = pg.InfiniteLine(angle=90, movable=False)
        self.hLine = pg.InfiniteLine(angle=0, movable=False)
        self.Positioner.addItem(self.vLine, ignoreBounds=True)
        self.Positioner.addItem(self.hLine, ignoreBounds=True)
        ###############################################################

        ######## Маленькое #################################################
        self.viewIntenference = pg.ViewBox()
        self.intenferenceWindow.setCentralItem(self.viewIntenference)
        self.imgIntenference = set2dOptions(pg.ImageItem())
        self.viewIntenference.addItem(self.imgIntenference)
        ###############################################################

        ######## Оригинал пучка #################################################
        self.viewBeamOrigin = pg.ViewBox()
        self.beamOrigin.setCentralItem(self.viewBeamOrigin)
        self.imgOriginBeam = set2dOptions(pg.ImageItem())
        self.viewBeamOrigin.addItem(self.imgOriginBeam)
        ###############################################################

        ######## Реконструкция пучка #################################################
        self.viewRecBeam = pg.ViewBox()
        self.recBeam.setCentralItem(self.viewRecBeam)
        self.imgRecBeam = set2dOptions(pg.ImageItem())
        self.viewRecBeam.addItem(self.imgRecBeam)
        #######################################################
#-------------------------------------------------------------------------------------------------------
        ###############################################################


        #### Инициализация обектов изображения для окон
        self.image = np.zeros((self.shapeMainWindow[0],self.shapeMainWindow[1]))
        self.imageModification = np.zeros((self.shapeMainWindow[0],self.shapeMainWindow[1]))
        self.dataBlackLevel = np.zeros((self.shapeMainWindow[0],self.shapeMainWindow[1]))
        self.Urec = ( np.zeros((1000,1000)) ).astype('complex128')

        ####### Инициализация таймеров ######################################
        self.timerMain = QtCore.QTimer()
        self.timerMain.timeout.connect(self.updateWindows)

        self.timerBackground = QtCore.QTimer()
        self.timerBackground.timeout.connect(self.setBlackLevel)

        self.timerDecomposition = QtCore.QTimer()
        self.timerDecomposition.setSingleShot(True)
        self.timerDecomposition.timeout.connect(self.decompositionMethod)
        ##########################################################

        ##### Инииализации кнопок #################################################
        self.start.clicked.connect(self.startPush)
        self.stop.clicked.connect(self.stopPush)

        self.InitButton.clicked.connect(self.initDevices)

        self.setBG.clicked.connect(self.PushBlackLevel)

        self.InitExperiment.clicked.connect(self.InitExperimentMethod)

        self.StartDecompose.clicked.connect(self.StartDecomposeMethod)
        self.StopDecompose.clicked.connect(self.StopDecomposeMethod)

        self.SaveButton.clicked.connect(self.SaveImage)
        ##########################################################

        ##### Инииализации переменных #################################################
        self.BufferSize = 5
        self.buffer = np.array([np.zeros((self.shapeMainWindow[0],self.shapeMainWindow[1])) for i in range(self.BufferSize)])
        self.numberBuffer = 0
        self.p = 0
        self.m = 0
        self.ismdruning = False
        self.setExposition = 10
        self.x0, self.y0 = self.shapeMainWindow[0] // 2, self.shapeMainWindow[1] // 2
        self.r0 = 1017. / 8.

        self.AmpZeros = 0

        self.pathSave.setText("V:/gonta/EndingDecomposition/191223/12kW/beam")
        self.pathDecompose.setText("V:/gonta/EndingDecomposition/191223/12kW/")
        ##########################################################

    ##############################################################
    ########### Button action #####################################
    def startPush(self):
        self.Beamage.start()
        mp.initSLM()
        self.timerMain.start(100)
        self.start.setEnabled(False)
        self.stop.setEnabled(True)

    def stopPush(self):
        self.Beamage.stop()
        self.timerMain.stop()
        self.start.setEnabled(True)
        self.stop.setEnabled(False)

    def PushBlackLevel(self):
        self.numberBuffer = 0  # обнуляем номер буффера
        self.timerMain.stop()  # Останавливаем таймер для накопления знания об уровне черного
        self.timerBackground.start()

    def setBlackLevel(self):

        #### Захват изображения с камеры ######################################
        self.image, self.saturation = self.Beamage.grab()
        self.buffer[self.numberBuffer] = self.image
        self.numberBuffer += 1
        ##############################################################
        if self.numberBuffer == self.BufferSize:
            self.dataBlackLevel = self.buffer.sum(axis=0) / (self.BufferSize)
            self.timerBackground.stop()
            self.timerMain.start()
        else:
            app.processEvents()

    def initDevices(self):
        try:

            clr.AddReference("BeamageSDK")
            from BeamageSDK import Beamage

            self.Beamage = Beamage()
            self.start.setEnabled(True)
        except:
            print("Devices are not visible")

    ########### Акции мыши #################################################
    def mouseMoved(self, evt):
        self.mousePoint = self.Positioner.vb.mapSceneToView(evt[0])
        self.vLine.setPos(self.mousePoint.x())
        self.hLine.setPos(self.mousePoint.y())

    def crossHairPartial(self):
        self.spinX.setValue(int(self.mousePoint.x()))
        self.spinY.setValue(int(self.mousePoint.y()))
    ##############################################################

    ### Инициализация модовой декомпозиции #####################################
    def InitExperimentMethod(self):
        mp.firstGenerate(self.r0)
        self.StartDecompose.setEnabled(True)
    ##############################################################

    def StartDecomposeMethod(self):
        self.Urec = np.zeros((1000, 1000))
        self.numberBuffer = 0
        self.timerDecomposition.start(1)
        self.ismdruning = True
        self.StopDecompose.setEnabled(True)
        self.StartDecompose.setEnabled(False)

    def StopDecomposeMethod(self):
        self.ismdruning = False
        self.StopDecompose.setEnabled(False)
        self.StartDecompose.setEnabled(True)
    ##############################################################
    ##############################################################

    def updateWindows(self):
        #### Захват изображения с камеры ######################################
        image, saturation = self.Beamage.grab()
        image -= self.dataBlackLevel
        image[image < 20] = 0  ### обнуление половины уровня шума после вычитания УЧ ля модифицированного изображения
        ##############################################################


        ### проверка на изменение экспозиции #######################
        if self.setExposition != int(self.spinBoxExpos.text()):
            self.Beamage.setExposition(int(self.spinBoxExpos.text()))
            self.setExposition = int(self.spinBoxExpos.text())
        ##############################################################

        ##############################################################
        self.x0, self.y0 = int(self.spinX.text()), int(self.spinY.text())
        ##############################################################
        self.r0 = float(self.spinSizeBeam.text()) / 8.
        #### Отображение всего ###########################################
        self.lcdNumberModes.display(2 * self.p + abs(self.m))
        self.lcdNumberModes_P.display(self.p)
        self.lcdNumberModes_M.display(self.m)
        self.saturationLevel.setText(str(int(saturation)) + "%")
        self.imgMain.setImage(image)#### Отображение изображения в окне
        self.imgIntenference.setImage(FieldRamochka(image, self.x0, self.y0))#### Отображение изображения в окне
        self.imgRecBeam.setImage(abs(self.Urec) ** 2)#### Отображение изображения в окне
        ##############################################################

        #app.processEvents()

    def decompositionMethod(self):
        for kk in range(1, 2):
            kk = ''
            for ord in range(0, 11):
                for j in range(-ord, ord + 1, 2):
                    if not self.ismdruning:
                        break
                    self.p = int((ord - abs(j)) // 2)
                    self.m = j

                    ########## Ищем амплитуду ##################################################################
                    normaAmp = mp.setPhase(self.p, self.m, self.r0)
                    for i in range(3):
                        app.processEvents()
                        mp.time.sleep(0.1)
                        for i in range(self.BufferSize):
                            #### Захват изображения с камеры ######################################
                            self.image, self.saturation = self.Beamage.grab()
                            self.image -= self.dataBlackLevel
                            self.image[self.image < 20] = 0
                            self.buffer[i] = self.image  ####### Пишем в буффер
                            app.processEvents()
                        ##############################################################
                    resImageAmp = self.image#self.buffer.sum(axis=0) / (self.BufferSize)
                    mp.release()
                    np.savez_compressed(
                        self.pathDecompose.text() + str(kk) + 'p_' + str(self.p) + ' m_' + str(self.m) + '.npz', a=resImageAmp, b=[self.x0, self.y0], c=self.r0,
                        d=normaAmp)
                    ##############################################################################################################

                    ########## Ищем косинус ##################################################################
                    normaCos = mp.setPhase_cos(self.p, self.m, self.r0)
                    for i in range(3):
                        app.processEvents()
                        mp.time.sleep(0.1)
                    for i in range(self.BufferSize):
                        #### Захват изображения с камеры ######################################
                        self.image, self.saturation = self.Beamage.grab()
                        self.image -= self.dataBlackLevel
                        self.image[self.image < 20] = 0
                        self.buffer[i] = self.image  ####### Пишем в буффер
                        app.processEvents()#############################################
                    resImageCos = self.image#self.buffer.sum(axis=0) / (self.BufferSize)
                    mp.release()
                    np.savez_compressed(
                        self.pathDecompose.text() + str(kk) + 'p_' + str(self.p) + ' m_' + str(self.m) + 'cos.npz', a=resImageCos, b=[self.x0, self.y0], c=self.r0,
                        d=normaCos)
                    ##############################################################################################################

                    ########## Ищем синус ##################################################################
                    normaSin = mp.setPhase_sin(self.p, self.m, self.r0)
                    for i in range(3):
                        app.processEvents()
                        mp.time.sleep(0.1)
                    for i in range(self.BufferSize):
                        #### Захват изображения с камеры ######################################
                        self.image, self.saturation = self.Beamage.grab()
                        self.image -= self.dataBlackLevel
                        self.image[self.image < 20] = 0
                        self.buffer[i] = self.image  ####### Пишем в буффер
                        app.processEvents()
                        ##############################################################
                    resImageSin = self.buffer.sum(axis=0) / (self.BufferSize)
                    mp.release()
                    np.savez_compressed(
                        self.pathDecompose.text() + str(kk) + 'p_' + str(self.p) + ' m_' + str(self.m) + 'sin.npz', a=resImageSin, b=[self.x0, self.y0], c=self.r0,
                        d=normaSin)
                    ##############################################################################################################

                    ##### Компилируем все #####################################################
                    if ord == 0:
                        self.AmpZeros = resImageAmp[self.x0, self.y0]
                        self.Urec = self.Urec + np.sqrt(self.AmpZeros) * mp.U(self.p, self.m, self.r0) * np.exp(1j * 0) * normaAmp
                        print(self.p, self.m, resImageAmp[self.x0, self.y0])
                    else:
                        SINdp = normaSin ** 2 * resImageSin[self.x0, self.y0] - resImageAmp[self.x0, self.y0] - self.AmpZeros
                        COSdp = normaCos ** 2 * resImageCos[self.x0, self.y0] - resImageAmp[self.x0, self.y0] - self.AmpZeros
                        dphi = -np.arctan2(SINdp, COSdp)
                        self.Urec += np.sqrt(resImageAmp[self.x0, self.y0]) * mp.U(self.p,self.m, self.r0) * np.exp(1j * dphi) * normaAmp

                        print(self.p, self.m, resImageAmp[self.x0, self.y0], "circle = ", (SINdp ** 2 + COSdp ** 2) / (4 * resImageAmp[self.x0, self.y0] * self.AmpZeros))
        ##############################################################################################################


    def SaveImage(self):
        for i in range(self.BufferSize):
            #### Захват изображения с камеры ######################################
            image, saturation = self.Beamage.grab()
            image -= self.dataBlackLevel
            image[image < 20] = 0
            self.buffer[i] = image  ####### Пишем в буффер
            ##############################################################
        res = self.buffer.sum(axis=0) / (self.BufferSize)
        np.savez_compressed(self.pathSave.text() + '.npz', a=res)


if __name__ == '__main__':
    app = QtGui.QApplication([])
    app.setStyle(QtGui.QStyleFactory.create("Cleanlooks"))
    image_widget = ModesDecompositionApp()
    image_widget.show()
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
